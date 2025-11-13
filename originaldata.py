# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# # Load data
# BradfordFactor = pd.read_csv(
#     './Bradford.txt',
#     delim_whitespace=True,
#     skiprows=2,
#     names=['Year', 'Month', 'MaxTemp', 'MinTemp',
#            'SnowDays', 'Rain', 'Sunshine'],
#     engine='python',
#     on_bad_lines='skip'
# )

# # Clean numeric columns
# for col in ['MaxTemp', 'MinTemp']:
#     BradfordFactor[col] = pd.to_numeric(BradfordFactor[col], errors='coerce')
#     BradfordFactor[col] = BradfordFactor[col].fillna(
#         BradfordFactor[col].median())

# # Filter only first year
# data_1908 = BradfordFactor[BradfordFactor['Year'] == 1908]

# # Plot
# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
#           'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][:len(data_1908)]
# x = np.arange(len(months))
# width = 0.35

# fig, ax = plt.subplots(figsize=(12, 5))
# ax.bar(x - width/2, data_1908['MaxTemp'],
#        width, label='Max Temp', color='orange')
# ax.bar(x + width/2, data_1908['MinTemp'],
#        width, label='Min Temp', color='skyblue')

# # Add data labels
# for i in range(len(data_1908)):
#     ax.text(i - width/2, data_1908['MaxTemp'].iloc[i] + 0.2,
#             f"{data_1908['MaxTemp'].iloc[i]:.1f}", ha='center', fontsize=8)
#     ax.text(i + width/2, data_1908['MinTemp'].iloc[i] + 0.2,
#             f"{data_1908['MinTemp'].iloc[i]:.1f}", ha='center', fontsize=8)

# # Labels, title, legend
# ax.set_xticks(x)
# ax.set_xticklabels(months)
# ax.set_xlabel('Month')
# ax.set_ylabel('Temperature (°C)')
# ax.set_title('Monthly Max and Min Temperatures in Bradford (1908)')
# ax.legend()
# ax.grid(axis='y', alpha=0.3)

# plt.tight_layout()
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# # Load data
# BradfordFactor = pd.read_csv(
#     './Bradford.txt',
#     delim_whitespace=True,
#     skiprows=2,
#     names=['Year', 'Month', 'MaxTemp', 'MinTemp',
#            'SnowDays', 'Rain', 'Sunshine'],
#     engine='python',
#     on_bad_lines='skip'
# )

# # Clean numeric columns
# for col in ['MaxTemp', 'Sunshine']:
#     BradfordFactor[col] = pd.to_numeric(BradfordFactor[col], errors='coerce')
#     BradfordFactor[col] = BradfordFactor[col].fillna(
#         BradfordFactor[col].median())

# # Scatter plot
# plt.figure(figsize=(10, 6))
# plt.scatter(BradfordFactor['Sunshine'],
#             BradfordFactor['MaxTemp'], color='orange', edgecolor='black')

# # Add trend line
# z = np.polyfit(BradfordFactor['Sunshine'], BradfordFactor['MaxTemp'], 1)
# p = np.poly1d(z)
# plt.plot(BradfordFactor['Sunshine'], p(
#     BradfordFactor['Sunshine']), "r--", label="Trend Line")

# # Labels and title
# plt.xlabel('Sunshine Hours')
# plt.ylabel('Maximum Temperature (°C)')
# plt.title(
#     'Relationship between Max Temperature and Sunshine Hours in Bradford (1908–1909)')
# plt.grid(alpha=0.3)
# plt.legend()
# plt.tight_layout()
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# # Load data
# BradfordFactor = pd.read_csv(
#     './Bradford.txt',
#     delim_whitespace=True,
#     skiprows=2,
#     names=['Year', 'Month', 'MaxTemp', 'MinTemp',
#            'SnowDays', 'Rain', 'Sunshine'],
#     engine='python',
#     on_bad_lines='skip'
# )

# # Clean numeric columns
# for col in ['MaxTemp', 'Sunshine']:
#     BradfordFactor[col] = pd.to_numeric(BradfordFactor[col], errors='coerce')
#     BradfordFactor[col] = BradfordFactor[col].fillna(
#         BradfordFactor[col].median())

# # Filter only first year
# data_1908 = BradfordFactor[BradfordFactor['Year'] == 1908]

# # Plot
# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
#           'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][:len(data_1908)]
# x = np.arange(len(months))
# width = 0.35

# fig, ax = plt.subplots(figsize=(12, 5))
# ax.bar(x - width/2, data_1908['MaxTemp'],
#        width, label='Max Temp (°C)', color='orange')
# ax.bar(x + width/2, data_1908['Sunshine'],
#        width, label='Sunshine Hours', color='skyblue')

# # Add data labels
# for i in range(len(data_1908)):
#     ax.text(i - width/2, data_1908['MaxTemp'].iloc[i] + 0.2,
#             f"{data_1908['MaxTemp'].iloc[i]:.1f}", ha='center', fontsize=8)
#     ax.text(i + width/2, data_1908['Sunshine'].iloc[i] + 1,
#             f"{data_1908['Sunshine'].iloc[i]:.0f}", ha='center', fontsize=8)

# # Labels, title, legend
# ax.set_xticks(x)
# ax.set_xticklabels(months)
# ax.set_xlabel('Month')
# ax.set_ylabel('Value')
# ax.set_title('Monthly Max Temperature and Sunshine Hours in Bradford (1908)')
# ax.legend()
# ax.grid(axis='y', alpha=0.3)

# plt.tight_layout()
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# # Load data
# BradfordFactor = pd.read_csv(
#     './Bradford.txt',
#     delim_whitespace=True,
#     skiprows=2,
#     names=['Year', 'Month', 'MaxTemp', 'MinTemp',
#            'SnowDays', 'Rain', 'Sunshine'],
#     engine='python',
#     on_bad_lines='skip'
# )

# # Clean numeric columns
# for col in ['MaxTemp', 'MinTemp', 'Sunshine']:
#     BradfordFactor[col] = pd.to_numeric(BradfordFactor[col], errors='coerce')
#     BradfordFactor[col] = BradfordFactor[col].fillna(
#         BradfordFactor[col].median())

# # Filter first year for simplicity (1908)
# data_1908 = BradfordFactor[BradfordFactor['Year'] == 1908]

# # Month labels
# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
#           'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][:len(data_1908)]

# # Plot
# plt.figure(figsize=(12, 5))
# plt.plot(months, data_1908['MaxTemp'], marker='o',
#          color='orange', label='Max Temp (°C)')
# plt.plot(months, data_1908['MinTemp'], marker='o',
#          color='skyblue', label='Min Temp (°C)')
# plt.fill_between(months, data_1908['MinTemp'],
#                  data_1908['MaxTemp'], color='orange', alpha=0.1)

# # Labels, title, legend
# plt.xlabel('Month')
# plt.ylabel('Temperature (°C)')
# plt.title('Average Monthly Maximum and Minimum Temperatures in Bradford (1908)')
# plt.grid(axis='y', alpha=0.3)
# plt.legend()
# plt.tight_layout()
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# # Load data
# BradfordFactor = pd.read_csv(
#     './Bradford.txt',
#     delim_whitespace=True,
#     skiprows=2,
#     names=['Year', 'Month', 'MaxTemp', 'MinTemp',
#            'SnowDays', 'Rain', 'Sunshine'],
#     engine='python',
#     on_bad_lines='skip'
# )

# # Clean numeric columns
# BradfordFactor['Rain'] = pd.to_numeric(BradfordFactor['Rain'], errors='coerce')
# BradfordFactor['Rain'] = BradfordFactor['Rain'].fillna(
#     BradfordFactor['Rain'].median())

# # Filter only first year
# data_1908 = BradfordFactor[BradfordFactor['Year'] == 1908]

# # Month labels
# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
#           'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][:len(data_1908)]
# x = np.arange(len(months))
# width = 0.6

# # Plot
# fig, ax = plt.subplots(figsize=(12, 5))
# bars = ax.bar(x, data_1908['Rain'], width, color='skyblue', edgecolor='black')

# # Add data labels
# for i in range(len(data_1908)):
#     ax.text(i, data_1908['Rain'].iloc[i] + 1,
#             f"{data_1908['Rain'].iloc[i]:.1f}", ha='center', fontsize=8)

# # Labels, title, legend
# ax.set_xticks(x)
# ax.set_xticklabels(months)
# ax.set_xlabel('Month')
# ax.set_ylabel('Rainfall (mm)')
# ax.set_title(
#     'Monthly Rainfall in Bradford (1908) – Missing values replaced by median')
# ax.grid(axis='y', alpha=0.3)

# plt.tight_layout()
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
BradfordFactor = pd.read_csv(
    './Bradford.txt',
    delim_whitespace=True,
    skiprows=2,
    names=['Year', 'Month', 'MaxTemp', 'MinTemp',
           'SnowDays', 'Rain', 'Sunshine'],
    engine='python',
    on_bad_lines='skip'
)

# Clean numeric columns
for col in ['MaxTemp', 'Sunshine']:
    BradfordFactor[col] = pd.to_numeric(BradfordFactor[col], errors='coerce')
    BradfordFactor[col] = BradfordFactor[col].fillna(
        BradfordFactor[col].median())

# Filter only 1908 for consistency
data_1908 = BradfordFactor[BradfordFactor['Year'] == 1908]

# Scatter plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(data_1908['MaxTemp'], data_1908['Sunshine'],
           color='orange', edgecolor='black', s=100)

# Add data labels
for i in range(len(data_1908)):
    ax.text(data_1908['MaxTemp'].iloc[i]+0.1, data_1908['Sunshine'].iloc[i]+1,
            f"{data_1908['Sunshine'].iloc[i]:.1f}", fontsize=8)

# Labels, title
ax.set_xlabel('Maximum Temperature (°C)')
ax.set_ylabel('Sunshine Hours')
ax.set_title(
    'Correlation between Maximum Temperature and Sunshine Hours (Bradford, 1908)')
ax.grid(alpha=0.3)

plt.tight_layout()
plt.show()
