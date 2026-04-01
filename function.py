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
            'xp' : 0, 'weapon_level' : 0, 'armor_level' : 0, 'name' : None, 'level' : 1, ' health_potion' : 0}

def read_player_data():
    return read_file("player_data.json")

def create_new_save():
    write_data(base_player_data_dict(), "player_data.json")

def monster_data_dict():
    return {1 : [({'max_health' : 100, 'attack_damage' : 10, 'crit_chance' : 0, 'crit_multiplier' : 2, 'money_reward' : 10,
                  'actual_health' : 100,'xp_reward' : 15, 'name' : "Michel_killeur"},1)]}

def xp_to_level(xp):
    level_tab = [0,0,10,50,100,500,1000,5000,10000,50000,100000]
    for i in range(len(level_tab)):
        if xp < level_tab[i]:
            return i-1
    else:
        return len(level_tab) - 1

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

