import numpy as np


def normalize(x):
    arr = np.asarray(x, dtype=np.float32)
    denom = np.linalg.norm(arr)
    return arr / denom if denom != 0 else arr
