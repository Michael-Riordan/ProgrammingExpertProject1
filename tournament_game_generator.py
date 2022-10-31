
num_teams = input("Enter the number of teams in the tournament: ")

while int(num_teams) < 2:
    print("The minimum number of teams is 2, try again.")
    num_teams = input("Enter the number of teams in the tournament: ")

teams = []
for i in range(1, int(num_teams) + 1):
        team = input(f"Enter the name for team #{i}: ")

        while len(team.split(" ")) > 2 or len(team) < 2:
            if len(team.split(" ")) > 2:
                print("Team names must have at most 2 words, try again.")
            if len(team) < 2:
                print("Team names must have at least 2 characters, try again.")
            team = input(f"Enter the name for team #{i}: ")

        teams.append(team)
            
num_of_games_played = input("Enter the number of games played by each team: ")

while int(num_of_games_played) < len(teams) - 1:
    print("Each team plays each other at least once in the regular season, try again.")
    num_of_games_played = input("Enter the number of games played by each team: ")

team_wins = {}
for i, team_name in enumerate(teams):
    number_of_wins = input(f"Enter the number of wins Team {teams[i]} had: ")
    while int(number_of_wins) < 0 or int(number_of_wins) > int(num_of_games_played):
        if int(number_of_wins) < 0:
            print("The minimum number of wins is 0, try again.")
        if int(number_of_wins) > int(num_of_games_played):
            print(f"The maximum number of wins is {num_of_games_played}, try again.")
        number_of_wins = input(f"Enter the number of wins Team {teams[i]} had: ")
        

    team_wins[team_name] = team_wins.get(team_name, int(number_of_wins))

print("Generating the games to be played in the first round of the tournament...")

sorted_teams = sorted(team_wins, key=team_wins.get)


while len(sorted_teams) > 0:
    home_team = sorted_teams[0]
    away_team = sorted_teams[-1]
    print(f"Home: {home_team} VS Away: {away_team}")
    sorted_teams.remove(home_team)
    sorted_teams.remove(away_team)



    
