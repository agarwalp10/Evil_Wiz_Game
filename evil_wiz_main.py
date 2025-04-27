#Importing every class from classes.py
from classes import *

# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Ninja")  
    print("4. Rogue") 
    
    # using a try and except for a input, incase the input is incorrect. Checks if its not 1,2,3,4
    # raises an error and prints out the error, allowing for program to still run
    while True:
        try:
            class_choice = input("Enter the number of your class choice: ")
            if class_choice not in ['1', '2', '3', '4']:
                raise ValueError("Invalid class choice")
            break
        except ValueError as ve:
            print(f"Error: {ve}. Please choose a valid number (1-4).")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Ninja(name)
    elif class_choice == '4':
        return Rogue(name)
    
# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        
        choice = input("Choose an action: ")
        print("\n ======= GAME PLAY =======")

        if choice == '1':
            player.attack(wizard) 
        elif choice == '2':
            player.special_ability(wizard)
        elif choice == '3':
            player.heal() 
        elif choice == '4':
            player.display_stats() 
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate - the wizard will always take a turn no matter the user choice 
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard, {wizard.name}, has been defeated by {player.name}!")


        

# Main function to handle the flow of the game
def main():
    # Character creation phase - first thing you want to do is to create a character
    player = create_character()

    # Evil Wizard is created - creating an instance of the evil wizard
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    # using a try and except to make sure if there is an error, that the program runs smoothly still.
    # if there is an error, the statment will start with "Something went wrong:" and then types out the error"
    try: 
        main()
    except Exception as e: 
        print(f'Something went wrong: {e}')

# TODO: Read me
# TODO: Advanced python, creativity 
