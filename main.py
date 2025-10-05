from src.scoring import Factors, score

def main():
    # Example profile: 98% on-time payments, 20% utilization
    f = Factors(on_time_payment_rate=0.98, utilization=0.20)
    s = score(f)
    print(f"Simulated credit score: {s:.1f}")

if __name__ == "__main__":
    main()