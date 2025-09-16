import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('salary_data.csv')

pivot_table = df.pivot(index='Country', columns='Profession', values='Average Salary')
print("میانگین حقوق هر حرفه در هر کشور:")
print(pivot_table)

pivot_table.plot(kind='bar', figsize=(12, 6))
plt.title('مقایسه میانگین حقوق در کشورهای مختلف برای هر حرفه')
plt.ylabel('میانگین حقوق (دلار)')
plt.xlabel('کشور')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('salary_comparison.png')
plt.show()

max_salary = df.loc[df['Average Salary'].idxmax()]
min_salary = df.loc[df['Average Salary'].idxmin()]

print(f"\nبالاترین حقوق: {max_salary['Profession']} در {max_salary['Country']} با حقوق {max_salary['Average Salary']}")
print(f"پایین‌ترین حقوق: {min_salary['Profession']} در {min_salary['Country']} با حقوق {min_salary['Average Salary']}")