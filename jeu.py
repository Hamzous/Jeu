from pymongo import MongoClient
import sys
import random


# MENU = [
#   "Lancer Jeu",
#   "Afficher les scores",
#   "Quitter",
# ]
MENU = [
    "Lancer Jeu",
    "Afficher les scores",
    "Quitter",
]

# Menu
#   Boucle sur tout element de MENU
#       afficher numero element et texte element
def afficher_menu():
    for i in range(len(MENU)):
        print(i + 1, "-", MENU[i])


# Choix (options, erreur)
#    while True:
#        Recuperer choix utilisateur
#        Verifier si choix est valide
#        Si valide
#             return choix
#        Sinon
#             Lancer fonction erreur

 
 
def choix(options, erreur):
    while True:
        saisie = input("Votre choix : ")
        if saisie.isdigit() and 1 <= int(saisie) <= len(options):
            return int(saisie)
        else:
            erreur()
            
def erreur():
    print("Erreur : saisie invalide")

afficher_menu()
choix(MENU , erreur)


# Recuperer heros DB
#       ouvrir base
#       acceder a la collection heros
#       find
#       convertir le curseur en liste
#       heros_dispo = liste
def recuperer_heros():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["game_db"]
    collection = db["characters"]
    curseur = collection.find()
    liste = list(curseur)
    heros_dispo = liste
    return heros_dispo
print(recuperer_heros())

# Afficher heros dispo
#       Boucle sur tout element de heros_dispo
#           afficher nom, pv, attaque, defense
def afficher_heros_dispo(heros_dispo):
    for hero in heros_dispo:
        print(hero["nom"], "| PV :", hero["pv"], "| Attaque :", hero["attaque"], "| Défense :", hero["defense"])


# Récupérer 3 noms valides
#       noms = []
#       tant que len(noms) < 3 :
#           Recuperer nom utilisateur
#           Verifier si nom est valide
#               nom existe dans heros_dispo (sans tenir compte majuscules)
#               pas deja dans noms
#           Si valide
#               ajouter nom a noms
#           Sinon
#               Lancer fonction erreur
#       return noms
def recuperer_3_noms_valides(heros_dispo):
    noms = []
    while len(noms) < 3:
        nom = input("Nom du héros : ").lower()
        existe = False
        for hero in heros_dispo:
            if hero["nom"].lower() == nom:
                existe = True
        deja_dans_noms = nom in noms
        if existe and not deja_dans_noms:
            noms.append(nom)
        else:
            erreur()
    return noms



# Construire l'equipe
#       equipe = []
#       for nom in noms :
#           hero = element de heros_dispo dont le nom == nom
#           hero.estEnVie = True
#           ajouter hero a equipe
#   return equipe
def construire_equipe(noms , heros_dispo):
    equipe = []
    for nom in noms:
        for element in heros_dispo :
            if element ["nom"] == nom :
                hero = element
        hero["estEnVie"] = True
        equipe.append(hero)
    return equipe 


# nouveau.monstre
#     recup monstres DB
#         ouvrir base
#         acceder a la collection monstre
#         find
#         convertir le curseur en liste
#     monstre = random dans la liste
#     monstre.estEnVie = True

def nouveau_monstre():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["game_db"]
    collection = db["monsters"]
    curseur = collection.find()
    liste = list(curseur)
    print(liste)
    monstre = random.choice(liste)
    monstre["estEnVie"] = True
    return monstre
print(nouveau_monstre())


# estEnVie :
#     si les pv > 0 : return True
#     sinon : return False

def estEnVie( personnage): 
    if personnage["PV"] > 0 :
        return True
    else :
        return False

# afficher_stats_hero : afficher les stats hero

def afficher_stats_hero (equipe):
    for hero in equipe :
        print (hero["nom"] , " PV : ", hero["hp"], " Attaque : " , hero["attack"] , "defense : ", hero["defense"])

# afficher_stats_monstre : afficher les stats monstre

def afficher_stats_monstre (monstre) :
        print (monstre["nom"] , " PV : ", monstre["hp"], " Attaque : " , monstre["attack"] , "defense : ", monstre["defense"])


# hero_attaque
#     recuperer attaque hero
#     recuperer hp et defense monstre
#     degats_hero = attaqueHero - defense.monstre
#     pv_monstre = pv_monstre - degats_hero
#     return degats_hero

def hero_attaque(hero, monstre):
    attaque_hero = hero["attack"]
    pv_monstre = monstre["hp"]
    defense_monstre = monstre["defense"]
    degats_hero = attaque_hero - defense_monstre
    pv_monstre = pv_monstre - degats_hero
    monstre["estEnVie"] = estEnVie(monstre)
    return degats_hero


# attaquer_monstre
#     recuperer attaque monstre
#     recuperer defense hp hero
#     degats_monstre = attaqueMonstre - defense.hero
#     pv_hero = pv_hero - degats_monstre
#     return degats_monstre

def monstre_attaque(monstre , hero) :
    attaque_monstre = monstre["attack"]
    pv_hero = hero["hp"]
    defense_hero = hero["defense"]
    degats_monstre = attaque_monstre - defense_hero
    pv_hero = pv_hero - degats_monstre
    hero["estEnVie"] = estEnVie(hero)
    return degats_monstre


def au_moins_un_hero_en_vie(equipe):
    for hero in equipe:
        if hero["estEnVie"] == True:
            return True
    return False



# JEU
def jeu():
    # Récupérer 3 noms valides (création de l'équipe)
    # tant que au moins un hero est en vie 
    # for heros in choix 
    # for monstre in choix 
    # le monstre attaque le premier héros en vie



    heros_dispo = recuperer_heros()
    afficher_heros_dispo(heros_dispo)
    noms = recuperer_3_noms_valides(heros_dispo)
    equipe = construire_equipe(noms, heros_dispo)
    vague = 0
    monstre = nouveau_monstre()
    while au_moins_un_hero_en_vie(equipe):
        afficher_stats_hero(equipe)
        afficher_stats_monstre(monstre)
        for hero in equipe:
            if hero["estEnVie"] == True:
                degats_hero = hero_attaque(hero, monstre)
                print(hero["nom"], "inflige", degats_hero, "dégâts")
                if monstre["estEnVie"] == False:
                    print("Le monstre", monstre["nom"], "est mort")
                    vague += 1
                    monstres = nouveau_monstre()
                    break
            else:
                print("Le héros", hero["nom"], "est mort")

        for monstre in [monstres]:
            if monstre["estEnVie"] == True:
                for hero in equipe:
                    if hero["estEnVie"] == True:
                        degats_monstre = monstre_attaque(monstre, hero)
                        print(monstre["nom"], "inflige", degats_monstre, "dégâts")
                        break
            else:
                print("Le monstre", monstre["nom"], "est mort")
