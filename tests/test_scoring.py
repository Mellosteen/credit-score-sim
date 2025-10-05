from src.scoring import Factors, score

def test_basic_ranges():
    # Perfect payments + 0% util => should be high
    f1 = Factors(1.0, 0.0)
    s1 = score(f1)
    assert s1 > 800

    # Bad payments + 100% util => should be low-ish
    f2 = Factors(0.5, 1.0)
    s2 = score(f2)
    assert s2 < 650

def test_monotonicity():
    # Better utilization should help
    f_low = Factors(0.9, 0.8)
    f_high = Factors(0.9, 0.2)
    assert score(f_high) > score(f_low)