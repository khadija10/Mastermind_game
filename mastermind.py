#Étape 1 : Préparation

#imports
import random

#constantes
COMBINATION_LENGTH = 4
MAX_ATTEMPTS = 10
POSSIBLE_VALUES = [str(index) for index in range(1, 7)]  # liste de valuers possibles (1 à 6) [Comprehension list ]

#Étape 2 : Génération de la Combinaison Secrète
def generate_secret_combination():
   
    return [random.choice(POSSIBLE_VALUES) for _ in range(COMBINATION_LENGTH)]

#Étape 3 : Interaction Joueur

def get_player_combination():
    while True:
        combination = input(f"Enter your combination ({COMBINATION_LENGTH} digits from {POSSIBLE_VALUES}): ")
        
        if len(combination) != COMBINATION_LENGTH:
            print(f"Your combination must be exactly {COMBINATION_LENGTH} digits long.")
            continue
        
        if not all(char in POSSIBLE_VALUES for char in combination):
            print(f"Each digit must be one of {POSSIBLE_VALUES}.")
            continue
        
        return list(combination)
    
if __name__ == "__main__":

    secret_combination = generate_secret_combination()
    
    print(secret_combination)

    player_combination = get_player_combination()

    print(player_combination)