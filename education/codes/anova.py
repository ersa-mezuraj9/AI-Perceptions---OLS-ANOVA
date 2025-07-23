"""
Null Hypothesis (H₀) p-value ≥ 0.05:
All questions have the same mean positive response.

Alternative Hypothesis (H₁) p-value < 0.05 :
At least one question has a mean positive response that is significantly different from the others.
"""

import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("C:/Users/User/OneDrive/Desktop/AI Project/AI-Perceptions---OLS-ANOVA/data/education_data.xlsx")

edu_cols = ["Bachelor or equivalent", "Master or equivalent", "Doctoral or equivalent"]
df_questions = df.drop(columns=edu_cols)

df_long = df_questions.melt(var_name="Question", value_name="Response")
print(df_long.head)

model = ols('Response ~ C(Question)', data=df_long).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

print("=== One-Way ANOVA Across Questions ===")
print(anova_table)

plt.figure(figsize=(14, 6))
sns.boxplot(x="Question", y="Response", data=df_long)
plt.xticks(rotation=45, ha="right")
plt.title("Distribution of Responses by Question")
plt.tight_layout()
plt.show()
