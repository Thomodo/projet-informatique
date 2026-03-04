from function import *

class Player:
    def __init__(self, player_data_dict):
        self.player_data_dict = player_data_dict


    def update_player_data(self, player_data_dict):
        self.player_data_dict = player_data_dict


    def load_saved_player_data(self):
        self.player_data_dict = read_player_data()

    def save_player_data(self):
        write_data(self.player_data_dict, "player_data.json")

    def name_choose(self):
        self.player_data_dict["name"] = input("Veillez choisr votre nom: ")
        print("Vous vous appelez", self.player_data_dict["name"] + ".")
