def calculate_league_points(wins, draws, losses):
    win = wins * 4 
    draw = draws * 2
    loss = losses * -1
    return win + draw + loss

statistics = input().split(",")
wins = int(statistics[0])
draws = int(statistics[1])
losses = int(statistics[2])
print(calculate_league_points(wins, draws, losses))