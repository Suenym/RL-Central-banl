import numpy as np

def compute_reward(macro_state, lambda_, mu, nu):
    pi = macro_state.get("inflation", 0.0)
    target_pi = 2.0
    y_gap = macro_state.get("output_gap", 0.0)
    fsi = macro_state.get("FSI", 0.0)
    dr = macro_state.get("dr", 0.0)
    r = -((pi - target_pi) ** 2 + lambda_ * (y_gap ** 2))
    r -= mu * fsi
    r -= nu * (dr ** 2)
    return float(r)
