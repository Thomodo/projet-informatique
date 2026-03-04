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

### choisir ce qu'on fait
quit = False 

while quit != True : 
    choice = input (" Que souhaité vous faire ? \n" 
                " Pour accéder à votre boutique, entrez 'boutique'\n"
                " Pour effectuer un combat de boss, entrez 'boss'\n"
                " Pour effectuer un combat contre un monstre, entrez 'monstre' \n"
                " Pour quitter la partie , entrez 'quitter' \n")
    
    while choice not in [ "Boutique","boutique", "Boss", "boss","Monstre","monstre",' Quitter', 'quitter']:
        choice = input("Vous devez répondre par soit par 'boutique' soit par  'boss'soit par  'monstre' ou par 'quitter'!\n")
        
        if choice in ["Boutique","boutique"]:
             print ( "Bienvenue dans la boutique (pseudo)")

        elif choice in ["Boss","boss"]:
            print ("Vous vous appretez à effectuer un combat de boss")
            
        elif choice in ["Monstre","monstre"]:
            print ("Vous vous appretez à affronter un monstre")
        
        elif choice in [ "Quitter", "quitter"]:
            print (" Vous allez quitter le jeu, votre jeu sera automatiquement sauvegarder ")
            player.save_player_data()
            quit = True 
