import random

class Character():
    pass

class Player():
    pass

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