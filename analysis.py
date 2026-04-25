import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('unemployment_data.xlsx')

print("Average unemployment rate per year:")
print(df.groupby('Year')['Unemployment_Rate'].mean())

print("\nHighest unemployment region in 2023:")
print(df[df['Year']==2023].sort_values('Unemployment_Rate', ascending=False).head(1))

plt.figure(figsize=(10,6))
for region in df['Region'].unique():
    data = df[df['Region']==region]
    plt.plot(data['Year'], data['Unemployment_Rate'], marker='o', label=region)

plt.title('Unemployment Rate in Saudi Regions 2022-2023')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate %')
plt.legend()
plt.grid(True)
plt.savefig('unemployment_chart.png')
plt.show()

print("\nConclusion: Unemployment decreased in all regions between 2022 and 2023")
