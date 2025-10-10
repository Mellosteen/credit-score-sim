import json
from typing import List, Dict, Any, Optional

class Profile:
    def __init__(self, accounts: Optional[List[Dict[str, Any]]] = None):
        self.accounts: List[Dict[str, Any]] = accounts or []

    # ---- CRUD ----
    def add_account(self, account: Dict[str, Any]) -> None:
        existing = self.get_account(account["id"])
        if existing:
            self.accounts = [a if a["id"] != account["id"] else account for a in self.accounts]
        else:
            self.accounts.append(account)

    def remove_account(self, account_id: str) -> bool:
        before = len(self.accounts)
        self.accounts = [a for a in self.accounts if a["id"] != account_id]
        return len(self.accounts) < before

    def get_account(self, account_id: str) -> Optional[Dict[str, Any]]:
        return next((a for a in self.accounts if a["id"] == account_id), None)

    def list_accounts(self) -> List[Dict[str, Any]]:
        return list(self.accounts)

    # ---- Mutations ----
    def set_balance(self, account_id: str, balance: float) -> None:
        acc = self.get_account(account_id)
        if not acc:
            raise KeyError(f"Account '{account_id}' not found.")
        acc["balance"] = float(balance)

    def set_limit(self, account_id: str, limit: float) -> None:
        acc = self.get_account(account_id)
        if not acc:
            raise KeyError(f"Account '{account_id}' not found.")
        if not acc.get("has_limit", False):
            acc["has_limit"] = True
        acc["limit"] = float(limit)

    def close_account(self, account_id: str) -> None:
        acc = self.get_account(account_id)
        if not acc:
            raise KeyError(f"Account '{account_id}' not found.")
        acc["is_open"] = False

    # ---- Rollups ----
    def totals(self) -> Dict[str, float]:
        total_limit = 0.0
        total_balance = 0.0
        total_rev_limit = 0.0
        total_rev_balance = 0.0
        for a in self.accounts:
            bal = float(a.get("balance", 0.0))
            lim = float(a.get("limit", 0.0)) if a.get("has_limit", False) else 0.0
            total_balance += bal
            total_limit += lim
            if a.get("main_type") == "revolving":
                total_rev_balance += bal
                total_rev_limit += lim
        util_all = (total_balance / total_limit) * 100.0 if total_limit > 0 else 0.0
        util_rev = (total_rev_balance / total_rev_limit) * 100.0 if total_rev_limit > 0 else 0.0
        return {
            "total_balance": round(total_balance, 2),
            "total_limit": round(total_limit, 2),
            "overall_utilization_pct": round(util_all, 2),
            "revolving_utilization_pct": round(util_rev, 2),
        }

    # ---- Persistence ----
    def to_json(self, path: str) -> None:
        import io
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"accounts": self.accounts}, f, indent=2)

    @classmethod
    def from_json(cls, path: str) -> "Profile":
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return cls(accounts=data.get("accounts", []))