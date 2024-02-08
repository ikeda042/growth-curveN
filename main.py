import data
import matplotlib.pyplot as plt
from typing import cast
import seaborn as sns
import numpy as np

sns.set()
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111)
ax.scatter(np.array(data.days), np.array(data.mc1), label="Micro-colony1")
ax.scatter(np.array(data.days), np.array(data.mc2), label="Micro-colony2")
ax.scatter(np.array(data.days), np.array(data.mc3), label="Micro-colony3")
ax.scatter(np.array(data.days), np.array(data.Planktonic1), label="Planktonic1")
ax.scatter(np.array(data.days), np.array(data.Planktonic2), label="Planktonic2")
ax.scatter(np.array(data.days), np.array(data.Planktonic3), label="Planktonic3")
ax.set_xlabel("Days")
ax.set_ylabel("Nitrate Concentration (mg-N/L)")
ax.legend()
fig.savefig("scatter_all.png", dpi=400)


fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111)
ax.scatter(np.array(data.days), np.log(np.array(data.mc1)), label="Micro-colony1")
ax.scatter(np.array(data.days), np.log(np.array(data.mc2)), label="Micro-colony2")
ax.scatter(np.array(data.days), np.log(np.array(data.mc3)), label="Micro-colony3")
ax.scatter(np.array(data.days), np.log(np.array(data.Planktonic1)), label="Planktonic1")
ax.scatter(np.array(data.days), np.log(np.array(data.Planktonic2)), label="Planktonic2")
ax.scatter(np.array(data.days), np.log(np.array(data.Planktonic3)), label="Planktonic3")
ax.set_xlabel("Days")
ax.set_ylabel("Log of Nitrate Concentration (mg-N/L)")
ax.legend()
fig.savefig("scatter_log.png", dpi=200)
