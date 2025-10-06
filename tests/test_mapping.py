from src.scoring import Factors, score

def test_mapping_deduplication():
    credit_types_dupes = {
        "credit_card": True,
        "store_card": True,
    } # Both exist as revolving credit types
    credit_types_diverse = {
        "credit_card": True,
        "store_card": True,
        "auto_loan": True,
    } # Add an installment credit type to check if score increases

    mix_dupes = Factors.mix_scoring(credit_types_dupes)
    mix_diverse = Factors.mix_scoring(credit_types_diverse)

    assert mix_diverse > mix_dupes