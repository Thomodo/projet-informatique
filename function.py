import json
from ast import literal_eval

file_name = player_data.json

def write_player_data (player_data_dict, file_name):
    with open(file_name, 'w') as json_file:
        json.dump(player_data_dict, json_file)

def read_player_data (file_name):
    with open(file_name, "r") as json_file:
        player_data_dict = json.load(json_file)
        return player_data_dict