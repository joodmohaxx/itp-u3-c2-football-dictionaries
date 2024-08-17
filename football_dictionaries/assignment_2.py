def players_by_position(squads_list):
    players_by_position={}
    for player in players:
        position = player['position']
        if position not in player_by_position:
            players_by_poeition[position] = []
        players_by_position[position].append(player)
    return players_by_position
        
