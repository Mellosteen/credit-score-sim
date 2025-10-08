from dataclasses import dataclass, field
from src.data_loader import load_subtype_map

# Global constants here
MONTH_IDX = 0

@dataclass
class Account:
    """
    Account will contain variables for dictionaries for different types of credit.
    Simulates the characteristic that a given account can have different types of credit.
    Goal: Expand upon the factors that are used in scoring.py.
    """

    # Identification Attributes
    id: int
    opened_month: int               # Reference potentially a globel month index counter
    closed_month: int               # "
    type: str                       # Identifies type of credit, follows lowercase and spaced-by-underscore format

    # Financial Attributes
    limit: float                    # For revolving credit types
    balance: float                  # Current owed balance for credit
    apr_annual: float               # Annual interest rate
    payment_due: float              # Amount due on current month
    min_payment_rule: float              # Percentage or fixed value, decide later

    # Behavorial Attributes
    on_time_payments: float         # Count number of months of on-time payments
    late_payments: float            # Same with late payments
    last_payment_month: int         # Records lateness or recency

    # Derived metrics
    utilization = balance / limit   # For credit cards
    age_in_month = MONTH_IDX - opened_month

    # Dict for credit types, see scoring.py
    credit_types: dict = field(default_factory = dict)