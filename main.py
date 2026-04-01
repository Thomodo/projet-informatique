from function import *
from classe import *

### Initialisaton (on veut savoir si le joueur veut charger la sauvegarde)

ans = input("Voulez vous charger la sauvegarde ?\n"
            "'O' pour Oui, 'N' pour Non\n"
            "\n")
while ans not in ["O","N"]:
    ans = input("Vous devez répondre 'O' ou 'N'!\n")


if ans == "O": # Si la réponse est oui, une sauvegarde se fait
    player = Player({})
    player.load_saved_player_data()
    print("Chargement de la sauvegarde")
else: # Sinon un nouveau fichier est crée et va remplacer l'ancien
    player = Player({})
    create_new_save()
    player.load_saved_player_data()
    print("Création d'une nouvelle sauvegarde")
    player.name_choose()


### choisir ce qu'on fait

quit = False 
skip_exp= True
while quit != True : # Tant que le joueur ne souhaite pas quitter la partie le code continue
    if skip_exp != True:
        asw = input(" Bienvenue dans Pyplot the Game !!! Souhaitez - vous connaître le fonctionnement du jeu ? Faite 'O' pour Oui et 'N' pour non  ")
        while choice not in [ "O","o", "N", "n"]:
            asw = input("Vous devez répondre soit par 'O' soit par 'N !\n")
            if asw in ["O","o"]:
                asw1=input( " Le but de Pyplot the Game est un de combattre le boss final ! \n Pour connaître le fonctionnement des combats, entrez 'Combat' \n " 
                "Pour savoir comment obtenir de l'argent, entrez : 'argent' \n "
                " Pour savoir comment obtenir de l'expérience, entrez :'xp'\n"
                "Pour connaitre le fonctionnement de la boutique, entrez: 'boutique'"
                "Pour quitter, entrez 'quitter")
                
                if asw1 not in ["Argent","argent","Combat","combat","Xp","xp","Boutique","boutique","Quitter","quitter"]:
                    aws1=input( "Veuillez ecrire 'Combat', 'Argent', ' Xp',' Boutique' ou 'Quitter' " )

                    if asw1 in ['Combat','combat']:
                        print(" Il existe deux types de combat possible qui se base sur le fonctionnement du tour par tour. \n"
                              " Vous affronterez soit un monstre qui aura une difficulté proportionnelle à votre niveau soit un boss qui aura une diffulculté plus importante tout les 5 niveaux")
                        
                    if asw1 in ['Argent','argent']:
                        print("Pour avoir de l'argent, il suffit d'affronter un monstre mais attention si au cours du combat vous décidez de fuir " \
                        "alors vous perderez 10% de votre argent actuelle. Réflichissez donc bien avant d'en entamer un.") 
        
                    if asw1 in ["Xp",'xp']:
                        print( " Pour gagner de l'expérience, il suffit d'effectuer des combats de monstres s'il vous reussissez à les vaincre alors vous pourrez gagner de l'expérience")
                    
                    if asw1 in [ "Boutique","boutique"]:
                        print("La boutique sert à acheter différents items qui vous aideront dans les combats. Les items ont une efficacité proportionnelle à votre niveau actuelle \n"
                              " Vous pourrez acheter des potions qui vous permettront d'augmenter votre vie\n"
                              , " des armures pour vous proteger et des armes pour infliger d'avantage de dégât lors des combats.\n")
                    if asw1 in ["Quitter", "quitter"]:
                        skip_exp =  True
                        
    choice = input ("Que souhaitez vous faire ? \n" 
                "Pour accéder à votre boutique, entrez 'boutique'\n"
                "Pour effectuer un combat de boss, entrez 'boss'\n"
                "Pour effectuer un combat contre un monstre, entrez 'monstre' \n"
                "Pour quitter la partie , entrez 'quitter' \n"
                "\n")
    
    while choice not in [ "Boutique","boutique", "Boss", "boss","Monstre","monstre",' Quitter', 'quitter']:
        choice = input("Vous devez répondre soit par 'boutique' soit par  'boss'soit par  'monstre' ou par 'quitter'!\n")
        
    if choice in ["Boutique","boutique"]:
        print("Bienvenue dans la boutique " + str(player.player_data_dict["name"]) + " Vous avez nbr  Potion vous possédez " + str(player.player_data_dict["money"]) +  " argent actuellement et vous êtes niveau " + str(player.player_data_dict["level"]) + "\n ")
        retour= False 
        while retour!= True:# Tant que le joueur ne souhaite pas quitter la boutique, le choix entre acheter des objets et quitter la boutique continue 
            article= input("Pour acheter des potions, entrez 'potion' \n pour acheter des améliorations pour votre arme, entrez 'arme' \n pour acheter des améliorations pour votre armure, 'armure' \n et pour quitter la boutique, entrez ' Quitter' ")
            while article not in ["Armure","armure", "Potion", "potion","arme","arme", " Quitter", "quitter"]:
                article = input("Vous devez répondre soit par 'armure' soit par 'potion' soit par 'arme' ou ' quitter '\n")

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
                    if armory[i]["required level"] <= player.player_data_dict["level"]: # Sert à determiner quelle armure est disponible pour le joueur en fonction de son niveau actuel
                        mini= armory[i]["required level"]
                        indice_mini=i
                if indice_mini != player.player_data_dict["armor_level"]: # Si l'armure disponible est differente de celle que le joueur possède alors il peut l'acheter s'il le souhaite.
                    decision= input(print("L'armure disponible pour votre niveau actuelle permet d'ajouté",armory[indice_mini]["required level"],"point de protection, son prix est de",armory[indice_mini]["Price"],"\n souhaitez vous l'acheté ?, 'O' pour Oui, 'N' pour Non\n"))
                    while decision not in ["O","o","N","n"]:
                        decision = input("Vous devez répondre 'O' ou 'N'!\n")
                    if decision in ["O","o"]:
                        if player.player_data_dict["money"] < armory[indice_mini]["Price"]:
                            print ("Vous n'avez pas assez d'argent pour acheter cet article, revenez quand vous aurez assez")
                        else:
                            player.player_data_dict["money"]-=armory[indice_mini]["Price"]
                            player.player_data_dict["armor_level"] += 1
                            print("Félicitation " + player.player_data_dict["name"] + "vous venez d'obtenir une magnifique armure, votre argent maintenant à " +  player.player_data_dict["money"])
                    else:
                        retour = True
                else:
                    print("Vous ne pouvez pas acheter d'armure pour l'instant car vous posséder déjà celle disponible à votre niveau, continuer à combattre des monstres pour accéder à l'armure suivante")
                     
            if article in ["Potion","potion"]:
                potion=[{"life point":0,"required level":0, "Price":0},{"life point":5,"required level":10, "Price":5},
                        {"life point":10,"required level":20, "Price":10},{"life point":15,"required level":30, "Price":15},
                        {"life point":20,"required level":40, "Price":20},{"life point":25,"required level":50, "Price":25},
                        {"life point":30,"required level":60, "Price":30},{"life point":35,"required level":70, "Price":35},
                        {"life point":40,"required level":80, "Price":40},{"life point":45,"required level":90, "Price":45},
                        {"life point":50,"required level":100, "Price":50}]
                mini = potion[0]["required level"]
                indice_mini=0
                for i in range(len(potion)):
                    if potion[i]["required level"] <= player.player_data_dict["level"]:
                        mini= potion[i]["required level"]
                        indice_mini=i
                if indice_mini != player.player_data_dict["level"]:
                    decision= input(print("La potion disponible pour votre niveau actuelle permet d'ajouté "+ potion[indice_mini]["required level"] + "point de vie, son prix est de " + potion[indice_mini]["Price"] + "\n souhaitez vous l'acheté ?, 'O' pour Oui, 'N' pour Non\n"))
                    while decision not in ["O","o","N","n"]:
                        decision = input("Vous devez répondre 'O' ou 'N'!\n")
                    if decision in ["O","o"]:
                        if player.player_data_dict["money"] < potion[indice_mini]["Price"]:
                            print ("Vous n'avez pas assez d'argent pour acheter cet article, revenez quand vous aurez assez")
                        else:
                            player.player_data_dict["money"]-=potion[indice_mini]["Price"]
                            player.player_data_dict["health_potion"] += 1
                            print("Félicitation " + player.player_data_dict["name"] + "vous venez d'obtenir une potion qui vous permettra de vous rajouter de la vie supplémentaire, votre argent est maintenant à " +  player.player_data_dict["money"])
                    else:
                        retour = True
                else:
                    print("Vous ne pouvez pas acheter de potion pour l'instant, continuer à combattre des monstres")
        

            if article in ["Arme","arme"]:
                weapon=[{"damage attack":0,"required level":0, "Price":0},{"damage attack":5,"required level":10, "Price":5},
                        {"damage attack":10,"required level":20, "Price":10},{"damage attack":15,"required level":30, "Price":15},
                        {"damage attack":20,"required level":40, "Price":20},{"damage attack":25,"required level":50, "Price":25},
                        {"damage attack":30,"required level":60, "Price":30},{"damage attack":35,"required level":70, "Price":35},
                        {"damage attack":40,"required level":80, "Price":40},{"damage attack":45,"required level":90, "Price":45},
                        {"damage attack":50,"required level":100, "Price":50}]
                mini = weapon[0]["required level"]
                indice_mini=0
                for i in range(len(weapon)):
                    if weapon[i]["required level"] <= player.player_data_dict["level"]:
                        mini= weapon[i]["required level"]
                        indice_mini=i
                if indice_mini != player.player_data_dict["weapon_level"]:
                    decision= input(print("L'arme disponible pour votre niveau actuelle permet de faire "+ weapon[indice_mini]["required level"],"dégat à votre adversaire, son prix est de" + weapon[indice_mini]["Price"] +"\n souhaitez vous l'acheté ?, 'O' pour Oui, 'N' pour Non\n"))
                    while decision not in ["O","o","N","n"]:
                        decision = input("Vous devez répondre 'O' ou 'N'!\n")
                    if decision in ["O","o"]:
                        if player.player_data_dict["money"] < weapon[indice_mini]["Price"]:
                            print ("Vous n'avez pas assez d'argent pour acheter cet article, revenez quand vous aurez assez")
                        else:
                            player.player_data_dict["money"]-=weapon[indice_mini]["Price"]
                            player.player_data_dict["armor_level"] += 1
                            print("Félicitation " + player.player_data_dict["name"] + "vous venez d'obtenir une superbe arme, votre argent est maintenant à "+ player.player_data_dict["money"])
                    else:
                        retour = True
                else:
                    print("Vous ne pouvez pas acheter d'arme pour l'instant, continuer à combattre des monstres")
            if article in['Quitter','quitter']:
                print( "Vous allez quitter la boutique et retourner au menu")
                retour = True

    elif choice in ["Boss","boss"]:
        print("Vous vous appretez à effectuer un combat de boss")
        player.start_boss_fight()
            
    elif choice in ["Monstre","monstre"]:
        print("Vous vous appretez à affronter un monstre")
        player.start_monster_fight()
        
    elif choice in ["Quitter", "quitter"]:
        print("Vous allez quitter le jeu, votre jeu sera automatiquement sauvegardé")
        player.save_player_data()
        quit = True

