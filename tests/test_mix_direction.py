from src.scoring import Factors, score

# Test monotonicity for mix
def test_mix_increases_score():
    base = Factors(0.98, 0.20, 55, 2, 0.50)       # mix score 0.50
    higher_mix = Factors(0.98, 0.20, 55, 2, 0.70) 
    assert score(higher_mix) > score(base) 

# Test monotonicity for inquiries
def test_inquiries_decrease_score():
    few = Factors(0.98, 0.20, 55, 0, 0.50)  # 0 inquiries
    many = Factors(0.98, 0.20, 55, 5, 0.50) # 5 inquiries
    assert score(few) > score(many)