import pandas as pd
from scipy import stats
import numpy as np

from scipy.stats import norm

chat_id = 42791670 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    b_ml = np.max(x)
    s = np.std(x, ddof=1)
    t = stats.t.ppf((1+p)/2, n-1)
    delta = t * s / np.sqrt(n)
    b_interval = (max(b_ml, b_ml - delta), b_ml + delta)
    return  b_interval
