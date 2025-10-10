from dataclasses import dataclass
from typing import Mapping
from src.config.credit_types import SUB_TO_MAIN_MAP

LOW = 300
HIGH = 850

# Align to your actual main types in config
MAIN_TYPE_WEIGHTS = {
    "revolving": 0.35,     # example weights; adjust later
    "installment": 0.25,
    "open": 0.15,
    "other": 0.25,
}

@dataclass
class Factors:
    """
    Scoring inputs (toy model for now).
    """
    on_time_payment_rate: float  # 0..1
    utilization: float           # 0..1
    avg_account_age_months: int  # 1..240
    recent_inquiries: int        # 0..5
    mix_score: float             # 0..1

    @staticmethod
    def mix_scoring(credit_types: Mapping[str, bool]) -> float:
        """
        credit_types: dict of {subtype_name: True/False} where True means the user holds ≥1 account of that subtype.
        We collapse subtypes into main types via SUB_TO_MAIN_MAP and score based on diversity across mains.
        """
        mains_present = set()
        for subtype, has in credit_types.items():
            if not has:
                continue
            main = SUB_TO_MAIN_MAP.get(subtype)
            if main:
                mains_present.add(main)

        # Simple diversity score across mains present.
        # 0 if only one main type; 1 if you cover all mains proportionally to weights.
        # Here we use the sum of weights for mains you have, divided by total weight mass.
        total_weight = sum(MAIN_TYPE_WEIGHTS.values())
        covered_weight = sum(MAIN_TYPE_WEIGHTS.get(m, 0.0) for m in mains_present)
        return 0.0 if total_weight == 0 else min(1.0, covered_weight / total_weight)

def _clamp(x, lo, hi): 
    return max(lo, min(hi, x))

def score(f: Factors) -> float:
    """
    Toy score: weighted linear blend normalized into [LOW, HIGH].
    You can replace this later when your sim loop is in place.
    """
    # Simple weights (placeholder)
    w_pay = 0.35
    w_util = 0.30
    w_age = 0.15
    w_inq = 0.10
    w_mix = 0.10

    pay = _clamp(f.on_time_payment_rate, 0, 1)
    util = 1 - _clamp(f.utilization, 0, 1)               # lower util -> higher score
    age = _clamp(f.avg_account_age_months / 72.0, 0, 1)   # full credit at 72 months
    inq = 1 - _clamp(f.recent_inquiries / 5.0, 0, 1)      # fewer inquiries -> higher
    mix = _clamp(f.mix_score, 0, 1)

    raw = (w_pay*pay + w_util*util + w_age*age + w_inq*inq + w_mix*mix)
    return LOW + raw * (HIGH - LOW)