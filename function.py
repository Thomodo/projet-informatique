import json
from ast import literal_eval

#file_name = player_data.json

def write_player_data(player_data_dict, file_name):
    with open(file_name, 'w') as json_file:
        json.dump(player_data_dict, json_file)

def read_file(file_name):
    with open(file_name, "r") as json_file:
        data = json.load(json_file)
        return data

def base_player_data():
    return read_file("base_player_data.json")

def base_player_data_dict():
    return {'max_health' : 100, 'attack_damage' : 20, 'crit_chance' : 0, 'crit_multiplier' : 2, 'money' : 0, 'actual_health' : 100,
            'xp' : 0, 'weapon_level' : 0, 'armor_level' : 0, 'name' : None}

def read_player_data():
    return read_file("player_data.json")


