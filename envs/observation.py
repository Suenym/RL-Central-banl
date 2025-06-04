import numpy as np

def build_observation(state, lagged_actions=None):
    state = np.asarray(state, dtype=np.float32)
    if state.shape[0] != 17:
        padded = np.zeros(17, dtype=np.float32)
        padded[: min(len(state), 17)] = state[:17]
        return padded
    return state
