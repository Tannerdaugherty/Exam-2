import pandas as pd
import statsmodels.api as sm

# Load the data from the spreadsheet
data = pd.read_excel(r'C:\Users\DaughertTL18\Downloads\Restaurant Revenue.xlsx')

# Define the independent variables (features)
X = data[['Number_of_Customers', 'Menu_Price', 'Marketing_Spend', 'Average_Customer_Spending', 'Promotions', 'Reviews']]

# Add a constant column to the independent variables
X = sm.add_constant(X)

# Define the dependent variable (target)
y = data['Monthly_Revenue']

# Fit the multiple linear regression model
model = sm.OLS(y, X).fit()

# Print the coefficients and R-squared value
print("Coefficients:\n", model.params)
print("R-squared:", model.rsquared)