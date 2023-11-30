import random

class Character():
    def __init__(self, name):
        self.name = name

    def battle(self, target, player, computer):
        outcomes = {"Warrior": "Mage", "Mage": "Archer", "Archer": "Warrior"}
        if self.name == target.name:
            print(f"{self.name} attacks {target.name}! You both live to fight another day!")
        elif outcomes[self.name] == target.name:
            print(f"{self.name} attacks {target.name}! {self.name} is victorious!")
            player.increase_score()
        else:
            print(f"{self.name} attacks {target.name}! {target.name} is victorious!")
            computer.increase_score()

class Player():
    def __init__(self, name):
        self.name = name
        self.character = None
        self.score = 0

    def select_character(self):
        print("Choose your character!")
        print("1. Warrior")
        print("2. Mage")
        print("3. Archer")
        choice = input("Choose 1, 2, or 3: ")
        if choice == "1":
            self.character = Character("Warrior")
        elif choice == "2":
            self.character = Character("Mage")
        elif choice == "3":
            self.character = Character("Archer")
        else:
            print("Invalid choice!")

    def random_character(self):
            self.character = random.choice([Character("Warrior"), Character("Mage"), Character("Archer")])

    def introduce_character(self):
            print(f"{self.name} is {self.character.name}!")

    def increase_score(self):
        self.score += 1

class Game():
    def __init__(self):
        self.player_one = Player(input("What is your name? "))
        self.player_two = Player("Computer")
        self.game_running = True
        self.rounds = 1

    def play_again(self):
        play_again = input("Play again? (y/n) ").lower()
        if play_again == "y":
            self.rounds += 1
            self.player_one.character = None
            self.player_two.character = None
        else:
            self.game_running = False
            self.announce_winner()

    def announce_score(self):
        print(f"After {self.rounds} rounds, here are the scores:")
        print(f"{self.player_one.name}: {self.player_one.score} | Computer: {self.player_two.score}")

    def announce_winner(self):
        print(f"Thanks for playing! After {self.rounds} rounds:")
        if self.player_one.score > self.player_two.score:
            print(f"{self.player_one.name} is the winner!")
        elif self.player_one.score < self.player_two.score:
            print("Computer is the winner!")
        else:
            print("It's a tie!")
        
    def play(self):
        print(f"Welcome to the Legends Unleashed, {self.player_one.name}!")
        while self.game_running:
            self.player_one.select_character()
            self.player_one.introduce_character()
            self.player_two.random_character()
            self.player_two.introduce_character()
            self.player_one.character.battle(self.player_two.character, self.player_one, self.player_two)
            self.announce_score()
            self.play_again()
            
my_game = Game()
my_game.play()