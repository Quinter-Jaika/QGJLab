#### Banking Queue model

### 1. **Load the Dataset**
**`pd.read_csv('BankChurners.csv')`**
- This command loads the dataset from the CSV file `'BankChurners.csv'` into a pandas DataFrame (`df`).

### 2. **Calculating the Arrival Rate**
**`df['Months_Inactive_12_mon']`**
- This accesses the column `'Months_Inactive_12_mon'` in the DataFrame, which presumably contains data on how many months a customer has been inactive.

**`df['arrival_rate']`**
- This creates a new column, `'arrival_rate'`, in the DataFrame. The calculation `1 / (df['Months_Inactive_12_mon'] + 1)` is used to calculate the arrival rate (λ) for each customer.
- The formula assumes that more months of inactivity result in a lower arrival rate, hence the addition of `1` ensures that customers who were inactive for 0 months still have a positive arrival rate.


### 3. **Assigning Service Rate Based on Card Category**
**`service_rates`**
- This dictionary defines the service rates (`μ`) for different card categories.
- The `Platinum` card has the highest service rate (12), and `Blue` has the lowest (5).

**`df['Card_Category'].map(service_rates)`**
- This maps each customer’s card category to the corresponding service rate by using the `map()` function.
- It looks up the card category in the `service_rates` dictionary and assigns the respective service rate to each row in the `'service_rate'` column of the DataFrame.


### 4. **Adjusting the Service Rate Based on Dependent Count**
**`priority_weight = 1.2`**
- This sets a factor to adjust the service rate based on the number of dependents a customer has.
- A higher number of dependents will result in a higher service priority, which is factored into the service rate.

**`df['adjusted_service_rate']`**
- This creates a new column called `'adjusted_service_rate'`.
- The calculation adjusts the original service rate based on the number of dependents.
- The formula `df['Dependent_count'] / priority_weight` increases the service rate for customers with more dependents, prioritizing them by simulating faster service for customers with more dependents.


### 5. **Calculating Traffic Intensity, Average Customers in the System, and Average Wait Time**
**`df['traffic_intensity']`**
- This calculates the traffic intensity (ρ) using the formula `arrival_rate / adjusted_service_rate`.
- Traffic intensity represents the ratio of customer arrivals to the system's service capacity.

**`df['avg_customers_system']`**
- This calculates the average number of customers in the system (L) using the formula `traffic_intensity / (1 - traffic_intensity)`.
- This represents the average number of customers being served or waiting.

**`df['avg_wait_time']`**
- This calculates the average wait time (W) for a customer, using the formula `1 / (adjusted_service_rate - arrival_rate)`.
- This represents the expected wait time before a customer is served.


### 6. **Filtering the Results and Dropping Invalid Values (NaNs)**
**`df[['CLIENTNUM', 'traffic_intensity', 'avg_customers_system', 'avg_wait_time']]`**
- This selects only the relevant columns (`CLIENTNUM`, `traffic_intensity`, `avg_customers_system`, `avg_wait_time`) for further analysis and visualization.

**`result.dropna()`**
- This drops any rows that contain missing values (`NaN`) in the selected columns.
- It's used to ensure that invalid or incomplete data does not affect further analysis or visualization.


### 7. **Visualizing the Results:**
**Still in development due to a few error**
**`plt.bar(df['CLIENTNUM'], ['avg_wait_time'])`**
- This attempts to create a bar plot where the x-axis represents the client numbers (`CLIENTNUM`) and the y-axis represents the average wait time (`avg_wait_time`). However, this line contains an error: `['avg_wait_time']` should be `df['avg_wait_time']` instead.

**`plt.xlabel('Client Number')`**:
- This sets the label for the x-axis to `'Client Number'`.

**`plt.ylabel('Average Wait Time (hrs)')`**
- This sets the label for the y-axis to `'Average Wait Time (hrs)'`.

**`plt.title('Wait Time by Client')`**
- This sets the title of the plot to `'Wait Time by Client'`.

**`plt.show()`**
- This displays the plot.

