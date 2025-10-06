from src.scoring import Factors, score

credit_types = {
    "auto_loan": True,
    "credit_card": True,
    "first_mortgage": False,
    "store_card": True,
}

def main():
    # Example profile: 98% on-time payments, 20% utilization
    mix = Factors.mix_scoring(credit_types)
    f = Factors(
        on_time_payment_rate = 0.98, 
        utilization = 0.20,
        avg_account_age_months = 55,
        recent_inquiries = 2,
        mix_score = mix
    )
    s = score(f)
    print(f"Simulated credit score: {s:.1f}")   # Should return 744.2 with current inputs.


# This line ensures that whatever is run within it is not run if this file 
# is imported by another such that __name__ is only set to 'main'.
if __name__ == "__main__":
    main()