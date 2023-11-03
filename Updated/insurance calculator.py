from flask import Flask, render_template, request

app = Flask(__name__)

# Constants for premium calculation (keep them here for the calculation)
SCALE_PREMIUMS = {"Small": 5000, "Medium": 10000, "Large": 20000}
RISK_FACTORS = {"Low": 0.5, "Medium": 1, "High": 2}
DATA_FACTORS = {"Sensitive": 1.5, "Non-sensitive": 1}
LOSS_FACTORS = {1000000: 1, 5000000: 1.5}
REVENUE_FACTORS = {1000000: 1, 10000000: 1.5}
COMPLIANCE_FACTORS = {"yes": 2, "no": 1}

# Define the route for the insurance calculator form
@app.route("/", methods=["GET", "POST"])
def insurance_calculator():
    if request.method == "POST":
        # Get input values from the form
        business_scale = request.form["business_scale"]
        risk_exposure = request.form["risk_exposure"]
        data_type = request.form["data_type"]
        potential_loss = int(request.form["potential_loss"])
        annual_revenue = int(request.form["annual_revenue"])
        compliance_requirements = request.form["compliance_requirements"]

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

        return render_template("result.html", insurance_premium=insurance_premium)

    return render_template("calculator.html")

if __name__ == "__main__":
    app.run(debug=True)
