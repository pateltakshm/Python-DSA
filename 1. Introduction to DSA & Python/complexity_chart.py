import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

n = np.linspace(1, 20, 500)

complexities = [
    ("O(1)",        np.ones_like(n),              "#2ecc71", "-"),
    ("O(log n)",    np.log2(n),                   "#3498db", "-"),
    ("O(n)",        n,                             "#f39c12", "-"),
    ("O(n log n)",  n * np.log2(n),               "#e67e22", "-"),
    ("O(n²)",       n ** 2,                        "#e74c3c", "-"),
    ("O(2ⁿ)",       np.clip(2 ** n, 0, 500),       "#9b59b6", "--"),
    ("O(n!)",       np.clip([1 if x < 2 else min(math.factorial(int(x)), 500) for x in n], 0, 500), "#c0392b", ":"),
]

fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor("#1a1a2e")
ax.set_facecolor("#16213e")

for label, y, color, style in complexities:
    ax.plot(n, y, label=label, color=color, linestyle=style, linewidth=2.5)

ax.set_xlim(1, 20)
ax.set_ylim(0, 500)
ax.set_xlabel("Input Size (n)", fontsize=13, color="white", labelpad=10)
ax.set_ylabel("Time / Operations", fontsize=13, color="white", labelpad=10)
ax.set_title("Big O Complexity Analysis", fontsize=17, color="white", fontweight="bold", pad=15)

ax.tick_params(colors="gray")
ax.spines["bottom"].set_color("#444")
ax.spines["left"].set_color("#444")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{int(x)}"))

ax.grid(color="#2c2c54", linestyle="--", linewidth=0.6, alpha=0.7)

legend = ax.legend(
    loc="upper left",
    fontsize=11,
    framealpha=0.2,
    facecolor="#0f3460",
    edgecolor="#444",
    labelcolor="white",
)

zones = [
    (0, 1,   "#2ecc71", "Excellent"),
    (1, 2,   "#f1c40f", "Good"),
    (2, 3,   "#e67e22", "Fair"),
    (3, 500, "#e74c3c", "Bad / Horrible"),
]
for y0, y1, color, label in zones:
    ax.axhspan(y0, y1 * 15, alpha=0.04, color=color)

plt.tight_layout()
plt.savefig("complexity_chart.png", dpi=150, facecolor=fig.get_facecolor())
plt.show()
print("Chart saved to complexity_chart.png")
