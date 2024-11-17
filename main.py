import pandas as pd
import matplotlib.pyplot as plt

# Load dataset on bank
df = pd.read_csv('BankChurners.csv')

# Calculate arrival rate (λ) based on inactivity: 1 inactive month = 1 arrival
df['arrival_rate'] = 1 / (df['Months_Inactive_12_mon'] + 1)

# Assign service rate (μ) based on card category
service_rates = {'Platinum': 12, 'Gold': 10, 'Silver': 8,  'Blue': 5}
df['service_rate'] = df['Card_Category'].map(service_rates)

# Queuing discipline: Adjust service rates for customers with dependent_count
priority_weight = 1.2
df['adjusted_service_rate'] = df['service_rate'] * (1 + (df['Dependent_count'] / priority_weight))

# Calculate traffic intensity (ρ), L (avg customers in system), W (avg wait time)
df['traffic_intensity'] = df['arrival_rate'] / df['adjusted_service_rate']
df['avg_customers_system'] = df['traffic_intensity'] / (1 - df['traffic_intensity'])
df['avg_wait_time'] = 1 / (df['adjusted_service_rate'] - df['arrival_rate'])

# Filter results for relevant columns and check for any NaN or invalid values
result = df[['CLIENTNUM', 'traffic_intensity', 'avg_customers_system', 'avg_wait_time']]
print(result.dropna())  # Drop any rows with invalid calculations

# Visualize results
plt.bar(df['CLIENTNUM'], ['avg_wait_time'])
plt.xlabel('Client Number')
plt.ylabel('Average Wait Time (hrs)')
plt.title('Wait Time by Client')
plt.show()
