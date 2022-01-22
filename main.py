
from lib2to3.pgen2.token import RPAR
import random
from socket import SocketIO
import time
import os
from pystyle import Colors, Colorate,Anime, Colorate, Colors, Center, System, Write

banner="""
 __  __ _   _ _   _____ ___ ____  _     _____    ____    _    __  __ _____ 
|  \/  | | | | | |_   _|_ _|  _ \| |   | ____|  / ___|  / \  |  \/  | ____|
| |\/| | | | | |   | |  | || |_) | |   |  _|   | |  _  / _ \ | |\/| |  _|  
| |  | | |_| | |___| |  | ||  __/| |___| |___  | |_| |/ ___ \| |  | | |___ 
|_|  |_|\___/|_____|_| |___|_|   |_____|_____|  \____/_/   \_\_|  |_|_____|

"""

System.Size(140, 40)#Taille Fenetre
System.Title("Multiple GAMES")#Nom fenetre

def start():#Premier menu au lancement
    
    print (banner)#Premiere partie du load
    print("Loading.")
    time.sleep(0.3)
    

    print (banner)#Deuxieme partie du load 
    print("Loading./")
    time.sleep(0.3)
    

    print (banner)#Troisieme partie du load 
    print("Loading.\.")
    time.sleep(0.3)
    
    print (banner)
    
    print ("Bienvenue au menu d'acceuil du MULTIPLE GAMEE!")
    time.sleep(1)
    def select_game_function():
        print ("Voici tout les jeux: ")
        time.sleep(0.5)
        print("1.Nombre Mystères")
        time.sleep(0.3)
        print("2.Pierre, Feuille, Ciseaux")
        time.sleep(0.3)
        print ("3.Aleatoire")
        time.sleep(0.3)
        print("4.Exit")
    select_game_function()

    time.sleep(0.6)
    select_game_input = int(input("Ecrit 1,2 ou 3 en fonction du jeu auxquels tu veux jouer: "))
    time.sleep(0.9)
    if select_game_input == 1:#Nombre Mystere
        print ('Secret number selected!')
        time.sleep(0.9)
        scecret_number_game()
    if select_game_input ==2:#Nombre Mystere
        print ('Pierre feuille ciseaux Selected!')
        time.sleep(0.9)
        pierre_game()

    if select_game_input == 3:#Jeux aleatoire
        random_game = random.randint(1,2)
        if random_game == 1:
            print("Random module choose secret number")
            time.sleep(0.9)
            scecret_number_game()
        if random_game == 2:
            print ("Random module choose dev game")
            time.sleep(0.9)
            pierre_game()
    if select_game_input == 4:
        print("Aurevoir!")
        exit()



        
def scecret_number_game():#Jeu n*1
    score_secret_number = 0 #Score 
    game_lunch = True
    secret_number = random.randint(1,100)
    cheat_fstring = "**CHEAT**"

    print ("Bienvenue au nombre mystere")

    while game_lunch:#Boucle du jeu
        time.sleep(0.7)
        print ("Score:",score_secret_number)

        player_number = float(input("Entrez un nombre au choix en 1 et 100: "))

        if player_number > secret_number:#Si le nombre du joueur est trop grand
            print ("C'est moin")
        if player_number < secret_number:#Si le nombre du joueur est trop petit
            print ("C'est Plus") 
        if player_number == 1809:#Code Secret Pour menu secret
            cheat_menu=True

            while cheat_menu:#Menu secret
                
                print ("Bienvenue dans le menu secret :)")
                time.sleep(0.6)
                print ("1.(Give points)")
                print ("2.(Show secret number)")
                print("3.(Exit)")
                
                secret_menu_input = int(input("Type 1,2 or 3 according to the cheat options you want: "))
                if secret_menu_input == 1:
                    give_point_input = int(input("How many points do you want (enter a number): "))
                    score_secret_number = give_point_input
                    print(f"{cheat_fstring} Your score has been succesfully updated {cheat_fstring}")
                    cheat_menu = False
                if secret_menu_input == 2:
                    print(f"{cheat_fstring} Secret Number: {secret_number} {cheat_fstring}")
                    cheat_menu = False
                if secret_menu_input == 3:
                    print (f"{cheat_fstring} Leaving the cheat menu {cheat_fstring}")
                    time.sleep(0.9)
                    cheat_menu = False

        if player_number == secret_number:
            print("Bien joué")
            time.sleep(0.3)
            restart_var = input("Voulez vous continuz?(y/n):")
            score_secret_number +=1
            if restart_var == "y":
                secret_number = random.randint(1,100)
                game_lunch
                a = 0
                while a<1:
                    print("/..")
                    a+= 1
                    time.sleep(0.1)
                    print ("../")

            if restart_var =='n':          
                print('Aurevoir')       
                start()
            else:
                start()

def pierre_game():#Jeu n*2
    import random
    pierre_game = True
    cheat_fstring = "**CHEAT**"
    element_list = ["Pierre","Feuille","Ciseaux"]
    score_pierre_game = 0
    print("Bienvenue dans Pierre, Feuille, Ciseaux")
    time.sleep(1)
    print ("Vous allez jouer contre un bot")
    time.sleep(1)
    
    def rappel_exit():
        print('Tapez exit si vous voulez quittez a nimporte quel momment')

    while pierre_game:
        pierre_equal_choose = True 

        while pierre_equal_choose:
            pierre_aletoire = random.choice(element_list)
            print("Score:",score_pierre_game)
            pierre_game_player_input = input("Pierre Feuille ou Ciseaux (entrez votre réponse)?:")

            #Si le bot a pierre:#############################################

            if pierre_aletoire == "Pierre" :
                if pierre_game_player_input == "Pierre":
                    print("Egalité, recommencez")
                    time.sleep(0.6)
                    rappel_exit()
                    time.sleep(1)
                    print ("\n"*2)
                if pierre_game_player_input == "Feuille":
                    print(f"Bien joué +1 le bot avait choisis: {pierre_aletoire}")
                    score_pierre_game+=1
                    time.sleep(0.6)
                    rappel_exit()
                    time.sleep(2)
                    print ("\n"*2)
                if pierre_game_player_input == "Ciseaux":
                    print (f"Vous avez perdu, le bot a choisi: {pierre_aletoire} ")
                    time.sleep(0.6)
                    rappel_exit()
                    time.sleep(2)
                    print ("\n"*2)

            #Si le bot a feuille #############################################

            if pierre_aletoire == "Feuille":
                if pierre_game_player_input == "Pierre":
                    print(f"Vous avez perdu, le bot a choisis: {pierre_aletoire}")
                    time.sleep(0.6)
                    rappel_exit()
                    time.sleep(3)
                    print ("\n"*2)
                if pierre_game_player_input == "Feuille":
                    print("Egalité, recommencez")
                    time.sleep(0.6)
                    rappel_exit()
                    time.sleep(1)
                    print ("\n"*2)
                if pierre_game_player_input == "Ciseaux":
                    print(f"Bien joué +1 le bot avait choisis: {pierre_aletoire}")
                    score_pierre_game +=1
                    time.sleep(0.6)
                    rappel_exit
                    time.sleep(2)
                    print ("\n"*2)
                    
            #Si le bot a ciseau#############################################

            if pierre_aletoire == "Ciseaux":
                if pierre_game_player_input == "Pierre":
                    print(f"Bien joué +1 le bot avait choisis: {pierre_aletoire}")
                    score_pierre_game+=1
                    time.sleep(0.6)
                    rappel_exit
                    time.sleep(2)
                    print ("\n"*2)
                if pierre_game_player_input == "Feuille":
                    print(f"Vous avez perdu, le bot a choisis: {pierre_aletoire}")
                    time.sleep(0.6) 
                    rappel_exit
                    time.sleep(3)
                    print ("\n"*2)
            #Quittez le jeu #############################################

            if pierre_game_player_input == "exit":
                start # reviens au menu d'acceuil

            #Cheat Menu #############################################
            if pierre_game_player_input == "2705":
                pierre_cheat = True
                while pierre_cheat:#Menu secret
                    
                    print ("Bienvenue dans le menu secret :)")
                    time.sleep(0.6)
                    print ("1.(Give points)")
                    print ("2.(Show secret number)")
                    print("3.(Exit)")
                    
                    secret_menu_input = int(input("Type 1,2 or 3 according to the cheat options you want: "))
                    
                    if secret_menu_input == 1:
                        give_point_input = int(input("How many points do you want (enter a number): "))
                        score_pierre_game = give_point_input
                        print(f"{cheat_fstring} Your score has been succesfully updated {cheat_fstring}")
                        pierre_cheat = False

                    if secret_menu_input == 2:
                        print(f"{cheat_fstring} Secret Number: {pierre_aletoire} {cheat_fstring}")
                        pierre_cheat = False

                    if secret_menu_input == 3:
                        print (f"{cheat_fstring} Leaving the cheat menu {cheat_fstring}")
                        time.sleep(0.9)
                        pierre_cheat = False


            if pierre_game_player_input == " ":
                print ("Veuillez entrez une réponse correcte")       
            if pierre_game_player_input =="exit":
                start()

        

start()