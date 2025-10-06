from dataclasses import dataclass
from typing import Mapping
from src.data_loader import load_subtype_map

# Set constant global variables for upper and lower bounds of a credit score
LOW = 300
HIGH = 850
MAIN_TYPE_WEIGHTS = {
            "revolving": 0.2,
            "installment": 0.3,
            "mortgage": 0.3,
            "retail": 0.1,
            "other": 0.1,
        }

@dataclass
class Factors:
    """
    Class that contains all necessary factors for computing the weight to calculate credit score.
    Also contains helper static functions for calculating certain subscores.

    !!! It is intended that the static method mix_scoring is computed in the main.py with a preset 
    credit_type Mapping object inside it!!!
    """
    on_time_payment_rate: float  # 0..1, last 24 months
    utilization: float           # 0..1
    avg_account_age_months: int  # 1..240 months, but only 72 needed for max weight
    recent_inquiries: int        # 0..5, # of hard inquiries only
    mix_score: float             # 0..1, 0 = all one type/1 = healthy mix

    @staticmethod
    def mix_scoring(credit_types: Mapping[str, bool]) -> float:
        """
        Helper function to calculate the mix_score.
        Create two dicts; first one contains the weights of the primary categories as 
        referenced in the Notion under the Extra Notes section, while the second dict will map 
        known subtypes of credit to its corresponding main type. The second dict has been saved in a 
        separate file under data.

        Utilize a helper dict to record found main types of credit in the argument then sum them for 
        the return value.

        !!! Assume all types are spaced with underscores! Letters will be standardized to lower case!!!

        Returns: float value indicating weight.

        Example dict:
        credit_types = {
            "revolving": True,
            "installment": False,
            "mortgage": True,
            "student_loan": True,
        }
        """

        if not credit_types:
            return 0.0
        
        present_main_types: set[str] = set()
        return_score = 0.0
        
        subtype_mapping = load_subtype_map()

        for key, has in credit_types.items():
            # This person does not have this type of credit
            if not has:
                continue

            # Format key to lowercase and remove excess whitespacing
            form_key = str(key).strip().lower()

            # Check if key is already a main type; otherwise, find corresponding main type
            if form_key in MAIN_TYPE_WEIGHTS:
                mapped_type = form_key
            else:
                mapped_type = subtype_mapping.get(form_key, "other")

            # Add main type into set
            present_main_types.add(mapped_type)

        # Add weights if type of credit was found
        for item in present_main_types:
            return_score += MAIN_TYPE_WEIGHTS.get(item, 0.0)

        return return_score

def score(f: Factors) -> float:
    """
    v0: super simple weighted formula:
    - payment history (70%)
    - utilization (30%, best is low utilization)
    Return: Adjusted credit score based on weighted proportion based on factors from Factor-class.
    """

    # Adjust values of on_time_payment_rate and utilization to be within 0 and 1
    pay_sub = max(0.0, min(1.0, f.on_time_payment_rate))

    util = max(0.0, min(1.0, f.utilization))
    util_sub = 1.0 - util  # 0 util -> 1.0 (great); 1.0 util -> 0.0 (bad)

    age_sub = min(f.avg_account_age_months/72.0, 1.0) # Any account older than 6 years gets full weight

    inquiries = min(5.0, max(0.0, f.recent_inquiries)) # Ensure # of inquiries within 0 and 5
    inq_sub = 1.0 - inquiries/5.0

    mix_sub = max(0.0, min(1.0, f.mix_score)) # mix_score computed beforehand through main.py

    # Formula for weighted proportions for credit score scaling. Will add more factors later on...
    raw = 0.35*pay_sub + 0.30*util_sub + 0.15*age_sub + 0.10*inq_sub + 0.10*mix_sub
    
    return LOW + raw * (HIGH - LOW)