def players_as_dictionaries(squads_list):
    keys = [ 'number','position','name','date_of_birth','caps','club','country','clup_country','year']
    players=[]
    for player in squads_list:
        player_dict=dict(zip(keys,player_list))
        players.append(player_dict)
    return players
                         


