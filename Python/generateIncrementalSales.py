import random
import pandas as pd

# Define the columns
columns = ['Branch_ID', 'Dealer_ID', 'Model_ID', 'Revenue', 'Units_Sold', 'Date_ID', 'Day', 'Month', 'Year', 'Branch_Name', 'Dealer_Name', 'Product_Name']

# Update to make Branch_Name and Product_Name more diverse
def generate_diverse_data(num_rows):
    branch_names = [
        "AC Cars Motors", "Deccan Motors", "Wiesmann Motors", 
        "Subaru Motors", "Saab Motors", "Messerschmitt Motors", "Lexus Motors",
        "Porsche Center", "Infinity Motors", "Tesla Dealers", "Volvo Cars", "Jaguar Land Rover"
    ]
    product_names = [
        "BMW", "Honda", "Tata", "Hyundai", "Renault", "Cadillac",
        "Porsche", "Tesla", "Volvo", "Jaguar", "Land Rover", "Infinity"
    ]
    data = []
    for i in range(1, num_rows + 1):
        branch_id = f"BR{str(random.randint(1, 9999)).zfill(4)}"
        dealer_id = f"DLR{str(random.randint(1, 9999)).zfill(4)}"
        model_id = f"{random.choice(product_names)}-M{random.randint(1, 500)}"
        revenue = random.randint(5000000, 20000000)
        units_sold = random.randint(1, 10)
        date_id = f"DT{str(i).zfill(5)}"  # Auto-incrementing and consecutive Date_ID
        day = random.randint(1, 31)
        month = random.randint(1, 12)
        year = random.choice([2017, 2018, 2019, 2020])
        branch_name = random.choice(branch_names)
        dealer_name = random.choice(branch_names)  # Dealer_Name from the same diverse pool
        product_name = random.choice(product_names)
        data.append([branch_id, dealer_id, model_id, revenue, units_sold, date_id, day, month, year, branch_name, dealer_name, product_name])
    return data

# Generate data for 10 rows
rows_diverse = generate_diverse_data(10)

# Create a DataFrame
df_incremental = pd.DataFrame(rows_diverse, columns=columns)

# Save to a CSV file
file_path_incremental = "C:/Users/tahir/Desktop/incrementalDataAnalytics/Data/IncrementalSales.csv"
df_incremental.to_csv(file_path_incremental, index=False)