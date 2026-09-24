# Marketing Sales Hypothesis Testing with Python

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Statistics](https://img.shields.io/badge/Statistics-ANOVA%20%7C%20Tukey%20HSD-purple)
![Status](https://img.shields.io/badge/Project-Portfolio%20Ready-success)

A portfolio-ready statistical analysis of historical marketing promotion data, using **Python, OLS regression, one-way ANOVA, and Tukey's HSD** to investigate whether sales differ across TV promotion-budget categories.

> **Project type:** Data Analytics / Statistical Inference  
> **Primary question:** Are differences in sales across TV promotion-budget groups statistically significant?

## Executive Summary

This project applies a complete hypothesis-testing workflow to marketing promotion data:

1. Explore the distribution of `Sales` across categorical promotion groups.
2. Clean missing observations.
3. Fit an OLS regression using `TV` as a categorical predictor.
4. Inspect model assumptions through residual diagnostics.
5. Perform a one-way ANOVA.
6. Use Tukey's HSD to identify which pairs of TV groups differ.
7. Translate statistical results into stakeholder-friendly business language.

The supplied exercise reports a strong relationship between TV promotion category and Sales. Its documented ANOVA result is **F = 1971.46, p = 8.81 × 10⁻²⁵⁶**, and the reported Tukey HSD results show significant differences for all three TV-category pairs.

## Business Problem

Marketing stakeholders want to understand whether sales differ meaningfully across different levels of TV promotion investment.

The analysis compares three TV promotion categories:

- **High**
- **Medium**
- **Low**

The goal is not simply to compare averages visually, but to determine whether the observed differences are statistically significant and which specific groups differ.

## Analytical Approach

```text
Marketing data
     │
     ▼
Exploratory analysis
     │
     ├── Sales vs TV boxplot
     └── Sales vs Influencer boxplot
     │
     ▼
Data cleaning
     │
     └── Remove missing rows
     │
     ▼
OLS: Sales ~ C(TV)
     │
     ├── R² / coefficients
     └── residual diagnostics
     │
     ▼
One-way ANOVA
     │
     └── Test whether any TV group means differ
     │
     ▼
Tukey HSD
     │
     └── Identify significant pairwise differences
     │
     ▼
Stakeholder interpretation
```

![Analysis workflow](reports/figures/analysis_workflow.png)

## Key Findings Reported in the Supplied Analysis

### Regression

The supplied analysis reports:

- `TV` was selected as the categorical predictor because exploratory analysis showed a strong relationship with `Sales`.
- The documented regression result reports **R² = 0.874** in one section and **R² = 0.871** in the final summary.
- The model uses `High` TV promotion as the reference category.
- The documented coefficient interpretation indicates that Low and Medium TV categories have lower average Sales than High.

The discrepancy between the two reported R² values is retained here rather than silently "corrected"; rerunning the analysis against the dataset should be used to establish the exact reproducible value.

### One-Way ANOVA

**Null hypothesis (H₀):** Mean Sales does not differ by TV promotion category.

**Alternative hypothesis (H₁):** At least one TV promotion category has a different mean Sales.

The supplied analysis reports:

- **F-statistic:** 1971.46
- **p-value:** 8.81 × 10⁻²⁵⁶

Because the reported p-value is below 0.05, the exercise concludes that there is a statistically significant difference in Sales among TV groups.

### Tukey HSD

The supplied analysis reports statistically significant differences for every pair:

| Comparison | Estimated mean difference | Reported 95% CI |
|---|---:|---:|
| High vs Low | $208.81M | $200.99M – $216.64M |
| High vs Medium | $101.51M | $93.69M – $109.32M |
| Medium vs Low | $107.31M | $99.71M – $114.91M |

![Tukey HSD differences](reports/figures/tukey_mean_differences.png)

## Model Diagnostics

The original analysis checks:

- **Independence:** each marketing promotion is treated as an independent observation.
- **Linearity:** because the predictor is categorical, the source notes that the usual continuous-predictor linearity requirement is not applicable in the same way.
- **Normality:** residual histogram and Q-Q plot are inspected. The supplied exercise notes some concern about the Q-Q pattern but proceeds with the lab assumption.
- **Constant variance:** fitted values versus residuals are inspected; the supplied exercise reports that the variance appears similarly distributed.

These diagnostics matter because statistical significance should be interpreted alongside the assumptions supporting the model.

## Project Structure

```text
marketing-sales-anova-analysis/
├── data/
│   └── README.md
├── notebooks/
│   └── hypothesis_testing_with_python.py
├── reports/
│   └── figures/
│       ├── analysis_workflow.png
│       └── tukey_mean_differences.png
├── src/
│   └── anova_analysis.py
├── .github/
│   └── workflows/
│       └── python-check.yml
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/marketing-sales-anova-analysis.git
cd marketing-sales-anova-analysis
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows**
```bash
.venv\Scripts\activate
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add the dataset

Place `marketing_sales_data.csv` inside the `data/` directory.

The expected fields are:

```text
TV
Social Media
Radio
Sales
Influencer
```

### 5. Run the analysis

```bash
python src/anova_analysis.py
```

The script prints the regression summary, ANOVA table, and Tukey HSD results and saves diagnostic figures under `reports/figures/`.

## Tools & Technologies

| Tool | Purpose |
|---|---|
| Python | Analysis and automation |
| Pandas | Data loading and cleaning |
| Seaborn | Exploratory visualisation |
| Matplotlib | Statistical plots |
| Statsmodels | OLS, ANOVA and Tukey HSD |
| Jupyter / Python | Reproducible analysis workflow |

## Skills Demonstrated

- Exploratory Data Analysis
- Data Cleaning
- Categorical-variable modelling
- Ordinary Least Squares (OLS)
- Model diagnostics
- Hypothesis testing
- One-way ANOVA
- Post-hoc testing
- Tukey's HSD
- Statistical interpretation
- Business/stakeholder communication
- Reproducible Python analysis

## Business Interpretation

The statistical workflow provides more information than a simple comparison of group averages.

ANOVA answers:

> **Is there evidence that at least one group mean differs?**

Tukey's HSD then answers:

> **Which specific group pairs differ after accounting for multiple comparisons?**

According to the supplied analysis, the three TV promotion categories differ significantly from one another, with the reported mean-sales differences increasing from Low → Medium → High.

This supports the analytical conclusion that TV promotion category is strongly associated with Sales in the dataset. It should not, by itself, be interpreted as proof of causal impact because the analysis is observational and does not establish that changing TV spend alone caused the observed sales differences.

## Potential Improvements

The supplied analysis identifies several ways the model could be developed further:

- Use actual TV promotion budgets instead of broad categories.
- Add campaign location.
- Add seasonality or time-of-year information.
- Include other marketing variables.
- Compare alternative model specifications.
- Re-run diagnostics on the exact dataset used for deployment.
- Separate statistical significance from practical/business significance.

## Data Source

The supplied exercise references:

**Saragih, H.S. — Dummy Marketing and Sales Data** on Kaggle.

The dataset is not redistributed in this repository. See `data/README.md` for the expected schema.

## Portfolio Note

This repository is structured to demonstrate an end-to-end statistical analysis rather than simply storing a course notebook. The original exercise is preserved in `notebooks/`, while `src/anova_analysis.py` provides a cleaner reusable analysis pipeline.

