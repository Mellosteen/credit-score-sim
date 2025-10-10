from src.core.factory import create_account
from src.core.profile import Profile
from src.scoring import Factors, score

def main():
    prof = Profile()
    # Add a couple of accounts
    cc = create_account("credit_card", id="cc1", limit=2000, balance=350)
    store = create_account("store_card", id="store1", limit=1000, balance=100)
    auto = create_account("auto_loan", id="auto1", original_principal=15000, balance=14200)

    prof.add_account(cc)
    prof.add_account(store)
    prof.add_account(auto)

    print("Accounts:")
    for a in prof.list_accounts():
        print(a)

    print("\nTotals:", prof.totals())

    # Build a mix map from current accounts for Factors.mix_scoring
    mix_map = {a["subtype"]: True for a in prof.list_accounts()}
    mix = Factors.mix_scoring(mix_map)

    f = Factors(
        on_time_payment_rate=0.98,
        utilization=prof.totals()["revolving_utilization_pct"] / 100.0,
        avg_account_age_months=55,
        recent_inquiries=2,
        mix_score=mix,
    )
    s = score(f)
    print(f"\nToy score from current state: {s:.1f}")

if __name__ == "__main__":
    main()