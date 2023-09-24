# Variables for insurance calculation
business_scale = input("Size of the business (Small, Medium, Large): ")
risk_exposure = input("Risk factor (Low, Medium, High): ")
data_type = input("Type of data (Sensitive/Non-sensitive): ")
potential_loss = int(input("Expected loss: "))
annual_revenue = int(input("Annual revenue: "))
compliance_requirements = input("Compliance with requirements (yes/no): ")

# Constants for premium calculation
SCALE_PREMIUMS = {"Small": 5000, "Medium": 10000, "Large": 20000}
RISK_FACTORS = {"Low": 0.5, "Medium": 1, "High": 2}
DATA_FACTORS = {"Sensitive": 1.5, "Non-sensitive": 1}
LOSS_FACTORS = {1000000: 1, 5000000: 1.5}
REVENUE_FACTORS = {1000000: 1, 10000000: 1.5}
COMPLIANCE_FACTORS = {"yes": 2, "no": 1}

# Calculate base premium based on business scale
base_premium = SCALE_PREMIUMS.get(business_scale, 0)

# Calculate risk factor based on risk exposure
risk_factor = RISK_FACTORS.get(risk_exposure, 0)

# Calculate data factor based on data sensitivity
data_factor = DATA_FACTORS.get(data_type, 0)

# Calculate loss factor based on potential loss
loss_factor = max([factor for loss, factor in LOSS_FACTORS.items() if potential_loss > loss], default=1)

# Calculate revenue factor based on annual revenue
revenue_factor = max([factor for revenue, factor in REVENUE_FACTORS.items() if annual_revenue > revenue], default=1)

# Calculate compliance factor based on compliance requirements
compliance_factor = COMPLIANCE_FACTORS.get(compliance_requirements, 0)

# Calculate the final insurance premium
insurance_premium = base_premium * risk_factor * data_factor * loss_factor * revenue_factor * compliance_factor

print("The insurance premium for this company is $" + str(insurance_premium))