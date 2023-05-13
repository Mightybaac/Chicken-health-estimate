import datetime

# Dictionary of breed scores
breed_scores = {
    "Buff Orpington": 2,
    "Plymouth Rock": 1,
    "Rhode Island Red": 0
}

# Function to prompt user for input for each attribute
def get_chicken_info():
    weight = float(input("Enter weight of chicken in grams: "))
    breed = input("Enter breed of chicken: ")
    while breed not in breed_scores.keys():
        breed = input("Invalid breed. Enter breed of chicken: ")
    appearance = input("Enter appearance of chicken: ")
    color = input("Enter color of chicken: ")
    feather_density = input("Enter feather density of chicken: ")
    comb_color = input("Enter comb color of chicken: ")
    eating = input("Is the chicken eating? (yes or no): ")
    drinking = input("Is the chicken drinking? (yes or no): ")
    attitude = input("Enter attitude of chicken: ")
    return {
        "weight": weight,
        "breed": breed,
        "appearance": appearance,
        "color": color,
        "feather_density": feather_density,
        "comb_color": comb_color,
        "eating": eating.lower() == "yes",
        "drinking": drinking.lower() == "yes",
        "attitude": attitude
    }

# Function to calculate health score based on age
def calculate_health_score(age, health_score):
    if age < 6:
        health_score += 2
    elif age < 12:
        health_score += 1
    elif age < 18:
        health_score -= 1
    else:
        health_score -= 2
    return health_score

# Get input data from user
chicken_info = get_chicken_info()

# Calculate initial health score based on input data
health_score = 0
if chicken_info["weight"] > 2000:
    health_score += 2
elif chicken_info["weight"] > 1500:
    health_score += 1
else:
    health_score -= 1

health_score += breed_scores[chicken_info["breed"]]

if chicken_info["appearance"] == "Good":
    health_score += 1
else:
    health_score -= 1

if chicken_info["color"] == "Brown":
    health_score += 1
else:
    health_score -= 1

if chicken_info["feather_density"] == "High":
    health_score += 1
else:
    health_score -= 1

if chicken_info["comb_color"] == "Red":
    health_score += 1
else:
    health_score -= 1

if chicken_info["eating"]:
    health_score += 1

# Calculate age of chicken
birthdate_str = input("Enter birthdate of chicken (format: YYYY-MM-DD): ")
birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d")
age_in_days = (datetime.datetime.now() - birthdate).days
age_in_weeks = age_in_days // 7

# Calculate final health score based on age
health_score = calculate_health_score(age_in_weeks, health_score)

# Output final health score and save to file
filename = input("Enter filename to save health score: ")
with open(filename, "w") as f:
    f.write(f"Health score: {health_score}\n")
print(f"Health score: {health_score}")
