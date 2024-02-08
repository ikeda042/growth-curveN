import data
import matplotlib.pyplot as plt
from typing import cast
import seaborn as sns
import numpy as np
from numpy.linalg import inv


sns.set()
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111)
max_mc1 = max(data.mc1)
mc1 = np.array([max_mc1 - i for i in data.mc1])
ax.scatter(np.array(data.days), mc1, label="Micro-colony1")
# ax.scatter(np.array(data.days), np.array(data.mc2), label="Micro-colony2")
# ax.scatter(np.array(data.days), np.array(data.mc3), label="Micro-colony3")
# ax.scatter(np.array(data.days), np.array(data.Planktonic1), label="Planktonic1")
# ax.scatter(np.array(data.days), np.array(data.Planktonic2), label="Planktonic2")
# ax.scatter(np.array(data.days), np.array(data.Planktonic3), label="Planktonic3")
ax.set_xlabel("Days")
ax.set_ylabel("Nitrate Concentration (mg-N/L)")
ax.legend()
fig.savefig("scatter_mc.png", dpi=400)


def r2_score(y, y_pred):
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r2 = 1 - (ss_res / ss_tot)
    return r2


def fit(
    days_raw: list[int],
    ncs: np.ndarray,
    start_index: int = 14,
    end_index: int = 20,
):
    s, e = start_index, end_index
    days = [days_raw[i] for i in range(s, e)]
    nc_conc = [max(ncs) - ncs[i] for i in range(s, e)]
    f = np.array([np.log(i) for i in nc_conc]).T
    W = np.array([[i, 1] for i in days])
    W_t = W.T
    theta = inv(W_t @ W) @ W_t @ f
    fig_i = plt.figure(figsize=(8, 5))
    X = np.linspace(min(days), max(days), 1000)
    Y = [max_mc1 - np.exp(theta[0] * i + theta[1]) for i in X]
    y_pred = [np.exp(theta[0] * i + theta[1]) for i in days]
    r2 = r2_score(np.array(nc_conc), np.array(y_pred))
    plt.plot(X, Y, color="red")
    plt.scatter(days_raw, ncs, s=10)
    plt.savefig(f"mc1.png", dpi=500)
    plt.close(fig_i)
    return X, Y, days_raw, ncs, theta[0], r2


X_mc1, Y_mc1, days_raw_1, ncs_1, t_1, r2_1 = fit(data.days, np.array(data.mc1), 14, 20)

X_mc2, Y_mc2, days_raw_2, ncs_2, t_2, r2_2 = fit(data.days, np.array(data.mc2))

X_mc3, Y_mc3, days_raw_3, ncs_3, t_3, r2_3 = fit(data.days, np.array(data.mc3))


fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111)
ax.plot(X_mc1, Y_mc1, color="red")
ax.plot(X_mc2, Y_mc2, color="red")
ax.plot(X_mc3, Y_mc3, color="red")
ax.scatter(
    np.array(data.days),
    np.array(data.mc1),
    label=f"Micro-colony1 {round(t_1,2)} "
    + r"$(day^{-1})\:\:R^2=$"
    + f"{round(r2_1, 4)}",
)
ax.scatter(
    np.array(data.days),
    np.array(data.mc2),
    label=f"Micro-colony2 {round(t_2,2)} "
    + r"$(day^{-1})\:\:R^2=$"
    + f"{round(r2_2, 4)}",
)
ax.scatter(
    np.array(data.days),
    np.array(data.mc3),
    label=f"Micro-colony3 {round(t_3,2)} "
    + r"$(day^{-1})\:\:R^2=$"
    + f"{round(r2_3, 4)}",
)

ax.set_xlabel("Days")
ax.set_ylabel("Nitrate Concentration (mg-N/L)")
ax.legend()
fig.savefig("fit_mc1.png", dpi=400)
