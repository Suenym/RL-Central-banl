# MacroFinance LLM-Driven Simulation

This repository contains an RL-based macroeconomic environment plus LLM integration to simulate persona-driven policy decisions.

## Repo Structure
- `envs/` – Gym-compatible macro environment (DSGE core + shocks + reward).
- `baselines/` – DSGE calibration seeds, unit tests for steady-state.
- `configs/` – YAML files for country calibrations & shock definitions.
- `docs/` – Sphinx documentation.
- `src/` – Utilities for data loading and general helpers.
- `notebooks/` – Example Jupyter notebooks.
- `tests/` – Pytest suite.

## Installation

```bash
git clone https://github.com/your-org/macrofinance-llm-sim.git
cd macrofinance-llm-sim
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Quick Smoke Test

1. Install in editable mode:

   ```bash
   pip install -e .
   ```
2. Run a random-policy rollout:

   ```bash
   pytest tests/test_env_smoke.py
   ```

## CI & Docs

- GitHub Actions will run tests on every push.
- To build documentation locally:

  ```bash
  cd docs
  make html
  ```
