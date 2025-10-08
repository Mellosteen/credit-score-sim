# Path src/confing/credit_types.py

MAIN_TYPES = {"revolving", "installment", "mortgage", "retail", "other"}

SUB_TO_MAIN_MAP = {
    # Revolving credit subtypes
    "credit_card": "revolving",
    "charge_card": "revolving",
    "store_card": "revolving",
    "secured_credit_card": "revolving",
    "personal_line_of_credit": "revolving",
    "heloc": "revolving",

    # Installment credit subtypes 
    "auto_loan": "installment",
    "personal_loan": "installment",
    "student_loan": "installment",
    "debt_consolidation_loan": "installment",
    "motorcycle_loan": "installment",

    # Mortgage credit subtypes
    "first_mortgage": "mortgage",
    "second_mortgage": "mortgage",
    "home_equity_loan": "mortgage",
    "construction_loan": "mortgage",

    # Retail credit subtypes
    "department_store_card": "retail",
    "electronics_financing": "retail",

    # All other unlisted types will be placed under other for now...
}

CREDIT_TYPES = {
    
    # Holds details on all main credit types including default values upon initialization of all instances, 
    # which is shared amongst all subtypes. Attributes under subtypes 
    # are only meant to override or add additional attributes that are type-specific!
    # See Notion for further explanation.

    # !!! Keys with only types marked with hints as values need to be changed!!!

    
    "revolving": {
        "defaults": {
            "apr_annual": 0.24,
            "is_open": True,
            "is_reported": True,
            "grace_period": 25,
            "min_payment_rule": {"fixed": 25, "pct": 0.02},
            "late_fee": 35,  
        },
        "subtypes": {
            "credit_card": {
                "limit": 2000,
                "balance": 0.0,
            },
            "charge_card": {
                "min_payment_rule": {"fixed": 0, "pct": 1.0}
            },
            "store_card": {
                "apr_annual": 0.29,
                "limit": 1000,
                "balance": 0.0,
            },
            "secured_card": {
                "deposit": 300,
                "limit": 300,
                "balance": 0.0,
            },    
            "personal_line_of_credit": {
                "draw_limit": 5000,
                "balance": 0.0,
            },  
        },
    },      # End revolving credit dict

    "installment": {
        "defaults": {
            "apr_annual": 0.06,
            "is_open": True,
            "is_reported": True,
            "amortization": "fixed",
            "compounding": "monthly",
            "late_fee": float,
        },

        "subtypes": {
            "auto_loan": {
                "original_principle": 15000,
                "term_months": 60,
                "collateral": "vehicle",
            },
            "personal_loan": {
                "original_principle": 5000,
                "term_months": 36,
                "apr_annual": 0.11,
            },
            "student_loan": {
                "original_principle": 12000,
                "term_months": 120,
                "apr_annual": float,
                "deferred_allowed": True,
            },
            "debt_consolidation_loan": {
                "original_principle": 10000,
                "term_months": 48,
            },
            "motorcycle": {
                "original_principle": 8000,
                "term_months": 48,
                "collateral": "vehicle",
            }
        }
    },      # End installment credit dict

    "mortgage": {
        "defaults": {
            "apr_annual": 0.045,
            "is_open": True,
            "is_reported": True,
            "term_months": 360,
            "amortization": "fixed",
            "escrow": True,
        },

        "subtypes": {
            "first_mortgage": {
                "original_principle": 250000,
            },
            "second_mortgage": {
                "original_principle": 30000,
                "term_months": 180,
                "apr_annual": 0.06,
            },
            "home_equity_loan": {
                "original_principle": 40000,
                "term_months": 120,
            },
            "construction_loan": {
                "term_months": 12,
                "interest_only": True,
            }
        }
    },      # End mortgage credit dict

    "retail": {
        "defaults": {
            "apr_annual": 0.28,
            "is_open": True,
            "is_reported": True,
        },

        "subtypes": {
            "department_store_card": {
                "min_payment_rule": {"fixed": 20, "pct": 0.04},
                "limit": 1000,
                "balance": 0.0,
            },
            "electronics_financing": {
                "promo_no_interest_months": 12,
                "deferred_interest": True,
                "original_principle": 1500,
                "term_months": 24,
            }
        }
    },      # End retail credit dict

    "other": {
        "defaults": {
            "apr_annual": 0.1,
            "is_open": True,
            "is_reported": True,
        }
    },      # End other credit dict
}       