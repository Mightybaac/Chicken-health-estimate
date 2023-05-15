print("Welcome to the Chicken Health Diagnostic Tool")

weight = float(input("What is the weight of your chicken in pounds? "))
if weight < 1 or weight > 15:
    print("Invalid weight, please try again")
    exit()

breed = input("What is the breed of your chicken? ").lower()
if breed not in ["rhode island red", "plymouth rock", "buff orpington", "legbar", "marans", "americauna", "silkies", "brahma", "cochin", "easter egger", "sussex"]:
    print("Invalid breed, please try again")
    exit()

appearance = input("How does your chicken look? ").lower()
if "pale" in appearance or "yellow" in appearance:
    print("Possible problem: Anemia")
elif "bloody" in appearance or "swollen" in appearance:
    print("Possible problem: Infection or injury")
elif "scaly" in appearance:
    print("Possible problem: Scaly leg mites")
elif "molting" in appearance:
    print("Possible problem: Normal molting process")
else:
    print("No visible problems detected")

eating = input("Is your chicken eating normally? ").lower()
if "no" in eating:
    print("Possible problem: Appetite loss")
elif "yes" in eating:
    print("No eating problems detected")

drinking = input("Is your chicken drinking water normally? ").lower()
if "no" in drinking:
    print("Possible problem: Dehydration")
elif "yes" in drinking:
    print("No drinking problems detected")

attitude = input("How is your chicken's attitude? ").lower()
if "lethargic" in attitude:
    print("Possible problem: Illness or infection")
elif "aggressive" in attitude:
    print("Possible problem: Stress or pain")
else:
    print("No attitude problems detected")
