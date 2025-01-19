import pandas as pd
from faker import Faker

# Initialize Faker
fake = Faker()

# Number of records you want to generate
num_cases = 1000

# Create an empty list to store data
data = []

for i in range(num_cases):
    # Generate data for each column
    testcase_id = f"TC{i + 1:04d}"  # Format Testcase ID as TC0001, TC0002, etc.
    name = fake.name()
    email = fake.email()
    password = fake.password(length=12)  # Create a random password of length 12
    gender = fake.random_element(elements=("Male", "Female"))

    # Append the row to the data list
    data.append([testcase_id, name, email, password, gender])

# Create a DataFrame from the data list
df = pd.DataFrame(data, columns=["Testcase ID", "name", "email", "pwd", "gender"])

# Save the DataFrame to an Excel file
df.to_excel("test_data.xlsx", index=False)

print("Excel file with test data has been created!")
