import seaborn as sns
import pandas as pd

salary = pd.read_csv("e:\salary_table.csv")
sns.boxplot(x="education",y="salary",
            hue="management",
            data=salary,palette="PRGn")