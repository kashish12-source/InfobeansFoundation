# 15. Cricket Team Management
# Problem

# Create player management system.

# Requirements

# Each player:

# name
# role
# runs scored
# Functionalities
# Update runs
# Display statistics
# Maintain total players
# Additional Challenge

# Find highest scorer among all players.



class Player:
    __total_players = 0
    __players = []

    def __init__(self, name, role, runs):
        self.__name = name
        self.__role = role
        self.__runs = runs

        Player.__total_players += 1
        Player.__players.append(self)

    def update_runs(self, runs):
        if runs >= 0:
            self.__runs += runs
            print("Runs updated successfully")
        else:
            print("Enter valid runs")

    def display_statistics(self):
        print("\nPlayer Name:", self.__name)
        print("Player Role:", self.__role)
        print("Runs Scored:", self.__runs)

    @classmethod
    def total_players(cls):
        print("\nTotal players:", cls.__total_players)

    @classmethod
    def highest_scorer(cls):
        if len(cls.__players) == 0:
            print("No players available")
            return

        highest = cls.__players[0]

        for player in cls.__players:
            if player.__runs > highest.__runs:
                highest = player

        print("\nHighest Scorer:", highest.__name)
        print("Runs Scored:", highest.__runs)



p1 = Player("Virat", "Batsman", 850)
p2 = Player("Rohit", "Batsman", 920)
p3 = Player("Bumrah", "Bowler", 150)
p4 = Player("Hardik", "All-rounder", 600)

p1.update_runs(200)
p3.update_runs(50)
p1.display_statistics()
p2.display_statistics()
p3.display_statistics()
p4.display_statistics()

Player.total_players()


Player.highest_scorer()
