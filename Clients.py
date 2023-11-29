import random
import pandas as pd
"""
# Fonction pour générer l'âge du client en fonction de plages d'âge prédéfinies avec des probabilités associées.
def generate_age():
    # ...

# Fonction pour générer le genre du client de manière aléatoire avec une probabilité plus élevée pour "female".
def generate_gender():
    # ...

# Fonction pour générer l'état civil du client en fonction de l'âge et du genre avec des probabilités différentes.
def generate_marital_status(age, gender):
    # ...

# Fonction pour générer la catégorie socio-professionnelle en fonction de l'âge du client avec des probabilités différentes.
def generate_SPC_ID(age):
    # ...

# Fonction pour déterminer le type de marché (B2B, B2C, les deux) en fonction de la catégorie socio-professionnelle.
def generate_Market_type(SPC_ID):
    # ...

# Fonction pour déterminer le secteur d'activité en fonction de la catégorie socio-professionnelle.
def generate_Industry_sector(SPC_ID):
    # ...

# Fonction pour sélectionner une agence affiliée en fonction d'une direction générale aléatoire.
def generate_affiliated_agency():
    # ...

# Fonction pour générer le revenu mensuel en fonction de la catégorie socio-professionnelle.
def generate_monthly_income(SPC_ID):
    # ...

# Fonction pour générer les paiements mensuels des dettes en fonction du revenu mensuel.
def generate_monthly_debt_payments(monthly_income):
    # ...

# Fonction pour générer les dépenses mensuelles en fonction du revenu mensuel et des paiements mensuels des dettes.
def generate_monthly_spending(monthly_income, monthly_debt_payments):
    # ...

# Fonction pour générer la valeur nette des actifs en fonction du revenu mensuel et de l'âge.
def generate_assets_worth(monthly_income, age):
    # ...

# Fonction pour générer la stabilité de l'emploi en fonction de l'âge du client.
def generate_employment_stability(age):
    # ...

# Fonction pour générer le score de crédit en fonction de l'âge et du revenu mensuel avec des ajustements basés sur le revenu.
def generate_credit_score(age, monthly_income):
    # ...

# Fonction pour générer les données d'un client en utilisant les fonctions précédentes.
def generate_client_data(client_id):
    # ...

# Fonction pour générer un dataframe de clients avec un nombre spécifié.
def generate_clients_dataframe(num_clients):
    # ...

# Exécution principale pour générer 10 000 enregistrements de clients simulés et les sauvegarder dans un fichier texte.

"""
def generate_age():
    age_ranges = [(18, 24), (25, 44), (45, 64), (65, 82)]
    probabilities = [0.21, 0.38, 0.28, 0.13]
    chosen_range = random.choices(age_ranges, probabilities)[0]
    return random.randint(chosen_range[0], chosen_range[1])


def generate_gender():
    return 'female' if random.random() < 0.58 else 'male'


def generate_marital_status(age, gender):
    if gender == 'female':
        if age < 24:
            return random.choices(['single', 'married'], [0.6, 0.4])[0]
        elif 24 <= age <= 44:
            return random.choices(['single', 'married', 'divorced'], [0.1, 0.7, 0.2])[0]
        else:
            return random.choices(['single', 'married', 'divorced'], [0.03, 0.44, 0.53])[0]
    else:
        if age < 24:
            return random.choices(['single', 'married'], [0.8, 0.2])[0]
        elif 24 <= age <= 44:
            return random.choices(['single', 'married', 'divorced'], [0.08, 0.62, 0.3])[0]
        else:
            return random.choices(['married', 'divorced'], [0.35, 0.65])[0]
        

def generate_SPC_ID(age):
    if age > 60:
        return random.choice(['024', '069'])
    else:
        spc_distribution = [
            ('000', 0.03), ('001', 0.01), ('002', 0.06), ('003', 0.08), ('004', 0.05),
            ('005', 0.08), ('006', 0.03), ('007', 0.05), ('008', 0.03), ('009', 0.08),
            ('010', 0.03), ('011', 0.05), ('012', 0.03), ('014', 0.13), ('015', 0.08),
            ('016', 0.10), ('020', 0.03), ('021', 0.07), ('022', 0.02), ('023', 0.02),
            ('024', 0.03), ('025', 0.13), ('026', 0.08), ('027', 0.10), ('030', 0.03),
            ('031', 0.03), ('032', 0.07), ('033', 0.06), ('035', 0.06), ('036', 0.06),
            ('037', 0.02), ('038', 0.04), ('039', 0.03), ('040', 0.07), ('041', 0.07),
            ('042', 0.10), ('043', 0.02), ('044', 0.02), ('045', 0.06), ('046', 0.03),
            ('047', 0.07), ('048', 0.07), ('049', 0.02), ('050', 0.07), ('051', 0.07),
            ('052', 0.10), ('053', 0.02), ('054', 0.02), ('055', 0.04), ('056', 0.02),
            ('057', 0.06), ('058', 0.06), ('059', 0.03), ('060', 0.07), ('061', 0.07),
            ('062', 0.10), ('063', 0.02), ('064', 0.02), ('065', 0.04), ('066', 0.07),
            ('067', 0.07), ('068', 0.02), ('069', 0.10), ('070', 0.02), ('071', 0.02),
            ('072', 0.03), ('073', 0.02), ('074', 0.02), ('099', 0.10), ('100', 0.10)
        ]
        spc_ids, probabilities = zip(*spc_distribution)
        return random.choices(spc_ids, probabilities)[0]

def generate_Market_type(SPC_ID):
    B2B_markets = [
        '000', '001', '002', '003', '004', '005', '007', '008', '009', '010', '011',
        '012', '013', '014', '015', '016', '017', '018', '019', '020', '021', '022',
        '023', '024', '025', '026', '027', '028', '029', '030', '031', '032', '033',
        '034', '035', '036', '037', '038', '039', '040', '041', '042', '043', '044',
        '060', '061', '062', '063'
    ]
    B2C_markets = [
        '006', '045', '046', '047', '048', '049', '050', '051', '052', '053', '054',
        '055', '056', '057', '058', '059', '064', '065', '066', '067', '068', '069',
        '070', '071', '072', '073', '074'
    ]

    if SPC_ID in B2B_markets and SPC_ID in B2C_markets:
        return 'Both B2B and B2C'
    elif SPC_ID in B2B_markets:
        return 'B2B Market (Business-to-Business)'
    else:
        return 'B2C Market (Business-to-Consumer)'
    
def generate_Industry_sector(SPC_ID):
    generalized_mapping = {
        "Armed forces": ["000"],
        "Public Administration": ["001", "003", "004", "005", "006", "007", "008", "009", "010", "011", "012", "013", "014", "015"],
        "Private Sector Management": ["016", "017", "018"],
        "Private Sector Technical and Support": ["019", "020", "021"],
        "Education": ["022", "023", "030", "031", "013", "014", "015", "037"],
        "Healthcare": ["032", "033", "034", "038"],
        "Legal Activities": ["035", "057", "066"],
        "Real Estate Activities": ["007", "067", "068"],
        "Self-Employed Professionals": ["027", "030", "031", "032", "033", "034", "035", "036", "037", "038", "039", "040", "041", "042", "043","027", "028", "029", "070", "071"],
        "Self-Employed Artisans and Traders": ["026", "044", "045", "046", "047", "048", "049"],
        "Merchants and Traders": ["050", "051", "052", "053", "054", "055", "056", "057", "058", "059", "100"],
        "Agriculture and Fishing": ["060", "061", "062", "063"],
        "Retirees and Pensioners": ["024", "025", "069"],
        "Unemployed and Others": ["064", "099"]
    }

    for key, value in generalized_mapping.items():
        if SPC_ID in value:
            return key

    return "Unreported"


def generate_affiliated_agency():
    Centre_et_Cap_Bon = [11, 18, 21, 27, 28, 29, 32, 33, 37, 40, 42, 43, 45, 49, 51, 52, 54, 55, 56, 67, 77, 94, 96, 102, 105,
                        108, 109, 116, 122, 125, 131, 135, 171, 172, 175, 178, 182, 183, 185, 190, 193, 195, 196, 197, 198, 227]
    Grand_Tunis = [0, 2, 3, 4, 6, 7, 8, 9, 10, 34, 35, 38, 44, 58, 70, 71, 79, 80, 82, 86, 101, 103, 104,
                  106, 107, 113, 114, 115, 118, 119, 120, 121, 123, 124, 126, 132, 133, 141, 142, 144, 145,
                  146, 147, 148, 150, 152, 153, 154, 155, 157, 161, 162, 165, 168, 173, 174, 177, 179, 180,
                  181, 184, 186, 187, 188, 189, 191, 192, 194, 200, 217, 224, 226, 232]
    Nord = [5, 26, 31, 36, 47, 53, 59, 61, 62, 72, 73, 75, 89, 93, 97, 111, 127, 128, 129, 130, 138, 139, 140, 151, 156, 160, 166,
            219, 220, 222, 223, 229, 230, 233, 235]
    Sud = [1, 12, 13, 14, 15, 16, 17, 19, 20, 22, 23, 24, 25, 30, 39, 41, 46, 48, 50, 57, 60, 63, 64, 65, 66, 68, 69, 74, 76, 78, 83,
           110, 112, 117, 134, 136, 137, 143, 149, 158, 159, 163, 164, 167, 169, 170, 176, 205, 218, 221, 225, 228, 231, 234]

    direction_generale_mapping = {
        'Centre et Cap Bon': 0.30,
        'Grand tunis': 0.25,
        'Sud': 0.25,
        'Nord': 0.20
    }

    selected_direction_generale = random.choices(
        list(direction_generale_mapping.keys()),
        list(direction_generale_mapping.values())
    )[0]

    if selected_direction_generale == 'Centre et Cap Bon':
        return random.choice(Centre_et_Cap_Bon)
    elif selected_direction_generale == 'Grand tunis':
        return random.choice(Grand_Tunis)
    elif selected_direction_generale == 'Sud':
        return random.choice(Sud)
    else:
        return random.choice(Nord)
    


def generate_monthly_income(SPC_ID):
    income_ranges = {
    "000": (1000, 2500),    # Armed forces
    "001": (5000, 8000),    # High-level civil servants (State)
    "002": (4000, 7000),    # Public sector business executives
    "003": (3000, 4500),    # Public sector senior managers
    "004": (4000, 7000),    # Medical and related professionals
    "005": (2500, 5000),    # Public sector engineers
    "006": (2000, 5000),    # Public sector lawyers and related professionals
    "007": (2500, 3500),    # Public sector architects and related professionals
    "008": (1500, 3000),    # Public sector accounting and related professionals
    "009": (1500, 2000),    # Primary school teachers in the public sector
    "010": (2000, 3000),    # Secondary school teachers in the public sector
    "011": (4000, 6500),    # University professors in the public sector
    "012": (3500, 6000),    # Middle managers in the public sector
    "013": (3000, 5000),    # Technicians in the public sector
    "014": (2500, 4000),    # Employees in the public sector
    "015": (2200, 3500),    # Workers in the public sector
    "016": (5000, 8000),    # Private sector business executives
    "017": (4500, 7000),    # Private sector senior managers
    "018": (4000, 6500),    # Middle managers in the private sector
    "019": (3000, 5500),    # Technicians in the private sector
    "020": (2500, 4500),    # Employees in the private sector
    "021": (2200, 4000),    # Workers in the private sector
    "022": (0, 1000),       # Students
    "023": (0, 500),        # Minors
    "024": (3500, 5000),    # Retirees
    "025": (3500, 5000),    # Rentiers
    "026": (3000, 5000),    # Self-employed artisans and traders
    "027": (4000, 6000),    # Self-employed professionals
    "028": (3500, 5500),    # Other self-employed
    "029": (2000, 4000),    # Young self-employed
    "030": (3000, 6000),    # Self-employed professionals - Students
    "031": (4000, 7000),    # Self-employed professionals - Architects and urban planners
    "032": (4500, 7000),    # Self-employed professionals - Medical professionals and related occupations
    "033": (4000, 6500),    # Self-employed professionals - Pharmacists and laboratory professionals
    "034": (3500, 6000),    # Self-employed professionals - Paramedical occupations
    "035": (4000, 6500),    # Self-employed professionals - Lawyers and related occupations
    "036": (3500, 5500),    # Self-employed professionals - Private educational establishment owners
    "037": (4000, 7000),    # Self-employed professionals - Notaries and judicial officers
    "038": (3500, 6000),    # Self-employed professionals - Sociologists, Psychologists, and related occupations
    "039": (3000, 5000),    # Self-employed professionals - Artists, Painters, Athletes
    "040": (3500, 6000),    # Self-employed professionals - Linguists, Translators
    "041": (3500, 6000),    # Self-employed professionals - Authors, Journalists, Writers
    "042": (3500, 6000),    # Self-employed professionals - Forwarding agents
    "043": (3000, 5000),    # Self-employed professionals - Other occupations
    "044": (2500, 4500),    # Artisans - Small trades
    "045": (3000, 5000),    # Artisans - Maintenance/Repair/Building
    "046": (3000, 5000),    # Artisans - Tourism/Leisure
    "047": (3000, 5000),    # Artisans - Metallurgy, Mechanical Construction
    "048": (3000, 5000),    # Artisans - Precision mechanics, Art metalwork
    "049": (2500, 4500),    # Artisans - Other trades
    "050": (2500, 4500),    # Merchants - Food retail
    "051": (3000, 5000),    # Merchants - Catering
    "052": (3000, 5000),    # Merchants - Clothing
    "053": (3000, 5000),    # Merchants - Transport
    "054": (3000, 5000),    # Merchant - Building, Sanitary
    "055": (3000, 5000),    # Merchants - Furniture & Decoration
    "056": (3000, 5000),    # Merchants - Household Appliances
    "057": (3000, 5000),    # Merchant - Tourism/Leisure
    "058": (3000, 5000),    # Merchant - School supplies
    "059": (3000, 5000),    # Merchants - Hardware
    "060": (2000, 4000),    # Farmers - Farmer
    "061": (2000, 4000),    # Farmers - Fisherman
    "062": (2000, 4000),    # Farmers - Livestock breeders
    "063": (2000, 4000),    # Agricultural & Fishing laborers
    "064": (0, 1000),       # Unemployed
    "065": (4500, 7000),    # Private sector engineers
    "066": (4500, 7000),    # Private sector lawyers and related professionals
    "067": (4500, 7000),    # Private sector architects and related professionals
    "068": (4500, 7000),    # Private sector accounting and related professionals
    "069": (3500, 5000),    # Retired self-employed
    "070": (3500, 5000),    # Self-employed - High-level employee
    "071": (2500, 4000),    # Self-employed - Worker & Employee
    "099": (2500, 5000),    # Others
    "100": (2500, 4500)     # Merchant - Others
}
    if SPC_ID in income_ranges:
        min_income, max_income = income_ranges[SPC_ID]
    else:
        # Set a default income range for SPC_IDs not in the dictionary
        min_income, max_income = (3000, 6000)

    # Generate a random income within the specified range
    monthly_income = random.randint(min_income, max_income)

    return monthly_income

def generate_monthly_debt_payments(monthly_income):
    # Define different debt payment probabilities
    probabilities = [0.5, 0.3, 0.2]

    # Assign debt payments based on the probabilities
    debt_payments = random.choices([0.4 * monthly_income, 0, 0.3 * monthly_income], probabilities)[0]

    return int(debt_payments)

def generate_monthly_spending(monthly_income, monthly_debt_payments):
    # Calculate the remaining income after deducting debt payments
    remaining_income = monthly_income - monthly_debt_payments

    # Define the spending multiplier probabilities
    spending_multipliers = [0.6, 0.7]

    # Randomly select one of the spending multipliers
    spending_multiplier = random.choice(spending_multipliers)

    # Calculate the monthly spending using the selected multiplier
    monthly_spending = int(remaining_income * spending_multiplier)

    return monthly_spending
    
def generate_assets_worth(monthly_income, age):
    base_assets = 0.5 * monthly_income * (age - 18)
    if monthly_income < 3000:
        additional_assets = random.randint(10000, 20000)
    elif monthly_income < 5000:
        additional_assets = random.randint(15000, 25000)
    else:
        additional_assets = random.randint(20000, 30000)
    
    assets_worth = base_assets + additional_assets
    return assets_worth


def generate_employment_stability(age):
    max_stability = min(age - 18, 30)
    return random.randint(0, max_stability)


def generate_credit_score(age, monthly_income):
    if age <= 30:
        # Younger clients have a higher chance of having a lower credit score
        credit_score = random.randint(600, 750)
    else:
        credit_score = random.randint(650, 800)

    # Adjust credit score based on monthly income
    if monthly_income < 3000:
        credit_score -= random.uniform(25, 50)
    elif monthly_income < 5000:
        credit_score -= random.uniform(10, 25)

    # Ensure the credit score is within the specified range
    credit_score = max(credit_score, 300)  # Minimum credit score set to 300
    credit_score = min(credit_score, 850)  # Maximum credit score set to 850

    return int(credit_score)  # Convert the credit_score to an integer before returning


def generate_client_data(client_id):
    age = generate_age()
    gender = generate_gender()
    marital_status = generate_marital_status(age, gender)
    SPC_ID = generate_SPC_ID(age)
    industry_sector = generate_Industry_sector(SPC_ID)
    market_type = generate_Market_type(SPC_ID)
    affiliated_agency = generate_affiliated_agency()
    monthly_income = generate_monthly_income(SPC_ID)
    monthly_debt_payments = generate_monthly_debt_payments(monthly_income)
    monthly_spending = generate_monthly_spending(monthly_income, monthly_debt_payments)
    assets_worth = generate_assets_worth(monthly_income, age)
    employment_stability = generate_employment_stability(age)
    credit_score = generate_credit_score(age, monthly_income)

    client_data = {
        "client_ID": client_id,
        "age": age,
        "gender": gender,
        "marital_status": marital_status,
        "SPC_ID": SPC_ID,
        "Industry_sector": industry_sector,
        "Market_type": market_type,
        "Affiliated_agency": affiliated_agency,
        "Monthly_income": monthly_income,
        "Monthly_debt_payments": monthly_debt_payments,
        "Monthly_spending": monthly_spending,
        "Assets_worth": assets_worth,
        "Employment_Stability": employment_stability,
        "Credit_Score": credit_score
    }
    return client_data


def generate_clients_dataframe(num_clients):
    clients_data = [generate_client_data(client_id) for client_id in range(1, num_clients + 1)]
    df = pd.DataFrame(clients_data)
    return df



if __name__ == "__main__":
    num_clients = 10000
    df = generate_clients_dataframe(num_clients)
    df.to_csv("client.txt", sep=";", index=False)