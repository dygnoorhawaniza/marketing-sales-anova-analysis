"""
Marketing Promotion Sales — One-Way ANOVA Analysis

This script follows the methodology in the supplied hypothesis-testing exercise:
- load and clean marketing promotion data
- explore Sales by TV and Influencer categories
- fit OLS: Sales ~ C(TV)
- inspect residual assumptions
- run one-way ANOVA
- run Tukey HSD post-hoc comparisons

Expected input:
    data/marketing_sales_data.csv

Required columns:
    TV, Social Media, Radio, Sales, Influencer
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "marketing_sales_data.csv"
FIGURE_DIR = ROOT / "reports" / "figures"
FIGURE_DIR.mkdir(parents=True, exist_ok=True)


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load and clean the marketing dataset."""
    data = pd.read_csv(path)
    data = data.dropna(axis=0)
    return data


def exploratory_plots(data: pd.DataFrame) -> None:
    """Save Sales distributions for TV and Influencer groups."""
    sns.set_theme(style="whitegrid")

    for column, filename, title in [
        ("TV", "sales_by_tv.png", "Sales Distribution by TV Promotion Budget"),
        ("Influencer", "sales_by_influencer.png", "Sales Distribution by Influencer Size"),
    ]:
        plt.figure(figsize=(8, 5))
        sns.boxplot(x=column, y="Sales", data=data)
        plt.title(title)
        plt.tight_layout()
        plt.savefig(FIGURE_DIR / filename, dpi=180)
        plt.close()


def fit_model(data: pd.DataFrame):
    """Fit OLS with TV as a categorical predictor."""
    model = ols("Sales ~ C(TV)", data=data).fit()
    return model


def assumption_plots(model) -> None:
    """Save residual normality and constant-variance diagnostics."""
    residuals = model.resid

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    sns.histplot(residuals, ax=axes[0])
    axes[0].set_xlabel("Residual Value")
    axes[0].set_title("Histogram of Residuals")

    sm.qqplot(residuals, line="s", ax=axes[1])
    axes[1].set_title("Normal Q-Q Plot")
    plt.tight_layout()
    plt.savefig(FIGURE_DIR / "residual_normality.png", dpi=180)
    plt.close()

    plt.figure(figsize=(7, 5))
    ax = sns.scatterplot(x=model.fittedvalues, y=model.resid)
    ax.set_xlabel("Fitted Values")
    ax.set_ylabel("Residuals")
    ax.set_title("Fitted Values vs. Residuals")
    ax.axhline(0)
    plt.tight_layout()
    plt.savefig(FIGURE_DIR / "fitted_vs_residuals.png", dpi=180)
    plt.close()


def run_tests(data: pd.DataFrame, model):
    """Return ANOVA and Tukey HSD results."""
    anova_table = sm.stats.anova_lm(model, typ=2)
    tukey = pairwise_tukeyhsd(endog=data["Sales"], groups=data["TV"])
    return anova_table, tukey


def main() -> None:
    data = load_data()
    exploratory_plots(data)

    model = fit_model(data)
    print(model.summary())

    assumption_plots(model)

    anova_table, tukey = run_tests(data, model)
    print("\nOne-way ANOVA")
    print(anova_table)

    print("\nTukey HSD")
    print(tukey.summary())


if __name__ == "__main__":
    main()
