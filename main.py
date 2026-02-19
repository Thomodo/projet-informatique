from function import *
from classe import *

### Initialisaton (on veut savoir si le joueur veut charger la sauvegarde)

ans = input("Voulez vous charger la sauvegarde ?\n"
            "'O' pour Oui, 'N' pour Non\n"
            "\n")
while ans not in ["O","N"]:
    ans = input("Vous devez répondre 'O' ou 'N'!\n")


if ans == "O": # Si la réponse est oui 
    print("Chargement de la sauvegarde")
else:
    print("Création d'une nouvelle sauvegarde")
