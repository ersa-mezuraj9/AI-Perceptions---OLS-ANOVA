from scipy.stats import shapiro
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.diagnostic import linear_reset
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_excel("C:/Users/User/OneDrive/Desktop/AI Project/AI-Perceptions---OLS-ANOVA/data/education_data.xlsx")

edu_cols = ["Bachelor or equivalent", "Master or equivalent", "Doctoral or equivalent"]

# Standardize in order to fix the problem of the multicollinearity after adding polynomial variables
scaler = StandardScaler()
df[edu_cols] = scaler.fit_transform(df[edu_cols])
dep = "QB11_4 Total 'Important'"

formula = (
    f'Q("{dep}") ~ Q("Bachelor or equivalent") + Q("Master or equivalent") + Q("Doctoral or equivalent")'
    f' + I(Q("Bachelor or equivalent")**2) + I(Q("Master or equivalent")**2) + I(Q("Doctoral or equivalent")**2)'
)
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
            exit()
            
    else:
        print("Too many outliers. Model not re-evaluated. Skipping ANOVA.")
        exit()

else:
    print("Residuals are normally distributed.")

# Linearity Test
reset_result = linear_reset(model, power=2, use_f=True)
print(f"Ramsey RESET p-value: {reset_result.pvalue:.4f}")

if reset_result.pvalue < 0.05:
    print("Nonlinearity detected. Skipping ANOVA.")
    exit()
else:
    print("No evidence of nonlinearity.")

# Breusch-Pagan test for heteroskedasticity
exog = model.model.exog
_, bp_pval, _, _ = het_breuschpagan(model.resid, exog)
print(f"Breusch-Pagan p-value: {bp_pval:.4f}")
if bp_pval <= 0.05:
    print("Heteroskedasticity detected. Skipping ANOVA.")
    exit()

print("All assumptions passed. Proceeding with ANOVA.")

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

