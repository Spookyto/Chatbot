import time
import random

name = input("Salut comment tu t'apelle ? ")

time.sleep(2)
print("Enchanté " + name)

feeling = input("Comment tu vas aujhourd'hui? ")

time.sleep(1)
if "et toi" in feeling:
    print("Personellement je suis une Machine je ne peux pas avoir de sentiment :)!")
else:
    print("Je suis desoler d'apprendre ça!")

time.sleep(1)
favcolour = input("Quelle est ta couleur préférée? ")

colours = ["Rouge","Vert","Bleu"]

time.sleep(1)
print("Ma Couleur préférée est  " + random.choice(colours))

mood = input("Quesque tu fait aujourd'hui? ")
mood = ["danse", "lie", "joue", "regarde la tele", "Marche"]
time.sleep(1)
print("Personellement je  " + random.choice(mood) + " aujourd'hui")

love=input("Tu a une petite amie? ")
love = ["oui", "Non"]
time.sleep(1)
input("cool")

food = input("Quelle est ta nouritture préferée? ")
food=["Asiatique", "Japonais", "Italien", "Chinois", "Oriental"]
time.sleep(1)
print("Je préfére " + random.choice(food))

sport = input("Quelle est le sport que tu aime le plus regarder ? ")
sport=["Football", "Basketball", "Tennis", "Rugby", "Athlétisme"]
time.sleep(1)
print("Non le meilleur c'est " + random.choice(sport))
time.sleep(1)
print("J'aime bien parler avec toi!")


peak = input("Est ce que tu connais la taille de la Montagne la plus haute du monde ? ")
time.sleep(1)
print("8848")
print("N'importe qui peut répondre à une question comme ça! ")

planet = input("Combien de planet il y a t'il dans le systéme Solaire?")
time.sleep(1)
print("Je pense qu'il y a 8 planetes")

horscope = input("Quelle est ton signe Astrologique? ")
horscope=["Lion", "Cancer", "Capricone", "Poisson", "Gémaux"]
time.sleep(1)
print("Le mien est le   " + random.choice(horscope))

exe = input("Combien de Pompes peut tu faire? ")
exe=["1", "15", "25", "40", "50"]
time.sleep(1)
print("Je pense que j'en fait à peu prés " + random.choice(exe))

tired = input("Je me sent fatigué aujhourd'hui.")
time.sleep(1)
print("Aurevoir, à la prochaine .")







