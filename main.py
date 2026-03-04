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
    create_new_save()
    print("Création d'une nouvelle sauvegarde")


### choisir ce qu'on fait