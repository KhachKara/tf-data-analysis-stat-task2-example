import pandas as pd
import numpy as np
from scipy.stats import chi2
from scipy.stats import norm

chat_id = 42791670 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    df = n - 1
    var = np.var(x, ddof=1)
    lower_crit = chi2.ppf(alpha / 2, df)
    upper_crit = chi2.ppf(1 - alpha / 2, df)
    var1 = df * var / upper_crit
    var2 = df * var / lower_crit
    b1 = (var1 * 12)**0.5 + 0.095
    b2 = (var2 * 12)**0.5 + 0.095
    return b1, b2
