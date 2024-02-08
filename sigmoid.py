import numpy as np
from scipy.optimize import curve_fit
import data
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()


def sigmoid_fit(days, mc1):
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

    # ベストフィット範囲のデータ
    x_data_best = days[best_range[0] : best_range[1]]
    y_data_best = mc1[best_range[0] : best_range[1]]
    y_pred_best = sigmoid(x_data_best, *best_params)
    # R2を返す
    x_data_best = np.linspace(min(x_data_best), max(x_data_best), 1000)
    y_pred_best = sigmoid(x_data_best, *best_params)
    return max_r2, best_params, x_data_best, y_data_best, y_pred_best


days = np.array(data.days)
mc1 = np.array(data.mc1)
r2_mc1, best_params_mc1, x_data_best_mc1, y_data_best_mc1, y_pred_best_mc1 = (
    sigmoid_fit(days, mc1)
)

mc2 = np.array(data.mc2)
r2_mc2, best_params_mc2, x_data_best_mc2, y_data_best_mc2, y_pred_best_mc2 = (
    sigmoid_fit(days, mc2)
)

mc3 = np.array(data.mc3)
r2_mc3, best_params_mc3, x_data_best_mc3, y_data_best_mc3, y_pred_best_mc3 = (
    sigmoid_fit(days, mc3)
)

pl1 = np.array(data.Planktonic1)
r2_pl1, best_params_pl1, x_data_best_pl1, y_data_best_pl1, y_pred_best_pl1 = (
    sigmoid_fit(days, pl1)
)

pl2 = np.array(data.Planktonic2)
r2_pl2, best_params_pl2, x_data_best_pl2, y_data_best_pl2, y_pred_best_pl2 = (
    sigmoid_fit(days, pl2)
)

pl3 = np.array(data.Planktonic3)
r2_pl3, best_params_pl3, x_data_best_pl3, y_data_best_pl3, y_pred_best_pl3 = (
    sigmoid_fit(days, pl3)
)


plt.figure(figsize=(10, 6))
# plt.scatter(
#     days,
#     mc1,
#     label="Micro-colony 1 "
#     + r"$R^2=$"
#     + f"{round(r2_mc1, 2)} "
#     + r"$k=$"
#     + f"{round(best_params_mc1[2], 2)}",
# )

# plt.plot(x_data_best_mc1, y_pred_best_mc1, color="red")

# plt.scatter(
#     days,
#     mc2,
#     label="Micro-colony 2 "
#     + r"$R^2=$"
#     + f"{round(r2_mc2, 2)} "
#     + r"$k=$"
#     + f"{round(best_params_mc2[2], 2)}",
# )
# plt.plot(x_data_best_mc2, y_pred_best_mc2, color="red")

# plt.scatter(
#     days,
#     mc3,
#     label="Micro-colony 3 "
#     + r"$R^2=$"
#     + f"{round(r2_mc3, 2)} "
#     + r"$k=$"
#     + f"{round(best_params_mc3[2], 2)}",
# )
# plt.plot(x_data_best_mc3, y_pred_best_mc3, color="red")

plt.scatter(
    days,
    pl1,
    label="Planktonic 1 "
    + r"$R^2=$"
    + f"{round(r2_pl1, 2)} "
    + r"$k=$"
    + f"{round(best_params_pl1[2], 2)}",
)
plt.plot(x_data_best_pl1, y_pred_best_pl1, color="red")

plt.scatter(
    days,
    pl2,
    label="Planktonic 2 "
    + r"$R^2=$"
    + f"{round(r2_pl2, 2)} "
    + r"$k=$"
    + f"{round(best_params_pl2[2], 2)}",
)
plt.plot(x_data_best_pl2, y_pred_best_pl2, color="red")

plt.scatter(
    days,
    pl3,
    label="Planktonic 3 "
    + r"$R^2=$"
    + f"{round(r2_pl3, 2)} "
    + r"$k=$"
    + f"{round(best_params_pl3[2], 2)}",
)
plt.plot(x_data_best_pl3, y_pred_best_pl3, color="red")

plt.xlabel("Days")
plt.ylabel("Nitrate Concentration (mg-N/L)")
plt.legend()
plt.grid(True)
plt.savefig("fit_pl_sig.png", dpi=400)
