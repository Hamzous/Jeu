from pymongo import MongoClient
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
 # 3 -> 