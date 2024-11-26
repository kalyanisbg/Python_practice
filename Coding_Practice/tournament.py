def tournament_winner(competitions, results):
    all_teams = []
    for element in competitions:
        for team in element:
            all_teams.append(team)
    teams = list(set(all_teams))
    team_dict = {}
    for team in teams:
        team_dict[team] = 0
    competitions_and_results = list(zip(competitions, results))
    for competition_and_result in competitions_and_results:
        if competition_and_result[0] == 0:
            team_dict[competition_and_result[1][0]] += 3
        else:
            team_dict[competition_and_result[1][1]] += 3
    scores = []
    for score in team_dict.items():
        scores.append(score)
    winner_score = max(scores)



