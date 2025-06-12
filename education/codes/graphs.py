import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

data_path = "C:/Users/User/OneDrive/Desktop/Project AI/data/education_data.xlsx"
df = pd.read_excel(data_path)
output_dir = "C:/Users/User/OneDrive/Desktop/Project AI/education/plots"
os.makedirs(output_dir, exist_ok=True)

# Histogram
attitudes = [
    "QB6_3 Total 'Agree'", "QB6_4 Total 'Agree'",
    "QB8_5 Total 'Positively'", "QB11_3 Total 'Important'"
]
for var in attitudes:
    cleaned_name = var.replace(" ", "_").replace("'", "")
    plt.figure(figsize=(10, 6))
    sns.histplot(df[var], kde=True, bins=20)
    plt.title(f"Distribution of {var}")
    plt.xlabel(var)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f"hist_{cleaned_name}.png"))
    plt.close()
