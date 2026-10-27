from pymongo import MongoClient
import sys
client = MongoClient("mongodb://localhost:27017")

db = client["game_db"]

perso = db.characters.find({}, {"_id": 0, "name": 1})

for perso in perso : 
    print (perso["name"])

monstres = db.monsters.find({} , {"_id": 0 , "name": 1})

for m in monstres : 
    print (m["name"])



# afficher le meunu de choix
 # 1 -> Demarrer la partie
 # 2 -> Settings
 # 3 -> Quitter

# 1 -> choisir perso
    # afficher liste perso
    # afficher les perso choisis et ses caracteristiques 
    # afficher les monstres 
    # Choirisir le monstre
    # afficher le monstre choisis et ses caracteristiques
    # lancer le combat 

# 2 -> modifier les params (evol donc oiur plus tard)
    # revenir a l'accueil

# 3 -> # quitter le jeu 


# COMBAT 

# afficher les stats du hero 
# afficher les stats du monstre 
# faire attaquer le hero 
# faire attaquer le monstre
# si le monstre est mort , le hero gagne 
# sinon le hero perd 
# affciher les PV restants du gagnat 
# affciher gg 


"""
afficher le meunu demarrer 

afficher ---------------Bienvenue sur le jeu------------
afficher 1 -> demarrer la game 
afficher 2 -> settings
afficher 3 -> Quitter 








"""

"""
                                        --- PYTHON ---

tant que le joueur ne quitte pas ke jeu

def afficher_menu():
    print( " 1 - Demarrer la game)
    print( " 2 - Settings) (settings)
    print( " 3 - Quitter la game) (sys.exit a confirmer )

    
    si choix = 1 alors :
                                                demander au joueur de choisir ses persos
              demander_hero:                    afficher la lisye des perso dispo
                                                afficher les caracteristiques des perso choisis
                                                        afficher la lisye des monstres 
            demander_monstre  :                         demander de choisisr les monstres 
                                                        afficher les caracteristiques du monstre choisis
        afficher le combat commence !
        tant que PV-hero > 0 et PV-monstre > 0 :
            afficher les stats hero
            afficher les stats monstres

            faire attaquer le hero

            si les pv monstre < 0 :
                Le hro a gagné 
            elif pv-hero < 0 : 
                le monstre a gagner 
            else : continuez le combat 

    si choix = 2 
        afficher les settings 
    si choix = 3 :
        merci au revoir 

            


"""