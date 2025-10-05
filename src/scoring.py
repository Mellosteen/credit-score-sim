from dataclasses import dataclass

LOW = 300
HIGH = 850

@dataclass
class Factors:
    # keep just two factors for now
    on_time_payment_rate: float  # 0..1
    utilization: float           # 0..1

def score(f: Factors) -> float:
    """
    v0: super simple weighted formula:
    - payment history (70%)
    - utilization (30%, best is low utilization)
    """
    pay_sub = max(0.0, min(1.0, f.on_time_payment_rate))
    u = max(0.0, min(1.0, f.utilization))
    util_sub = 1.0 - u  # 0 util -> 1.0 (great); 1.0 util -> 0.0 (bad)

    raw = 0.70 * pay_sub + 0.30 * util_sub
    return LOW + raw * (HIGH - LOW)