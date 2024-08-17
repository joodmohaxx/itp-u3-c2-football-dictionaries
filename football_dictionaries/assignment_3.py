def players_by_country_and_position(squads_list):
  
    player_country = {}

    for player in players:
        country = player["country"]
        position = player["position"]
        player_country.setdefault(country, {})
        player_country[country].setdefault(position, [])
        player_country[country][position].append(player)
    return player_country
