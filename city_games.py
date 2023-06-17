import random

resources = {
    'wood': 100,
    'stone': 100,
    'gold': 50
}

buildings = {
    'house': {
        'cost': {'wood': 10, 'stone': 5},
        'population_increase': 5
    },
    'market': {
        'cost': {'wood': 20, 'stone': 10, 'gold': 5},
        'income': 10
    },
    'mine': {
        'cost': {'wood': 15, 'stone': 10},
        'gold_increase': 5
    }
}

city_population = 10
city_gold = 20

def print_status():
    print("Resources:")
    for resource, amount in resources.items():
        print(f"{resource.capitalize()}: {amount}")
    print("City Population:", city_population)
    print("City Gold:", city_gold)

def build_building(building):
    if building in buildings:
        if all(resources[resource] >= cost for resource, cost in buildings[building]['cost'].items()):
            for resource, cost in buildings[building]['cost'].items():
                resources[resource] -= cost
            if 'population_increase' in buildings[building]:
                city_population += buildings[building]['population_increase']
                print(f"{building.capitalize()} built! Population increased by {buildings[building]['population_increase']}.")
            elif 'gold_increase' in buildings[building]:
                city_gold += buildings[building]['gold_increase']
                print(f"{building.capitalize()} built! Gold production increased by {buildings[building]['gold_increase']}.")
            else:
                print(f"{building.capitalize()} built!")
        else:
            print("Insufficient resources to build", building)
    else:
        print("Invalid building type")

def game_loop():
    print("Welcome to the City of Python!")
    print("You are the mayor. Build and manage your city.")

    while True:
        print("\n--- City Status ---")
        print_status()

        print("\n--- Available Buildings ---")
        for building in buildings:
            print(building.capitalize())

        print("\nWhat would you like to build? (Type 'quit' to exit)")
        building_choice = input("Building: ")

        if building_choice.lower() == 'quit':
            print("Thanks for playing!")
            break

        build_building(building_choice.lower())

game_loop()
