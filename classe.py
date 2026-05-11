from function import *

class Player:
    def __init__(self, player_data_dict):
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

    def start_monster_fight(self):
        monster = Monster(self.player_data_dict)
        monster.load_monster_data(self)
        tour = 0
        commence = prob_calc(0.5)
        if commence:
            while self.player_data_dict['actual_health'] > 0 and monster.monster_data_dict['actual_health'] > 0:
                if tour % 2 == 0: #tour joueur
                    print('Vous êtes face à ', monster.monster_data_dict['name'], ',il lui reste ',monster.monster_data_dict['actual_health'], 'points de vie.')
                    ans = input(
                        "Voulez vous attaquer ce boss ou fuir comme un lache (Vous allez perdre 10% de votre argent) ou utiliser une potion ?\n"
                        "'B' pour se battre, 'F' pour fuir comme un lache, 'P' pour utiliser une potion et ensuite vous battre\n"
                        "\n")
                    while ans not in ["B", "F", "P"]:
                        ans = input("Vous devez répondre 'B' ou 'F' ou 'P'!\n")

                    if ans == "B":
                        damage = (self.player_data_dict["attack_damage"] *
                                  (1 + (self.player_data_dict["crit_multiplier"] - 1) * crit_work(
                                      self.player_data_dict["crit_chance"])))
                        monster.monster_data_dict['actual_health'] -= damage
                        print("Vous avez fait ", damage, " dégats au monstre")
                    elif ans == 'F':
                        loose = self.player_data_dict["money"] * 0.1
                        self.player_data_dict["money"] = self.player_data_dict["money"] * 0.9
                        self.player_data_dict['actual_health'] = 0
                        print('Vous êtes un lache, vous avez perdu ', loose, "$.")
                    else:
                        if self.player_data_dict['nb_health_potion'] != 0:
                            print("Vous avez actuellement ", self.player_data_dict["nb_health_potion"],
                                  " potions de vie de ", self.player_data_dict["health_potion_regen"],
                                  " point de vie.")
                            ans = input("Voulez vous utiliser une potion ?\n"
                                        "'O' pour Oui, 'N' pour Non\n"
                                        "\n")
                            while ans not in ["O", "N"]:
                                ans = input("Vous devez répondre 'O' ou 'N'!\n")
                            if ans == "O":  # Si la réponse est oui
                                self.player_data_dict['nb_health_potion'] -= 1
                                self.player_data_dict['actual_health'] += self.player_data_dict[
                                    'health_potion_regen']
                                print("Vous avez maintenant ", self.player_data_dict['actual_health'],
                                      " point de vie.")
                        else:
                            print("Vous n'avez pas de potion.")

                        damage = (self.player_data_dict["attack_damage"] *
                                  (1 + (self.player_data_dict["crit_multiplier"] - 1) * crit_work(
                                      self.player_data_dict["crit_chance"])))
                        monster.monster_data_dict['actual_health'] -= damage
                        print("Vous avez fait ", damage, " dégats au monstre")

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
                        "Voulez vous attaquer ce boss ou fuir comme un lache (Vous allez perdre 10% de votre argent) ou utiliser une potion ?\n"
                        "'B' pour se battre, 'F' pour fuir comme un lache, 'P' pour utiliser une potion et ensuite vous battre\n"
                        "\n")
                    while ans not in ["B", "F", "P"]:
                        ans = input("Vous devez répondre 'B' ou 'F' ou 'P'!\n")

                    if ans == "B":
                        damage = (self.player_data_dict["attack_damage"] *
                                  (1 + (self.player_data_dict["crit_multiplier"] - 1) * crit_work(
                                      self.player_data_dict["crit_chance"])))
                        monster.monster_data_dict['actual_health'] -= damage
                        print("Vous avez fait ", damage, " dégats au monstre")
                    elif ans == 'F':
                        loose = self.player_data_dict["money"] * 0.1
                        self.player_data_dict["money"] = self.player_data_dict["money"] * 0.9
                        self.player_data_dict['actual_health'] = 0
                        print('Vous êtes un lache, vous avez perdu ', loose, "$.")
                    else:
                        if self.player_data_dict['nb_health_potion'] != 0:
                            print("Vous avez actuellement ", self.player_data_dict["nb_health_potion"],
                                  " potions de vie de ", self.player_data_dict["health_potion_regen"],
                                  " point de vie.")
                            ans = input("Voulez vous utiliser une potion ?\n"
                                        "'O' pour Oui, 'N' pour Non\n"
                                        "\n")
                            while ans not in ["O", "N"]:
                                ans = input("Vous devez répondre 'O' ou 'N'!\n")
                            if ans == "O":  # Si la réponse est oui
                                self.player_data_dict['nb_health_potion'] -= 1
                                self.player_data_dict['actual_health'] += self.player_data_dict[
                                    'health_potion_regen']
                                print("Vous avez maintenant ", self.player_data_dict['actual_health'],
                                      " point de vie.")
                        else:
                            print("Vous n'avez pas de potion.")
                        damage = (self.player_data_dict["attack_damage"] *
                                  (1 + (self.player_data_dict["crit_multiplier"] - 1) * crit_work(
                                      self.player_data_dict["crit_chance"])))
                        monster.monster_data_dict['actual_health'] -= damage
                        print("Vous avez fait ", damage, " dégats au monstre")
                tour = tour + 1
        if self.player_data_dict['actual_health'] <= 0:
            print("Vous avez perdu !")
        else:
            self.player_data_dict['money'] += monster.monster_data_dict['money_reward']
            self.player_data_dict['xp'] += monster.monster_data_dict['xp_reward']
            print("Vous avez gagné !\n"
                  "En récompense vous recevez ", monster.monster_data_dict['money_reward'], ' $ et ', monster.monster_data_dict['xp_reward'], ' xp.')
            self.update_level()
        self.player_data_dict['actual_health'] = self.player_data_dict['max_health']

    def update_level(self):
        old_level = self.player_data_dict['level']
        current_level = xp_to_level(self.player_data_dict['xp'])
        if old_level < current_level:
            if current_level not in [6,11,16]:
                self.player_data_dict['level'] = current_level
                print('Félicitation, tu es passé niveau ', current_level, '.')
                self.update_crit_chance()
            else:
                print("Vous pourriez atteindre le niveau suivant mais vous devez déjà battre le boss avant.")

    def update_crit_chance(self):
        old_crit_chance = self.player_data_dict['crit_chance']
        level = self.player_data_dict['level']
        crit_chance = 0.02 * level
        if crit_chance > 1:
            crit_chance = 1
        self.player_data_dict['crit_chance'] = crit_chance
        if old_crit_chance < crit_chance:
            print("Vous avez atteint une probabilité de ", crit_chance, " de faire un coup critique.")

    def start_boss_fight(self):
        if self.player_data_dict['level'] % 5 != 0:
            print("Vous ne pouvez par combattre le boss vous devez être à un niveau multiple de 5, tu es trop nul pour le prochain boss.")
        else:
            boss = Boss(self.player_data_dict)
            boss.load_boss_data()

            tour = 0
            commence = prob_calc(0.5)
            if commence:
                while self.player_data_dict['actual_health'] > 0 and boss.boss_data_dict['actual_health'] > 0:
                    if tour % 2 == 0:  # tour joueur
                        print('Vous êtes face à ', boss.boss_data_dict['name'], ',il lui reste ',
                              boss.boss_data_dict['actual_health'], 'points de vie.')
                        ans = input(
                            "Voulez vous attaquer ce boss ou fuir comme un lache (Vous allez perdre 10% de votre argent) ou utiliser une potion ?\n"
                            "'B' pour se battre, 'F' pour fuir comme un lache, 'P' pour utiliser une potion et ensuite vous battre\n"
                            "\n")
                        while ans not in ["B", "F", "P"]:
                            ans = input("Vous devez répondre 'B' ou 'F' ou 'P'!\n")

                        if ans == "B":
                            damage = (self.player_data_dict["attack_damage"] *
                                      (1 + (self.player_data_dict["crit_multiplier"] - 1) * crit_work(
                                          self.player_data_dict["crit_chance"])))
                            boss.boss_data_dict['actual_health'] -= damage
                            print("Vous avez fait ", damage, " dégats au boss")
                        elif ans == 'F':
                            loose = self.player_data_dict["money"] * 0.1
                            self.player_data_dict["money"] = self.player_data_dict["money"] * 0.9
                            self.player_data_dict['actual_health'] = 0
                            print('Vous êtes un lache, vous avez perdu ', loose, "$.")
                        else:
                            if self.player_data_dict['nb_health_potion'] != 0:
                                print("Vous avez actuellement ", self.player_data_dict["nb_health_potion"], " potions de vie de ", self.player_data_dict["health_potion_regen"], " point de vie.")
                                ans = input("Voulez vous utiliser une potion ?\n"
                                            "'O' pour Oui, 'N' pour Non\n"
                                            "\n")
                                while ans not in ["O", "N"]:
                                    ans = input("Vous devez répondre 'O' ou 'N'!\n")
                                if ans == "O":  # Si la réponse est oui
                                    self.player_data_dict['nb_health_potion'] -= 1
                                    self.player_data_dict['actual_health'] += self.player_data_dict['health_potion_regen']
                                    print("Vous avez maintenant ", self.player_data_dict['actual_health'], " point de vie.")
                            else:
                                print("Vous n'avez pas de potion.")
                            damage = (self.player_data_dict["attack_damage"] *
                                      (1 + (self.player_data_dict["crit_multiplier"] - 1) * crit_work(
                                          self.player_data_dict["crit_chance"])))
                            boss.boss_data_dict['actual_health'] -= damage
                            print("Vous avez fait ", damage, " dégats au boss")

                    else:  # tour boss
                        damage = (boss.boss_data_dict["attack_damage"] *
                                  (1 + (boss.boss_data_dict["crit_multiplier"] - 1) * crit_work(
                                      boss.boss_data_dict["crit_chance"])))
                        self.player_data_dict['actual_health'] -= damage
                        print(boss.boss_data_dict['name'], ' vous a fait ', damage
                              , ' point de dégats, il vous reste ', self.player_data_dict['actual_health'],
                              ' points de vie.')
                    tour = tour + 1
            else:
                while self.player_data_dict['actual_health'] > 0 and boss.boss_data_dict['actual_health'] > 0:
                    if tour % 2 == 0:  # tour boss
                        damage = (boss.boss_data_dict["attack_damage"] *
                                  (1 + (boss.boss_data_dict["crit_multiplier"] - 1) * crit_work(
                                      boss.boss_data_dict["crit_chance"])))
                        self.player_data_dict['actual_health'] -= damage
                        print(boss.boss_data_dict['name'], ' vous a fait ', damage
                              , ' point de dégats, il vous reste ', self.player_data_dict['actual_health'],
                              ' points de vie.')

                    else:  # tour joueur
                        print('Vous êtes face à ', boss.boss_data_dict['name'], ',il lui reste ',
                              boss.boss_data_dict['actual_health'], 'points de vie.')
                        ans = input(
                            "Voulez vous attaquer ce boss ou fuir comme un lache (Vous allez perdre 10% de votre argent) ou utiliser une potion ?\n"
                            "'B' pour se battre, 'F' pour fuir comme un lache, 'P' pour utiliser une potion et ensuite vous battre\n"
                            "\n")
                        while ans not in ["B", "F", "P"]:
                            ans = input("Vous devez répondre 'B' ou 'F' ou 'P'!\n")

                        if ans == "B":
                            damage = (self.player_data_dict["attack_damage"] *
                                      (1 + (self.player_data_dict["crit_multiplier"] - 1) * crit_work(
                                          self.player_data_dict["crit_chance"])))
                            boss.boss_data_dict['actual_health'] -= damage
                            print("Vous avez fait ", damage, " dégats au boss")
                        elif ans == 'F':
                            loose = self.player_data_dict["money"] * 0.1
                            self.player_data_dict["money"] = self.player_data_dict["money"] * 0.9
                            self.player_data_dict['actual_health'] = 0
                            print('Vous êtes un lache, vous avez perdu ', loose, "$.")
                        else:
                            if self.player_data_dict['nb_health_potion'] != 0:
                                print("Vous avez actuellement ", self.player_data_dict["nb_health_potion"],
                                      " potions de vie de ", self.player_data_dict["health_potion_regen"],
                                      " point de vie.")
                                ans = input("Voulez vous utiliser une potion ?\n"
                                            "'O' pour Oui, 'N' pour Non\n"
                                            "\n")
                                while ans not in ["O", "N"]:
                                    ans = input("Vous devez répondre 'O' ou 'N'!\n")
                                if ans == "O":  # Si la réponse est oui
                                    self.player_data_dict['nb_health_potion'] -= 1
                                    self.player_data_dict['actual_health'] += self.player_data_dict[
                                        'health_potion_regen']
                                    print("Vous avez maintenant ", self.player_data_dict['actual_health'],
                                          " point de vie.")
                            else:
                                print("Vous n'avez pas de potion.")
                            damage = (self.player_data_dict["attack_damage"] *
                                      (1 + (self.player_data_dict["crit_multiplier"] - 1) * crit_work(
                                          self.player_data_dict["crit_chance"])))
                            boss.boss_data_dict['actual_health'] -= damage
                            print("Vous avez fait ", damage, " dégats au boss")
                    tour = tour + 1
            if self.player_data_dict['actual_health'] <= 0:
                print("Vous avez perdu !")
            else:
                self.player_data_dict['money'] += boss.boss_data_dict['money_reward']
                self.player_data_dict['xp'] += boss.boss_data_dict['xp_reward']
                print("Vous avez gagné !\n"
                      "En récompense vous recevez ", boss.boss_data_dict['money_reward'], ' $ et ',
                      boss.boss_data_dict['xp_reward'], ' xp.')
                self.player_data_dict['level'] += 1
                print('Félicitation, tu es passé niveau ', self.player_data_dict['level'], '.')
                self.player_data_dict["xp"] = level_to_xp(self.player_data_dict["level"])
                self.update_crit_chance()
                if self.player_data_dict['level'] == 6:
                    self.player_data_dict["health_potion_regen"] = 75
                elif self.player_data_dict['level'] == 11:
                    self.player_data_dict["health_potion_regen"] = 100
                elif self.player_data_dict['level'] == 16:
                    self.player_data_dict["health_potion_regen"] = 150
            self.player_data_dict['actual_health'] = self.player_data_dict['max_health']

class Monster:
    def __init__(self, player_data_dict):
        self.player_data_dict = player_data_dict

    def load_monster_data(self, player):
        self.monster_data_dict = monster_choose(player.player_data_dict["level"])

class Boss:
    def __init__(self, player_data_dict):
        self.player_data_dict = player_data_dict

    def load_boss_data(self):
        self.boss_data_dict = boss_choose(self.player_data_dict["level"])
