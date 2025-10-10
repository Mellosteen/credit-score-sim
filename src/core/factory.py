from copy import deepcopy
from typing import Dict, Any, Tuple
from src.config.credit_types import CREDIT_TYPES, SUB_TO_MAIN_MAP

class UnknownCreditType(Exception): ...
class InvalidSubtype(Exception): ...

def _resolve_template(subtype: str) -> Tuple[str, Dict[str, Any]]:
    if subtype not in SUB_TO_MAIN_MAP:
        raise UnknownCreditType(f"Subtype '{subtype}' not found in SUB_TO_MAIN_MAP.")
    main = SUB_TO_MAIN_MAP[subtype]
    if main not in CREDIT_TYPES:
        raise UnknownCreditType(f"Main type '{main}' not found in CREDIT_TYPES.")
    node = CREDIT_TYPES[main]
    defaults = deepcopy(node.get("defaults", {}))
    subnode = node.get("subtypes", {}).get(subtype)
    if subnode is None:
        raise InvalidSubtype(f"Subtype '{subtype}' not defined under main '{main}'.")
    merged = {**defaults, **deepcopy(subnode)}
    return main, merged

def create_account(subtype: str, **overrides) -> Dict[str, Any]:
    main, tpl = _resolve_template(subtype)
    acc = {
        "id": overrides.pop("id", None) or f"{subtype}-acc",
        "main_type": main,
        "subtype": subtype,
    }
    acc.update(tpl)
    acc.update(overrides)
    if acc.get("has_limit", False) and "limit" not in acc:
        acc["limit"] = 0.0
    if "balance" not in acc:
        acc["balance"] = acc.get("original_principal", 0.0)
    return acc