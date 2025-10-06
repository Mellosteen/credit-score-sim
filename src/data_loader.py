from __future__ import annotations
from functools import lru_cache
from pathlib import Path
import json

MAIN_CATEGORIES = {"revolving", "installment", "mortgage", "retail"}

def _project_root() -> Path:
    # src/ -> project root
    return Path(__file__).resolve().parents[1]

def _default_data_path() -> Path:
    return _project_root() / "data" / "credit_subtypes.json"

@lru_cache(maxsize=1)
def load_subtype_map(path: str | Path | None = None) -> dict[str, str]:
    """Load categories->subtypes and invert to {subtype: main_category}.
    - Normalizes all keys to lowercase.
    - Validates duplicates and unknown categories.
    """
    p = Path(path) if path else _default_data_path()
    with p.open("r", encoding="utf-8") as f:
        raw = json.load(f)

    cats = raw.get("categories", {})
    subtype_to_cat: dict[str, str] = {}

    for cat, subtypes in cats.items():
        cat_norm = cat.strip().lower()
        if cat_norm not in MAIN_CATEGORIES:
            raise ValueError(f"Unknown category in data file: {cat!r}")
        for s in subtypes:
            s_norm = s.strip().lower()
            if s_norm in subtype_to_cat:
                raise ValueError(f"Subtype listed twice across categories: {s!r}")
            subtype_to_cat[s_norm] = cat_norm

    return subtype_to_cat