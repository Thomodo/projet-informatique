import json
from ast import literal_eval


def write_data(data, file_name):
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file)

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

def create_new_save():
    write_data(base_player_data_dict(), "player_data.json")



#write_data(base_player_data_dict(), "base_player_data.json")