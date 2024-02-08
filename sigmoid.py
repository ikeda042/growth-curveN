import numpy as np
from scipy.optimize import curve_fit
import data

days = np.array(data.days)
mc1 = np.array(data.mc1)


def sigmoid(x, L, x0, k, b):
    y = L / (1 + np.exp(-k * (x - x0))) + b
    return y


def r2_score(y, y_pred):
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r2 = 1 - (ss_res / ss_tot)
    return r2


# R2スコアを最大化するグリッドサーチ
max_r2 = -np.inf
best_range = None
best_params = None

for start in range(len(days)):
    for end in range(start + 1, len(days) + 1):
        try:
            # データ範囲の選択
            x_data = days[start:end]
            y_data = mc1[start:end]

            # シグモイド曲線フィット
            popt, _ = curve_fit(sigmoid, x_data, y_data, maxfev=5000)

            # R2スコアの計算
            y_pred = sigmoid(x_data, *popt)
            r2 = r2_score(y_data, y_pred)

            # 最大R2スコアの更新
            if r2 > max_r2:
                max_r2 = r2
                best_range = (start, end)
                best_params = popt
        except:
            continue

print(f"best range: {best_range}")
print(f"best params: {best_params}")
print(f"max R2 score: {max_r2}")
