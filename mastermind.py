#Étape 1 : Préparation

#imports
import random

#constantes
COMBINATION_LENGTH = 4
MAX_ATTEMPTS = 10
POSSIBLE_VALUES = [str(index) for index in range(1, 7)]  # valuers possibles [Comprehension list ]

#Étape 2 : Génération de la Combinaison Secrète
def generate_secret_combination():
   
    return [random.choice(POSSIBLE_VALUES) for _ in range(COMBINATION_LENGTH)]

if __name__ == "__main__":

    secret_combination = generate_secret_combination()
    
    print(secret_combination)