# Credit Score Simulator (v1)

Tiny starter that computes a toy "credit score" from:
- on-time payment rate (0..1)
- utilization (0..1)
- average age in months (0..240), but at least 72 for high score
- recent inquiries (0..5)
- credit mix score (0..1)

## Quickstart

```bash
conda create -n credit-score-sim python=3.11 -y
conda activate credit-score-sim
pip install pytest
pytest -q
python main.py