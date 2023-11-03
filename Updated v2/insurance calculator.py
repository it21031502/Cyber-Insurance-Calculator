from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)

# Load the dataset
df = pd.read_csv('insurance_dataset.csv')

# Define the target variable
target = "premium"

# Encode categorical features with one-hot encoding
df = pd.get_dummies(df, columns=["business_scale", "risk_exposure", "data_type", "compliance_requirements"], drop_first=True)

# Define the features and target variable
features = df.columns.difference([target])

# Split the data into features (X) and target (y)
X = df[features]
y = df[target]

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a machine learning model (Random Forest regressor)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

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

        # Prepare input data for the model with one-hot encoding
        input_data = pd.DataFrame({
            "business_scale_" + business_scale: [1],
            "risk_exposure_" + risk_exposure: [1],
            "data_type_" + data_type: [1],
            "potential_loss": [potential_loss],
            "annual_revenue": [annual_revenue],
            "compliance_requirements_" + compliance_requirements: [1]
        })

        # Ensure that all possible one-hot encoded feature names are included
        for column in X.columns:
            if column not in input_data:
                input_data[column] = 0

        # Reorder columns to match the model's expected order
        input_data = input_data[X.columns]

        # Predict the insurance premium using the model
        insurance_premium = model.predict(input_data)[0]

        return render_template("result.html", insurance_premium=insurance_premium)

    return render_template("calculator.html")

if __name__ == "__main__":
    app.run(debug=True)
