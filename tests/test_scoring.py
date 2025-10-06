from src.scoring import Factors, score

def test_basic_ranges():
    # Perfect stats. Should yield high score.
    f1 = Factors(1.0, 0.0, 72, 0, 1.0)
    s1 = score(f1)
    assert s1 > 800

    # Bad stats. Yield low score.
    f2 = Factors(0.5, 1.0, 10, 3, 0.3)
    s2 = score(f2)
    assert s2 < 650

def test_monotonicity():
    # Better weights yield higher scores
    f_low = Factors(0.9, 0.8, 70, 1, 0.8)
    f_high = Factors(0.9, 0.2, 70, 0, 0.9)
    assert score(f_high) > score(f_low)