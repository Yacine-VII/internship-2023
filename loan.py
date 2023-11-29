import pandas as pd
import random
def generate_default(client, credit_amount, number_of_years_reimbursed, monthly_amount):
    default_prob = 0.1

    # Probability adjustments based on conditions
    married_prob_adjustment = -0.05 if client['marital_status'] == 'married' else 0
    younger_than_25_prob_adjustment = 0.02 if client['age'] < 25 else 0
    net_monthly_income = client['Monthly_income'] - (client['Monthly_debt_payments'] + client['Monthly_spending'])
    high_debt_prob_adjustment = 0.02 if net_monthly_income < client['Monthly_income'] * 0.2 else 0
    high_assets_prob_adjustment = -0.02 if client['Assets_worth'] > 50000 else 0
    high_employment_stability_prob_adjustment = -0.04 if client['Employment_Stability'] >= 5 else 0
    high_credit_score_prob_adjustment = -0.01 if client['Credit_Score'] >= 750 else 0

    # Calculate the adjusted probability of default based on conditions
    adjusted_default_prob = default_prob + married_prob_adjustment + younger_than_25_prob_adjustment \
                           + high_debt_prob_adjustment + high_assets_prob_adjustment \
                           + high_employment_stability_prob_adjustment + high_credit_score_prob_adjustment

    # Check if the credit amount affects the probability of default
    if credit_amount > int(client['Monthly_income']) // 10 * 5:
        adjusted_default_prob += 0.2

    # Check if the monthly amount affects the probability of default
    if monthly_amount > credit_amount / (number_of_years_reimbursed * 12):
        adjusted_default_prob += 0.2

    # Clamp the probability between 0 and 1
    adjusted_default_prob = max(0, min(1, adjusted_default_prob))



    # Determine if the loan defaults
    defaulted = 1 if random.random() <= adjusted_default_prob else 0

    return defaulted

# Function to generate the Loan file
def generate_loan_data(client_data):
    loan_labels = ["BINAA", "MELKI", "ARDHI"]
    max_repayment_years = 18


    loan_data = pd.DataFrame(columns=[
        'Loan_ID', 'Loan_Label', 'Attached_client', 'credit_amount', 'annual_interest_rate',
        'monthly_amount', 'defaulted', 'default_loan_amount'
    ])

    for index, client in client_data.iterrows():
        loan_id = index + 1
        loan_label = random.choice(loan_labels)
        attached_client = client['client_ID']
        number_of_years_reimbursed = random.randint(1, max_repayment_years)
        credit_amount = int(client['Monthly_income']) * random.randint(5, 15)  # Adjust credit amount based on monthly income
        if client['Monthly_income'] == 0:
            annual_interest_rate=0.10
        else:
            annual_interest_rate = random.uniform(0.08, 0.18)
        monthly_amount =( credit_amount+(credit_amount*annual_interest_rate*number_of_years_reimbursed) )/ (number_of_years_reimbursed * 12)


        defaulted = generate_default(client, credit_amount, number_of_years_reimbursed, monthly_amount)
        default_loan_amount = int(credit_amount * random.uniform(0.1, 0.15)) if defaulted else None

        loan_data.loc[index] = [loan_id, loan_label, attached_client, credit_amount, annual_interest_rate,
                                monthly_amount, defaulted, default_loan_amount]

    return loan_data

if __name__ == "__main__":
    # Read the client data from "client.txt" into a dataframe
    client_data = pd.read_csv("client.txt", sep=';')

    # Generate the loan data
    loan_data = generate_loan_data(client_data)

    # Write the loan data to "loan.txt" file
    loan_data.to_csv("loan.txt", sep=';', index=False)
