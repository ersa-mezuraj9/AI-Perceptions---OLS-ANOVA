"""
# Regression
Null Hypothesis (H₀):
All regression coefficients for educational predictors are zero.
Alternative Hypothesis (H₁):
At least one of the coefficients is different from zero.

# ANOVA table 
Null Hypothesis (H₀):
The coefficient for that predictor is zero.
Alternative Hypothesis (H₁):
The coefficient is not zero.
"""


from scipy.stats import shapiro
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.diagnostic import het_breuschpagan
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("education/plots", exist_ok=True)

df = pd.read_excel("C:/Users/User/OneDrive/Desktop/Project AI/data/education_data.xlsx")
data = df.describe()
data.to_excel("data/describe_table.xlsx", index=False)


edu_cols = ["Bachelor or equivalent", "Master or equivalent", "Doctoral or equivalent"]

# VIF
correlation = df.corr()
correlation.to_excel("data/corr.xlsx", index=False)

X_vif = df[edu_cols]
vif_data = pd.DataFrame({
    "Education": X_vif.columns,
    "VIF": [variance_inflation_factor(X_vif.values, i) for i in range(X_vif.shape[1])]
})
print("=== VIF ===")
print(vif_data)

plt.figure(figsize=(16, 12))

# Heatmap #  Patterns in AI Perceptions Across Educational Demographics in the EU
heatmap = sns.heatmap(
    correlation,
    cmap="coolwarm",       
    annot=False,           
    linewidths=0.5,        
    square=True,           
    cbar_kws={"shrink": .8, "label": "Correlation Coefficient"}
)
plt.title("Correlation Heatmap of Education and AI Perception Variables", fontsize=16)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()


dep_vars = df.drop(columns=edu_cols)
for dep in dep_vars:
    print(f"\n--- {dep} ---")

    formula = f'Q("{dep}") ~ Q("Bachelor or equivalent") + Q("Master or equivalent") + Q("Doctoral or equivalent")'
    model = ols(formula, data=df).fit()
    resid = model.resid

    # Shapiro-Wilk test for normality
    sh_stat, sh_pval = shapiro(resid)
    print(f"Shapiro-Wilk p-value: {sh_pval:.4f}")

    if sh_pval <= 0.05:
        print("Residuals are NOT normally distributed. Checking for outliers...")
        Q1, Q3 = resid.quantile([0.25, 0.75])
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = (resid < lower_bound) | (resid > upper_bound)
        print(f"Number of outliers: {outliers.sum()}")

        plt.figure(figsize=(8, 5))
        sns.boxplot(x=resid)
        plt.title(f"Boxplot of Residuals for {dep}")
        plt.xlabel("Residuals")
        plt.grid(True)
        plt.savefig(f"education/plots/boxplot_resid_{dep.replace('/', '_')}.png")
        plt.close()

        if outliers.sum() < 3:
            cleaned_df = df.loc[~outliers]
            model_clean = ols(formula, data=cleaned_df).fit()
            new_shapiro = shapiro(model_clean.resid)
            print("\nAfter outlier removal:")
            print(f"Shapiro p-value: {new_shapiro.pvalue:.4f}")
            if new_shapiro.pvalue > 0.05:
                model = model_clean
                print("Residuals are now normally distributed after cleaning.")
            else:
                print("Still not normal after removing outliers. Skipping ANOVA.")
                continue
        else:
            print("Too many outliers. Model not re-evaluated. Skipping ANOVA.")
            continue
    else:
        print("Residuals are normally distributed.")

    # Breusch-Pagan test for heteroskedasticity
    exog = model.model.exog
    _, bp_pval, _, _ = het_breuschpagan(model.resid, exog)
    print(f"Breusch-Pagan p-value: {bp_pval:.4f}")
    if bp_pval <= 0.05:
        print("Heteroskedasticity detected. Skipping ANOVA.")
        continue

    print("Both assumptions passed. Proceeding with ANOVA.")

    # ANOVA 
    anova_table = sm.stats.anova_lm(model, typ=2)
    print("\nANOVA Table:")
    print(anova_table)

    significant = anova_table[anova_table['PR(>F)'] < 0.05]
    if not significant.empty:
        print("\nSignificant predictors (p < 0.05):")
        print(significant)
    else:
        print("No significant education predictors.")

    # Model summary
    if model.f_pvalue < 0.05:
        print(f"\nModel is significant (F p = {model.f_pvalue:.4f})")
        print(model.summary())
    else:
        print(f"Model is not significant (F p = {model.f_pvalue:.4f})")
