import json
from random import uniform
from ast import literal_eval


def write_data(data, file_name):
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file)

def read_file(file_name):
    with open(file_name, "r") as json_file:
        data = json.load(json_file)
        return data

def base_player_data_dict():
    return {'max_health' : 100, 'attack_damage' : 20, 'crit_chance' : 0, 'crit_multiplier' : 2, 'money' : 0, 'actual_health' : 100,
            'xp' : 0, 'weapon_level' : 0, 'armor_level' : 0, 'name' : None, 'level' : 1, 'nb_health_potion' : 0, "health_potion_regen" : 0}

def read_player_data():
    return read_file("player_data.json")

def create_new_save():
    write_data(base_player_data_dict(), "player_data.json")

def monster_data_dict():
    return {1: [({'max_health': 100, 'attack_damage': 10, 'crit_chance': 0, 'crit_multiplier': 2, 'money_reward': 10,
                  'actual_health': 100,'xp_reward': 10, 'name': "Michel_killeur"},1)],
            2: [({'max_health': 100, 'attack_damage': 12, 'crit_chance': 0, 'crit_multiplier': 2, 'money_reward': 20,
                  'actual_health': 100, 'xp_reward': 20, 'name': "Bob_le_bricoleur"}, 1)],
            3: [({'max_health': 100, 'attack_damage': 15, 'crit_chance': 0, 'crit_multiplier': 2, 'money_reward': 30,
                  'actual_health': 100, 'xp_reward': 25, 'name': "Mathilde"}, 1)],
            4: [({'max_health': 100, 'attack_damage': 17, 'crit_chance': 0, 'crit_multiplier': 2, 'money_reward': 40,
                  'actual_health': 100, 'xp_reward': 30, 'name': "Passe_partout"}, 1)],
            5: [({'max_health': 100, 'attack_damage': 20, 'crit_chance': 0, 'crit_multiplier': 2, 'money_reward': 100,
                  'actual_health': 100, 'xp_reward': 35, 'name': "Jacques_Chirac"}, 1)],
            6: [({'max_health': 125, 'attack_damage': 20, 'crit_chance': 0, 'crit_multiplier': 2, 'money_reward': 200,
                  'actual_health': 125, 'xp_reward': 40, 'name': "Macron"}, 1)],
            7: [({'max_health': 150, 'attack_damage': 20, 'crit_chance': 0, 'crit_multiplier': 2, 'money_reward': 300,
                  'actual_health': 150, 'xp_reward': 45, 'name': "Jules_césar"}, 1)],
            8: [({'max_health': 150, 'attack_damage': 23, 'crit_chance': 0, 'crit_multiplier': 2, 'money_reward': 400,
                  'actual_health': 150, 'xp_reward': 50, 'name': "Ramtin"}, 1)],
            9: [({'max_health': 150, 'attack_damage': 26, 'crit_chance': 0, 'crit_multiplier': 2, 'money_reward': 500,
                  'actual_health': 150, 'xp_reward': 60, 'name': "Mimie_mathie"}, 1)],
            10: [({'max_health': 150, 'attack_damage': 30, 'crit_chance': 0, 'crit_multiplier': 2, 'money_reward': 1000,
                  'actual_health': 150, 'xp_reward': 70, 'name': "Thomas_le_grand"}, 1)],
            11: [({'max_health': 175, 'attack_damage': 30, 'crit_chance': 0, 'crit_multiplier': 2, 'money_reward': 2000,
                  'actual_health': 175, 'xp_reward': 75, 'name': "Le_facteur"}, 1)],
            12: [({'max_health': 200, 'attack_damage': 30, 'crit_chance': 0, 'crit_multiplier': 2, 'money_reward': 3000,
                  'actual_health': 200, 'xp_reward': 80, 'name': "Patrick_Sebastien"}, 1)],
            13: [({'max_health': 200, 'attack_damage': 40, 'crit_chance': 0, 'crit_multiplier': 2, 'money_reward': 4000,
                  'actual_health': 200, 'xp_reward': 85, 'name': "La_serviette"}, 1)],
            14: [({'max_health': 200, 'attack_damage': 50, 'crit_chance': 0, 'crit_multiplier': 2, 'money_reward': 5000,
                  'actual_health': 200, 'xp_reward': 90, 'name': "La_chaise_à_trois_pattes"}, 1)],
            15: [({'max_health': 250, 'attack_damage': 60, 'crit_chance': 0, 'crit_multiplier': 2, 'money_reward': 10000,
                  'actual_health': 250, 'xp_reward': 100, 'name': "Le_Dézingueur"}, 1)],
            16: [({'max_health': 350, 'attack_damage': 80, 'crit_chance': 0, 'crit_multiplier': 2, 'money_reward': 20000,
                   'actual_health': 350, 'xp_reward': 115, 'name': "Napoléon"}, 1)]
            }

def xp_to_level(xp):
    level_tab = [0,0,10,50,100,200,300,450,600,750,1000,1250,1600,2000,2500,3500,5000]
    for i in range(len(level_tab)):
        if xp < level_tab[i]:
            return i-1
    else:
        return len(level_tab) - 1

def level_to_xp(level):
    level_tab = [0,0,10,50,100,200,300,450,600,750,1000,1250,1600,2000,2500,3500,5000]
    return level_tab[level]

def monster_choose(level):
    liste_1 = monster_data_dict()
    liste = liste_1[level]
    rng_number = uniform(0,1)
    current = 0
    for elt in liste:
        if current <= rng_number and rng_number <= current + elt[1]:
            return elt[0]
        else:
            current = current + elt[1]


def crit_work(crit_chance):
    rng_number = uniform(0, 1)
    if rng_number <= crit_chance:
        return 1
    else:
        return 0

def prob_calc(prob):
    rng_number = uniform(0, 1)
    if rng_number <= prob:
        return True
    else:
        return False

def boss_choose(level):
    boss_data_dict_level = [{'max_health': 100, 'attack_damage': 20, 'crit_chance': 0, 'crit_multiplier': 2, 'money_reward': 100,
                  'actual_health': 100, 'xp_reward': 35, 'name': "Jacques_Chirac_le_Boss"},
                            {'max_health': 150, 'attack_damage': 30, 'crit_chance': 0, 'crit_multiplier': 2, 'money_reward': 1000,
                  'actual_health': 150, 'xp_reward': 70, 'name': "Thomas_le_grand_le_Boss"},
                            {'max_health': 250, 'attack_damage': 60, 'crit_chance': 0, 'crit_multiplier': 2, 'money_reward': 10000,
                  'actual_health': 250, 'xp_reward': 100, 'name': "Le_Dézingueur_le_Boss"}]
    return boss_data_dict_level[int((level/5)-1)]