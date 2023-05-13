from enum import Enum

class Breed(Enum):
    RHODE_ISLAND_RED = "Rhode Island Red"
    LEGBORN = "Leghorn"
    # Add more breeds as needed

class FeatherDensity(Enum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"
    # Add more feather densities as needed

class Chicken:
    BREED_SCORES = {
        Breed.RHODE_ISLAND_RED: 5,
        Breed.LEGBORN: 3,
        # Add scores for more breeds as needed
    }
    
    FEATHER_DENSITY_SCORES = {
        FeatherDensity.HIGH: 3,
        FeatherDensity.MEDIUM: 1,
        FeatherDensity.LOW: -2,
        # Add scores for more feather densities as needed
    }

    def __init__(self, weight, breed, appearance, color, feather_density, comb_color, is_eating, is_drinking, attitude):
        self.weight = weight
        self.breed = breed
        self.appearance = appearance
        self.color = color
        self.feather_density = feather_density
        self.comb_color = comb_color
        self.is_eating = is_eating
        self.is_drinking = is_drinking
        self.attitude = attitude

    def estimate_health(self):
        health_score = 0
        
        # Calculate score for weight
        if self.weight > 4 and self.weight < 8:
            health_score += 5
        elif self.weight >= 8:
            health_score += 3
        else:
            health_score -= 2
        
        # Calculate score for breed
        breed_score = Chicken.BREED_SCORES.get(self.breed, 0)
        health_score += breed_score
        
        # Calculate score for appearance
        if self.appearance == "Clean":
            health_score += 3
        elif self.appearance == "Dirty":
            health_score -= 2
        
        # Calculate score for color
        if self.color == "White":
            health_score += 1
        
        # Calculate score for feather density
        feather_density_score = Chicken.FEATHER_DENSITY_SCORES.get(self.feather_density, 0)
        health_score += feather_density_score
        
        # Calculate score for comb color
        if self.comb_color == "Red":
            health_score += 1
        
        # Calculate score for eating and drinking
        if self.is_eating and self.is_drinking:
            health_score += 3
        
        # Calculate score for attitude
        if self.attitude == "Friendly":
            health_score += 2
        elif self.attitude == "Aggressive":
            health_score -= 2
        
        return health_score

# Example usage
chicken1 = Chicken(5, Breed.RHODE_ISLAND_RED, "Clean", "White", FeatherDensity.HIGH, "Red", True, True, "Friendly")
health_score = chicken1.estimate_health()
print(f"Chicken 1 health score: {health_score}")
