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

    def name_choose(self):
        self.player_data_dict["name"] = input("Veillez choisr votre nom: ")
        print("Vous vous appelez", self.player_data_dict["name"] + ".")

    def level_update(self):
        self.player_data_dict["level"] = xp_to_level(self.player_data_dict["xp"])

    def start_monster_fight(self):
        monster = Monster(self.player_data_dict)
        monster.load_monster_data(self)
        tour = 0
        commence = prob_calc(0.5)
        if commence:
            while self.player_data_dict['actual_health'] > 0 and monster.monster_data_dict['actual_health'] > 0:
                if tour % 2 == 0: #tour joueur
                    print('Vous êtes face à ', monster.monster_data_dict['name'], ',il lui reste ',monster.monster_data_dict['actual_health'], 'points de vie.')
                    ans = input("Voulez vous attaquer ce monstre ou fuir comme un lache (Vous allez perdre 10% de votre argent) ?\n"
                                "'B' pour se battre, 'F' pour fuir comme un lache\n"
                                "\n")
                    while ans not in ["B", "F"]:
                        ans = input("Vous devez répondre 'B' ou 'F'!\n")

                    if ans == "B":  # Si la réponse est oui
                        damage = (self.player_data_dict["attack_damage"] *
                                        (1 + (self.player_data_dict["crit_multiplier"] - 1)*crit_work(self.player_data_dict["crit_chance"])))
                        monster.monster_data_dict['actual_health'] -= damage
                        print("Vous avez fait ", damage, " dégats au monstre")
                    else:
                        self.player_data_dict["money"] = self.player_data_dict["money"] * 0.9
                        self.player_data_dict['actual_health'] = 0
                        print('Vous êtes un lache, vous avez perdu ', self.player_data_dict["money"], "$.")

                else: # tour monstre
                    damage = (monster.monster_data_dict["attack_damage"] *
                                        (1 + (monster.monster_data_dict["crit_multiplier"] - 1)*crit_work(monster.monster_data_dict["crit_chance"])))
                    self.player_data_dict['actual_health'] -= damage
                    print(monster.monster_data_dict['name'], ' vous a fait ', damage
                          , ' point de dégats, il vous reste ', self.player_data_dict['actual_health'], ' points de vie.')
                tour = tour + 1
        else:
            while self.player_data_dict['actual_health'] > 0 and monster.monster_data_dict['actual_health'] > 0:
                if tour % 2 == 0: #tour monstre
                    damage = (monster.monster_data_dict["attack_damage"] *
                              (1 + (monster.monster_data_dict["crit_multiplier"] - 1) * crit_work(
                                  monster.monster_data_dict["crit_chance"])))
                    self.player_data_dict['actual_health'] -= damage
                    print(monster.monster_data_dict['name'], ' vous a fait ', damage
                          , ' point de dégats, il vous reste ', self.player_data_dict['actual_health'],
                          ' points de vie.')

                else: # tour joueur
                    print('Vous êtes face à ', monster.monster_data_dict['name'], ',il lui reste ',
                          monster.monster_data_dict['actual_health'], 'points de vie.')
                    ans = input(
                        "Voulez vous attaquer ce monstre ou fuir comme un lache (Vous allez perdre 10% de votre argent) ?\n"
                        "'B' pour se battre, 'F' pour fuir comme un lache\n"
                        "\n")
                    while ans not in ["B", "F"]:
                        ans = input("Vous devez répondre 'B' ou 'F'!\n")

                    if ans == "B":  # Si la réponse est oui
                        damage = (self.player_data_dict["attack_damage"] *
                                  (1 + (self.player_data_dict["crit_multiplier"] - 1) * crit_work(
                                      self.player_data_dict["crit_chance"])))
                        monster.monster_data_dict['actual_health'] -= damage
                        print("Vous avez fait ", damage, " dégats au monstre")
                    else:
                        loose = self.player_data_dict["money"] * 0.1
                        self.player_data_dict["money"] = self.player_data_dict["money"] * 0.9
                        self.player_data_dict['actual_health'] = 0
                        print('Vous êtes un lache, vous avez perdu ', loose, "$.")
                tour = tour + 1
        if self.player_data_dict['actual_health'] <= 0:
            print("Vous avez perdu !")
        else:
            self.player_data_dict['money'] += monster.monster_data_dict['money_reward']
            self.player_data_dict['xp'] += monster.monster_data_dict['xp_reward']
            print("Vous avez gagné !\n"
                  "En récompense vous recevez ", monster.monster_data_dict['money_reward'], ' $ et ', monster.monster_data_dict['xp_reward'], ' xp.')
        self.player_data_dict['actual_health'] = self.player_data_dict['max_health']

class Monster:
    def __init__(self, player_data_dict):
        self.player_data_dict = player_data_dict

    def load_monster_data(self, player):
        self.monster_data_dict = monster_choose(player.player_data_dict["level"])

