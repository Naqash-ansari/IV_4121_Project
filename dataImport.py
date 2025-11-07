import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


BradfordFactor = pd.read_csv(
    './Bradford.txt',
    delim_whitespace=True,
    skiprows=2,
    names=['Year', 'Month', 'MaxTemp', 'MinTemp',
           'SnowDays', 'Rain', 'Sunshine'],
    engine='python',
    on_bad_lines='skip'
)

# step 2
# Replace '---' with NaN values
BradfordFactor.replace('---', np.nan, inplace=True)

# convert numeric columns from string to float
for col in ['MaxTemp', 'MinTemp', 'SnowDays', 'Rain', 'Sunshine']:
    BradfordFactor[col] = pd.to_numeric(BradfordFactor[col], errors='coerce')


# step 3
for col in ['MaxTemp', 'MinTemp', 'SnowDays', 'Rain', 'Sunshine']:
    BradfordFactor[col] = BradfordFactor[col].fillna(
        BradfordFactor[col].median())

# step 4
#  Max and Min Temperature over time
plt.figure(figsize=(12, 6))
plt.plot(BradfordFactor['Year'].astype(
    str) + '-' + BradfordFactor['Month'].astype(str), BradfordFactor['MaxTemp'], label='Max Temp')
plt.plot(BradfordFactor['Year'].astype(
    str) + '-' + BradfordFactor['Month'].astype(str), BradfordFactor['MinTemp'], label='Min Temp')
plt.xlabel('Time (Year-Month)')
plt.ylabel('Temperature (°C)')
plt.title('Max and Min Temperature Over Time')
plt.legend()
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Max and Min Rainfall and Sunshine Trends
plt.figure(figsize=(12, 6))
plt.plot(BradfordFactor['Rain'], label='Rain (mm)')
plt.plot(BradfordFactor['Sunshine'], label='Sunshine (hours)')
plt.xlabel('Months (Index)')
plt.ylabel('Rain / Sunshine')
plt.title('Rainfall and Sunshine Trends')
plt.legend()
plt.show()

# Step 5: Basic Statistics / Insights
# Yearly Average Temperature:
BradfordFactor['avgTemp'] = (BradfordFactor[
    'MaxTemp'] + BradfordFactor['MinTemp']) / 2

yearly_avg_temp = BradfordFactor.groupby('Year')['avgTemp'].mean()

# print(yearly_avg_temp)

# Rainfall / Sunshine Trends per Year:
yearly_rain = BradfordFactor.groupby('Year')['Rain'].mean()
# print(yearly_rain)

yearly_sunshine = BradfordFactor.groupby('Year')['Sunshine'].mean()
# print(yearly_sunshine)

plt.figure(figsize=(12, 6))
plt.plot(yearly_avg_temp, label='Yearly Avg Temp')
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.title('Yearly Average Temperature')
plt.legend()
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(yearly_rain, label='Yearly Rainfall (mm)')
plt.plot(yearly_sunshine, label='Yearly Sunshine (hours)')
plt.xlabel('Year')
plt.ylabel('Rain / Sunshine')
plt.title('Yearly Rainfall and Sunshine')
plt.legend()
plt.show()

# Step 6: Data Analysis / Trends
monthly_avg = BradfordFactor.groupby('Month')[['MaxTemp', 'MinTemp']].mean()
# print(monthly_avg)

yearly_sum = BradfordFactor.groupby('Year')[['Rain', 'Sunshine']].sum()
# print(yearly_sum)

monthly_avg.to_csv('MonthlyAvgTemp.csv')
yearly_sum.to_csv('YearlyRainSunshine.csv')


# print(BradfordFactor.info())
# print(BradfordFactor.describe())
# print(BradfordFactor.head(10))
