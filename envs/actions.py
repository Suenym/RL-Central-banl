import numpy as np

ACTION_BOUNDS = [(-5.0, 5.0)] * 5

def decode_action(action_vec):
    a = np.asarray(action_vec, dtype=np.float32)
    clipped = []
    for val, (lo, hi) in zip(a, ACTION_BOUNDS):
        clipped.append(float(np.clip(val, lo, hi)))
    return clipped
