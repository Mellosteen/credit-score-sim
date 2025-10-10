# Path src/config/credit_types.py

MAIN_TYPES = {"revolving", "installment", "open", "other"}

SUB_TO_MAIN_MAP = {
    # Revolving credit subtypes
    "credit_card": "revolving",
    "store_card": "revolving",
    "secured_credit_card": "revolving",
    "personal_line_of_credit": "revolving",
    "department_store_card": "revolving",
    "heloc": "revolving",

    # Installment credit subtypes 
    "auto_loan": "installment",
    "personal_loan": "installment",
    "student_loan": "installment",
    "debt_consolidation_loan": "installment",
    "motorcycle_loan": "installment",
    "first_mortgage": "installment",
    "second_mortgage": "installment",
    "home_equity_loan": "installment",
    "construction_loan": "installment",

    # Open credit subtypes
    "charge_card": "open",

    # All other unlisted types will be placed under other for now...
}

CREDIT_TYPES = {
    
    # Holds details on all main credit types including default values upon initialization of all instances, 
    # which is shared amongst all subtypes. Attributes under subtypes 
    # are only meant to override or add additional attributes that are type-specific!
    # See Notion for further explanation.

    # !!! Keys with only types marked with hints as values need to be changed!!!

    # Begin revolving credit dict
    "revolving": {
        "defaults": {
            "include_utilization": True,
            "has_limit": True,
            "required_full_pay": False,
            "apr_annual": 0.24,
            "is_open": True,
            "is_reported": True,
            "grace_period_days": 25,
            "min_payment_rule": {"fixed": 25, "pct": 0.02},
            "late_fee": 35,  
        },

        "subtypes": {
            "credit_card": {
                "limit": 2000,
                "balance": 0.0,
            },
            "store_card": {
                "apr_annual": 0.29,
                "limit": 1000,
                "balance": 0.0,
            },
            "secured_credit_card": {
                "deposit": 300,
                "limit": 300,
                "balance": 0.0,
            },    
            "personal_line_of_credit": {
                "limit": 5000,
                "balance": 0.0,
            },  
            "department_store_card": {
                "min_payment_rule": {"fixed": 20, "pct": 0.04},
                "limit": 1000,
                "balance": 0.0,
            },
            "heloc": {
                "apr_annual": 0.09,
                "limit": 50000,
                "variable_rate": True,
                "draw_period_months": 120,
            }
        },
    },      # End revolving credit dict

    # Begin installment credit dict
    "installment": {
        "defaults": {
            "include_utilization": False,
            "has_limit": False,
            "required_full_pay": False,
            "apr_annual": 0.06,
            "is_open": True,
            "is_reported": True,
            "amortization": "fixed",
            "compounding": "monthly",
            "late_fee": 35,     # May require adjustment/overrides later
        },

        "subtypes": {
            "auto_loan": {
                "original_principal": 15000,
                "term_months": 60,
                "collateral": "vehicle",
            },
            "personal_loan": {
                "original_principal": 5000,
                "term_months": 36,
                "apr_annual": 0.11,
            },
            "student_loan": {
                "original_principal": 12000,
                "term_months": 120,
                "apr_annual": 0.065,
                "deferment_allowed": True,
            },
            "debt_consolidation_loan": {
                "original_principal": 10000,
                "term_months": 48,
            },
            "motorcycle_loan": {
                "original_principal": 8000,
                "term_months": 48,
                "collateral": "vehicle",
            },

            # Mortgage type installments
            "first_mortgage": {
                "original_principal": 250000,
                "term_months": 360,
                "apr_annual": 0.045,
            },
            "second_mortgage": {
                "original_principal": 30000,
                "term_months": 180,
                "apr_annual": 0.06,
            },
            "home_equity_loan": {
                "original_principal": 40000,
                "term_months": 120,
                "apr_annual": 0.07,
            },
            "construction_loan": {
                "original_principal": 150000,
                "term_months": 12,
                "interest_only": True,
                "apr_annual": 0.08,
            },
        }
    },      # End installment credit dict

    # Begin open credit dict
    "open": {
        "defaults": {
            "required_full_pay": True,
            "include_utilization": False,
            "has_limit": False,
            "is_open": True,
            "is_reported": True,
            "grace_period_days": 25,
            "late_fee": 35,
        },

        "subtypes": {
            "charge_card": {    },  # required_full_pay = True, so no min_payment_rule is not needed.
        },
    },

    # Begin other credit dict
    "other": {
        "defaults": {
            "include_utilization": False,
            "has_limit": False,
            "required_full_pay": False,
            "apr_annual": 0.1,
            "is_open": True,
            "is_reported": True,
        },
    },      # End other credit dict
}       