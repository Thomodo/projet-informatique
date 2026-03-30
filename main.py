from function import *
from classe import *

### Initialisaton (on veut savoir si le joueur veut charger la sauvegarde)

ans = input("Voulez vous charger la sauvegarde ?\n"
            "'O' pour Oui, 'N' pour Non\n"
            "\n")
while ans not in ["O","N"]:
    ans = input("Vous devez répondre 'O' ou 'N'!\n")


if ans == "O": # Si la réponse est oui
    player = Player({})
    player.load_saved_player_data()
    print("Chargement de la sauvegarde")
else:
    player = Player({})
    create_new_save()
    player.load_saved_player_data()
    print("Création d'une nouvelle sauvegarde")
    player.name_choose()


### choisir ce qu'on fait

quit = False 

while quit != True :

    choice = input ("Que souhaitez vous faire ? \n" 
                "Pour accéder à votre boutique, entrez 'boutique'\n"
                "Pour effectuer un combat de boss, entrez 'boss'\n"
                "Pour effectuer un combat contre un monstre, entrez 'monstre' \n"
                "Pour quitter la partie , entrez 'quitter' \n"
                "\n")
    
    while choice not in [ "Boutique","boutique", "Boss", "boss","Monstre","monstre",' Quitter', 'quitter']:
        choice = input("Vous devez répondre soit par 'boutique' soit par  'boss'soit par  'monstre' ou par 'quitter'!\n")
        
    if choice in ["Boutique","boutique"]:
        print("Bienvenue dans la boutique" + str(player.player_data_dict["name"])+ " Vous avez nbr  Potion", "vous possédez", str(player.player_data_dict["money"]), "argent actuellement et vous êtes niveau", str(player.player_data_dict["level"]), "\n ")
        retour= False 
        while retour!= True:
            article= input("Pour acheter des potions, entrez 'potion' \n pour acheter des améliorations pour votre arme, entrez 'arme' \n pour acheter des améliorations pour votre armure, 'armure'")
            while article not in ["Armure","armure", "Potion", "potion","arme","arme"]:
                article = input("Vous devez répondre soit par 'armure' soit par 'potion' soit par 'arme'\n")


            if article in ["Armure","armure"]:
                armory=[{"protection point":0,"required level":0, "Price":0},{"protection point":5,"required level":10, "Price":5},
                        {"protection point":10,"required level":20, "Price":10},{"protection point":15,"required level":30, "Price":15},
                        {"protection point":20,"required level":40, "Price":20},{"protection point":25,"required level":50, "Price":25},
                        {"protection point":30,"required level":60, "Price":30},{"protection point":35,"required level":70, "Price":35},
                        {"protection point":40,"required level":80, "Price":40},{"protection point":45,"required level":90, "Price":45},
                        {"protection point":50,"required level":100, "Price":50}]
                mini = armory[0]["required level"]
                indice_mini=0
                for i in range(len(armory)):
                    if armory[i]["required level"] <= player.player_data_dict["level"]:
                        mini= armory[i]["required level"]
                        indice_mini=i
                if indice_mini != player.player_data_dict["armor_level"]:
                    decision= input(print("L'armure disponible pour votre niveau actuelle permet d'ajouté",armory[indice_mini]["required level"],"point de protection, son prix est de",armory[indice_mini]["Price"],"\n souhaitez vous l'acheté ?, 'O' pour Oui, 'N' pour Non\n"))
                    while decision not in ["O","o","N","n"]:
                        decision = input("Vous devez répondre 'O' ou 'N'!\n")
                    if decision in ["O","o"]:
                        if player.player_data_dict["money"] < armory[indice_mini]["Price"]:
                            print ("Vous n'avez pas assez d'argent pour acheter cet article, revenez quand vous aurez assez")
                            retour = True
                        else:
                            player.player_data_dict["money"]-=armory[indice_mini]["Price"]
                            player.player_data_dict["armor_level"] += 1
                            print("Félicitation " + player.player_data_dict["name"] + "vous venez d'obtenir une magnifique armure, votre argent maintenant à ", player.player_data_dict["money"])
                            retour = True
                    else:
                        retour = True
                else:
                    print("Vous ne pouvez pas acheter d'armure pour l'instant")
                    retour = True
            
            '''              
            if article in ["Potion","potion"]:
                potion=[{"life point":0,"required level":0, "Price":0},{"life point":5,"required level":10, "Price":5},
                        {"life point":10,"required level":20, "Price":10},{"life point":15,"required level":30, "Price":15},
                        {"life point":20,"required level":40, "Price":20},{"life point":25,"required level":50, "Price":25},
                        {"life point":30,"required level":60, "Price":30},{"life point":35,"required level":70, "Price":35},
                        {"life point":40,"required level":80, "Price":40},{"life point":45,"required level":90, "Price":45},
                        {"life point":50,"required level":100, "Price":50}]
                mini = potion[0]["required level"]
                indice_mini=0
                for i in range (len(potion)):
                    if potion[i]["required level"] <= player.player_data_dict["level"]:
                        mini= potion[i]["required level"]
                        indice_mini=i
                decision= input("La potion disponible pour votre niveau actuelle permet d'ajouté",potion[indice_mini]["required level"],"point de vie, son prix est de",potion[indice_mini]["Price"],"\n souhaitez vous l'acheté ?, 'O' pour Oui, 'N' pour Non\n")
                while decision not in ["O","o","N","n"]:
                    decision = input("Vous devez répondre 'O' ou 'N'!\n")
                    if decision in ["O","o"]:
                        if player.player_data_dict["money"] < potion[indice_mini]["Price"]:
                            print ("Vous n'avez pas assez d'argent pour acheter cet article, revenez quand vous aurez assez")
                        elif player.player_data_dict["potion"] < 3:
                            print ("Votre inventaire est déja plein")
                        else:
                            player.player_data_dict["argent"]-=potion[i]["Price"]
                            player.player_data_dict["potion"]+=1
                            print(" Félicitation" + player.player_data_dict["name"] + "vous venez d'obtenir une superbe potion, votre argent maintenant à ", player.player_data_dict["money"])
                    else:
                        retour= True
            '''

            if article in ["Arme","arme"]:
                wheapon=[{"damage attack":0,"required level":0, "Price":0},{"damage attack":5,"required level":10, "Price":5},
                        {"damage attack":10,"required level":20, "Price":10},{"damage attack":15,"required level":30, "Price":15},
                        {"damage attack":20,"required level":40, "Price":20},{"damage attack":25,"required level":50, "Price":25},
                        {"damage attack":30,"required level":60, "Price":30},{"damage attack":35,"required level":70, "Price":35},
                        {"damage attack":40,"required level":80, "Price":40},{"damage attack":45,"required level":90, "Price":45},
                        {"damage attack":50,"required level":100, "Price":50}]
                mini = wheapon[0]["required level"]
                indice_mini=0
                for i in range (len(wheapon)):
                    if wheapon[i]["required level"] <= player.player_data_dict["level"]:
                        mini= wheapon[i]["required level"]
                        indice_mini=i
                decision= input("L'arme disponible pour votre niveau actuelle permet de faire",wheapon[indice_mini]["required level"],"dégât,  son prix est de",wheapon[indice_mini]["Price"],"\n souhaitez vous l'acheté ?, 'O' pour Oui, 'N' pour Non\n")
                while decision not in ["O","o","N","n"]:
                    decision = input("Vous devez répondre 'O' ou 'N'!\n")
                    if decision in ["O","o"]:
                        if player.player_data_dict["money"] < wheapon[indice_mini]["Price"]:
                            print ("Vous n'avez pas assez d'argent pour acheter cet article, revenez quand vous aurez assez")
                        else:
                            player.player_data_dict["money"]-=wheapon[indice_mini]["Price"]
                            player.player_data_dict["amor"]+=1
                            print(" Félicitation" + player.player_data_dict["name"] + "vous venez d'obtenir une magnifique arme, votre argent est maintenant à ", player.player_data_dict["money"])
                    else:
                        retour= True
                  
                            
                   


    elif choice in ["Boss","boss"]:
        print("Vous vous appretez à effectuer un combat de boss")
            
    elif choice in ["Monstre","monstre"]:
        print("Vous vous appretez à affronter un monstre")
        
    elif choice in ["Quitter", "quitter"]:
        print("Vous allez quitter le jeu, votre jeu sera automatiquement sauvegarder")
        player.save_player_data()
        quit = True

