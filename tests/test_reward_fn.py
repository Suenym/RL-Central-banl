import numpy as np
from envs.reward import compute_reward


def test_reward_calculation():
    macro_state = {"inflation": 2.0, "output_gap": -1.0, "FSI": 5.0, "dr": 0.25}
    r = compute_reward(macro_state, lambda_=0.5, mu=0.3, nu=0.05)
    assert np.isclose(r, -2.003125)
