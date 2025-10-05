# Credit Score Simulator (v0)

Tiny starter that computes a toy "credit score" from:
- on-time payment rate (0..1)
- utilization (0..1)

## Quickstart

```bash
conda create -n credit-score-sim python=3.11 -y
conda activate credit-score-sim
pip install pytest
pytest -q
python main.py