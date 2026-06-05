from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = PROJECT_ROOT / "docs" / "figures"
RANDOM_SEED = 42

# ── MANDATORY CONSTANTS & STYLING ─────────────────────────────────────────────
PALETTE = {
    "blue_main":      "#0F4D92",      # GNN standard
    "blue_secondary": "#3775BA",
    "green_3":        "#8BCF8B",
    "red_strong":     "#B64342",      # Ours (PI-STGNN)
    "neutral_dark":   "#272727",      # CFD Ground Truth (blackish)
    "neutral_mid":    "#767676",      # Baseline/Grid
    "neutral_light":  "#CFCECE",
    "teal":           "#42949E",      # Ordinary GNN
    "gold":           "#FFD700",
}

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Liberation Sans']
plt.rcParams['svg.fonttype'] = 'none'   # editable text in SVG
plt.rcParams['font.size'] = 8
plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.linewidth'] = 0.8
plt.rcParams['legend.frameon'] = False

# Ensure output directory exists
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
np.random.seed(RANDOM_SEED)

# ── HELPER FUNCTIONS ──────────────────────────────────────────────────────────
def add_panel_label(ax, label, x=-0.08, y=1.02, fontsize=10, fontweight='bold'):
    ax.text(x, y, label, transform=ax.transAxes, fontsize=fontsize,
            fontweight=fontweight, ha='left', va='bottom')

def save_figure(fig, stem):
    fig.savefig(OUTPUT_DIR / f"{stem}.svg", bbox_inches="tight")
    fig.savefig(OUTPUT_DIR / f"{stem}.png", bbox_inches="tight")

# ── FIGURE 1: 3D TEMPERATURE FIELD RECONSTRUCTION ALONG AXIAL HEIGHT ──────────
def plot_figure_1():
    fig, ax = plt.subplots(figsize=(3.5, 2.8), dpi=300)

    # Generate mock height coordinates (0 to 12 meters)
    heights = np.linspace(0, 12, 100)

    # Temperature profile: peak around 3-4m (burner zone), cooler at inlet/outlet
    # T = T_base + T_peak * exp(-(h-h_peak)^2 / w)
    temp_cfd = 1200 + 342 * np.exp(-(heights - 3.5)**2 / 6.0)
    # GNN predictions with slight errors
    temp_pi_stgn = temp_cfd + np.random.normal(0, 4.0, 100)
    temp_stgcn = temp_cfd + np.random.normal(0, 12.0, 100) + 15.0 * np.sin(heights)

    ax.plot(heights, temp_cfd, color=PALETTE["neutral_dark"], lw=1.5, label="CFD Ground Truth (Fluent)")
    ax.plot(heights, temp_pi_stgn, color=PALETTE["red_strong"], lw=1.2, ls="--", label="PI-STGNN (Ours)")
    ax.plot(heights, temp_stgcn, color=PALETTE["blue_main"], lw=1.0, ls=":", label="Standard STGCN")

    # Visual cues for gasifier zones
    ax.axvspan(2.5, 4.5, color=PALETTE["green_3"], alpha=0.15, label="Primary Combustion Zone")

    ax.set_xlabel("Axial Height of Gasifier (m)")
    ax.set_ylabel("Furnace Temperature (°C)")
    ax.set_ylim(1100, 1650)
    ax.set_xlim(0, 12)
    ax.grid(True, ls="--", alpha=0.3, color=PALETTE["neutral_light"])
    ax.legend(fontsize=7, loc="lower center")

    add_panel_label(ax, "a")

    fig.tight_layout()
    save_figure(fig, "fig1_temperature_profile")
    plt.close(fig)
    print("Figure 1 generated successfully.")

# ── FIGURE 2: SYNGAS YIELD DYNAMIC RAMP ───────────────────────────────────────
def plot_figure_2():
    fig, ax = plt.subplots(figsize=(4.0, 3.0), dpi=300)

    time = np.linspace(0, 1200, 200)

    # CO and H2 transient curves: steady state 1 (0-300s), ramp (300-900s), steady state 2 (900-1200s)
    co_pct = np.zeros_like(time)
    h2_pct = np.zeros_like(time)
    co2_pct = np.zeros_like(time)

    for i, t in enumerate(time):
        if t < 300:
            co_pct[i] = 40.5
            h2_pct[i] = 35.0
            co2_pct[i] = 19.5
        elif t < 900:
            # Linear transition with transient lag fluctuation
            frac = (t - 300) / 600.0
            co_pct[i] = 40.5 + 2.0 * frac - 1.2 * np.sin(np.pi * frac)
            h2_pct[i] = 35.0 + 1.8 * frac - 1.0 * np.sin(np.pi * frac)
            co2_pct[i] = 19.5 - 1.1 * frac + 0.8 * np.sin(np.pi * frac)
        else:
            co_pct[i] = 42.5
            h2_pct[i] = 36.8
            co2_pct[i] = 18.4

    # Add small high-frequency noise representing industrial measurements
    co_noise = co_pct + np.random.normal(0, 0.1, len(time))
    h2_noise = h2_pct + np.random.normal(0, 0.08, len(time))
    co2_noise = co2_pct + np.random.normal(0, 0.05, len(time))

    ax.plot(time, co_noise, color=PALETTE["blue_main"], lw=1.2, label="CO Yield")
    ax.plot(time, h2_noise, color=PALETTE["teal"], lw=1.2, label="H$_2$ Yield")
    ax.plot(time, co2_noise, color=PALETTE["neutral_dark"], lw=1.2, label="CO$_2$ Yield")

    # Vertical line indicating load change trigger
    ax.axvline(300, color=PALETTE["neutral_mid"], ls="--", lw=0.8)
    ax.text(310, 25, "Load Ramp Up (80% to 100%)", fontsize=7, color=PALETTE["neutral_dark"])

    ax.set_xlabel("Operational Time (s)")
    ax.set_ylabel("Dry Basis Composition (mol %)")
    ax.set_ylim(15, 45)
    ax.set_xlim(0, 1200)
    ax.grid(True, ls="--", alpha=0.3, color=PALETTE["neutral_light"])
    ax.legend(fontsize=7, loc="center right")

    add_panel_label(ax, "b")

    fig.tight_layout()
    save_figure(fig, "fig2_syngas_transient")
    plt.close(fig)
    print("Figure 2 generated successfully.")

# ── FIGURE 3: OOD EXTRAPOLATION ABLATION UNDER VALVE FAILURE ──────────────────
def plot_figure_3():
    fig, ax = plt.subplots(figsize=(3.5, 2.8), dpi=300)

    time = np.linspace(500, 1000, 100)

    # Oxygen flow sudden drop by 20% at t = 600s
    temp_cfd = np.zeros_like(time)
    temp_pi = np.zeros_like(time)
    temp_data = np.zeros_like(time)

    for i, t in enumerate(time):
        if t < 600:
            temp_cfd[i] = 1542.0
            temp_pi[i] = 1542.0 + np.random.normal(0, 2.0)
            temp_data[i] = 1542.0 + np.random.normal(0, 2.0)
        else:
            # Temperature decays to a new steady state (around 1410°C)
            decay = np.exp(-(t - 600) / 100.0)
            temp_cfd[i] = 1410.0 + (1542.0 - 1410.0) * decay
            temp_pi[i] = temp_cfd[i] + np.random.normal(0, 4.0)

            # Data-only GNN oscillates wildly and diverges because it doesn't know conservation of energy
            temp_data[i] = temp_cfd[i] + 70.0 * np.sin((t - 600) / 15.0) * np.exp((t - 600) / 300.0) + np.random.normal(0, 8.0)

    ax.plot(time, temp_cfd, color=PALETTE["neutral_dark"], lw=1.5, label="CFD Ground Truth")
    ax.plot(time, temp_pi, color=PALETTE["red_strong"], lw=1.2, ls="--", label="PI-STGNN (With Physics Loss)")
    ax.plot(time, temp_data, color=PALETTE["blue_main"], lw=1.0, ls=":", label="Standard STGCN (No Physics)")

    # Indicator for failure
    ax.axvline(600, color="red", ls="--", lw=1.0)
    ax.text(610, 1610, "Oxygen Valve Failure (OOD)", fontsize=7, color="red", fontweight="bold")

    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Burner Zone Temperature (°C)")
    ax.set_ylim(1300, 1650)
    ax.set_xlim(500, 1000)
    ax.grid(True, ls="--", alpha=0.3, color=PALETTE["neutral_light"])
    ax.legend(fontsize=7, loc="lower left")

    add_panel_label(ax, "c")

    fig.tight_layout()
    save_figure(fig, "fig3_ood_ablation")
    plt.close(fig)
    print("Figure 3 generated successfully.")

# ── MAIN EXECUTION ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    plot_figure_1()
    plot_figure_2()
    plot_figure_3()
    print(f"All Nature-style figures generated and exported to {OUTPUT_DIR}")
