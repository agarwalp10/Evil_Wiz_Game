import random

# ====================== BASE CHARACTER CLASS ============================
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # This stores max health 
 
    
    # Function gives attacker a random attack power 
    def attack(self, opponent):
        damage = random.randint(1,30) 
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")

    # User can view stats for health and attack power
    def display_stats(self):
        print(f"{self.name}'s Stats: Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
        print('The Evil Wizard will still be able to attack')

    # User has the ability to heal
    def heal(self):
        self.health += 20 
        if self.health > self.max_health:
                self.health = self.max_health 
        print(f'{self.name} regenerated to {self.health} health')
        print('The Evil Wizard will still be able to attack')

# ============================ SUBCLASSES ================================ 

# * Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  

    # Each character gets two special abilities 
    def special_ability(self, opponent): #adding an opponent, this is the character we will be attacking
        print('Select Special Ability')
        print('1. Crippling Strike') 
        print('2. Battle Rage') 
        # Error checking for invalid input
        while True:
            try:
                action = input("Choose an Ability: ")
                if action not in ['1', '2']:
                    raise ValueError("Invalid class choice")
                break
            except ValueError as ve:
                print(f"Error: {ve}. Please choose a valid number.")
        
        if action == '1': 
            '''
            Ability: Crippling Strike 
            Description: Attacks opponent but your attack power also decreases, but if attack power gets to 0, it stays at 2
            '''
            opponent.health -= 15
            self.attack_power -= 2
            if self.attack_power <= 0:
                self.attack_power = 2 # This function won't allow player to go below 2
            print(f"Crippling Strike used on {opponent.name}. Their health was reduced by 15. Player attack power reduced to {self.attack_power} ")
        elif action == '2': 
            '''
            Ability: Battle Rage
            Description: Increases Warrior health and Attack by 5
            '''
            self.health += 5
            if self.health > self.max_health:
                self.health = self.max_health
            self.attack_power += 5
            print(f'{self.name} uses Battle Rage, and increase health and attack power by 5!')


# * Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  

    # Each character gets two special abilities 
    def special_ability(self,opponent): 
        print('Select Special Ability')
        print('1. Avada Kedavra')
        print('2. Reparo')
        while True:
            try:
                action = input("Choose an Ability: ")
                if action not in ['1', '2']:
                    raise ValueError("Invalid class choice")
                break
            except ValueError as ve:
                print(f"Error: {ve}. Please choose a valid number.")
        
        if action == '1': 
            '''
            Ability: Avada Kedavra
            Description: powerful spell casted on opponent
            '''
            self.attack_power += 10
            opponent.health -= self.attack_power
            print(f'{self.name} has used Avada Kedavra, for a damage of {self.attack_power}.')
        elif action == '2':
            '''
            Ability: Reparo
            Description: increases health by 5, but some of it rubs off on the opponent
            '''
            self.health += 5
            opponent.health +=2
            if self.health > self.max_health:
                self.health = self.max_health
            print(f'{self.name} has repaired health, increasing their health to {self.health}, but unfortunately some of it got used on {opponent.name}. Their health increased by 2')


    

#* Creating a Ninja Class
class Ninja(Character):
    def __init__(self, name):
        super().__init__(name, health = 130, attack_power = 20)

    # Each character gets two special abilities 
    def special_ability(self, opponent): #adding an opponent, so this is the person we want to attack
        print('Select Special Ability')
        # two seperate things we can use
        print('1. Daggers')
        print('2. Stealth mode and quick punch')
        while True:
            try:
                action = input("Choose an Ability: ")
                if action not in ['1', '2']:
                    raise ValueError("Invalid class choice")
                break
            except ValueError as ve:
                print(f"Error: {ve}. Please choose a valid number.")

        if action == "1":
            '''
            Ability: Daggers
            Description: Increases attack power and Strikes oppenents
            '''
            self.attack_power += 10
            opponent.health -= self.attack_power
            print(f"\n{self.name} uses Daggers which increases their attack power to {self.attack_power} and strickes {opponent.name}.")
        elif action == "2":
            '''
            Ability: Stealth Mode and Quick Punch
            Description: Stealth Mode increases their health and blows an attack.
            '''
            self.health += 5
            if self.health > self.max_health:
                self.health = self.max_health
            opponent.health -= self.attack_power            
            print(f'\n{self.name} goes into stealth mode which increase its health to {self.health} and delivers a quick punch for a damage of {self.attack_power}.')   



# * Creating a Rogue Class
class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, health = 110, attack_power = 30)
        
    # Each character gets two special abilities 
    def special_ability(self, opponent): 
        print('Select Special Ability')
        print('1. Increase Attack Power')
        print('2. Life Steal') 

        while True:
            try:
                action = input("Choose an Ability: ")
                if action not in ['1', '2']:
                    raise ValueError("Invalid class choice")
                break
            except ValueError as ve:
                print(f"Error: {ve}. Please choose a valid number.")
        if action == '1': 
            '''
            Ability: Increase Attack Power
            Description: Makes character much stronger!
            '''
            self.attack_power += 10
            print(f'{self.name} just got a whole lot stronger!! Attack power is now set to {self.attack_power}')
        elif action == '2':
            '''
            Ability: Life Steal
            Description: Attacks opponent by stealing health worth half of attackpower
            '''
            opponent.health -= self.attack_power
            self.health += self.attack_power // 2
            if self.health > self.max_health:
                self.health = self.max_health
            print(f"{self.name} uses Life Steal, and takes away {self.attack_power} health from {opponent.name}. Regenreating to {self.health} health")


# * EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5 
        if self.health > self.max_health:
            self.health = self.max_health 
        print(f"{self.name} regenerates 5 health! Wizard health: {self.health}")