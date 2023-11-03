import csv
import random

# Define possible values for each feature
business_scales = ["Small", "Medium", "Large"]
risk_exposures = ["Low", "Medium", "High"]
data_types = ["Sensitive", "Non-sensitive"]
compliance_requirements = ["yes", "no"]

# Create and open the CSV file for writing
with open("insurance_dataset.csv", mode="w", newline="") as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(["business_scale", "risk_exposure", "data_type", "potential_loss", "annual_revenue", "compliance_requirements", "premium"])

    # Generate and write 65,310 rows of random data
    for _ in range(65310):
        business_scale = random.choice(business_scales)
        risk_exposure = random.choice(risk_exposures)
        data_type = random.choice(data_types)
        potential_loss = random.randint(50000, 5000000)
        annual_revenue = random.randint(1000000, 20000000)
        compliance_requirement = random.choice(compliance_requirements)
        premium = random.randint(3000, 15000)

        writer.writerow([business_scale, risk_exposure, data_type, potential_loss, annual_revenue, compliance_requirement, premium])

print("CSV file 'insurance_dataset.csv' has been created.")
