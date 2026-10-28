"""
# MENU = [
#   "Lancer Jeu",
#   "Afficher les scores",
#   "Quitter",
#    ]
# Menu
#   Boucle sur tout element de MENU
#       afficher numero element et texte element
# Choix (options, erreur)
#    while True:
#        Recuperer choix utilisateur
#        Verifier si choix est valide
#        Si valide
#             return choix
#        Sinon
#             Lancer fonction erreur
# Process
        
# Creation equipe

#   Recuperer heros DB
#       ouvrir base
#       acceder a la collection heros
#       find
#       convertir le curseur en liste
#       heros_dispo = liste
#
#   Afficher heros dispo
#       Boucle sur tout element de heros_dispo
#           afficher nom, pv, attaque, defense
#
#   Récupérer 3 noms valides
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
#
#   Construire l'equipe
#       equipe = []
#       for nom in noms :
#           hero = element de heros_dispo dont le nom == nom
#           hero.estEnVie = True
#           ajouter hero a equipe
#
#   return equipe 

#    JEU
    Récupérer 3 noms valides 
#    tant que au moins un hero est en vie :
        afficher_stats_hero    : afficher les stats hero
        afficher_stats_monstre : afficher les stats monstres
            for heros in choix :
                if hero.estEnVie = True :
                    hero_attaque 
                        recuperer attaque hero
                        recuperer hp et defense monstre 
                        degats-hero = attaqueHero - defense.monstre
                        pv-monstre = pv-monstre - attaqueHero
                        return degats_hero
                    print hero inflige degats
                si monstre.estEnVie = false :
                    le monstre {nomMonstre} est mort 
                    vague += 1
                    nouveau.monstre
                        recup monstres DB
                            ouvrir base
                            acceder a la collection monstre
                            find 
                            convertir le curseur en liste
                        monstre = random  dans la liste
                        monstre.estEnVie = True 
                    break

                else : 
                le hero {nom.Hero} est mort 

            for monstre in choix :
                    if monstre.estEnVie = True :
                        attaquer_monstre
                            recuperer attaque monstre
                            recuperer defense hp hero
                            degats_monstre = attaqueMonstre - defense.hero
                            pv-hero = pv-hero - attaqueMonstre
                            return degats_monstre
                        
                        print monstre inflige degats
                    else : 
                    le monstre {nom.monstre} est mort 
            
                                        si les pv > 0 :
                                            return True
        estEnVie   :                    else :
                                            return false
#    Afficher les scores
#        Recuperer scores base
#            ouvrir base
#            acceder a collection score
#            find
#            convertir curseur en list
#        filtrer les 3 meilleurs
#             trie le tableau sur element.waves
#             prendre 3 derniers elements
#                    array[-3:-1]
#        Affiche les score
#    Quitter
#       sys.exit()


def GetName():
    name = input("Entrez votre nom: ")
    return name


def GetRNDName():
    import random
    names = ["Alice", "Bob", "Charlie", "Diana"]
    return random.choice(names)


def print_hello(name_func):
    name = name_func()
    print(f"Bonjour, {name} !")


print_hello(GetName)
print_hello(GetRNDName)
"""