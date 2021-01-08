#from p5 import *
import Game as gm 


jeu = gm.Game(True)

jeu.new_game()
while jeu.gamestate == True: 
    jeu.tour()
    jeu.end_of_game()
else:
    suite=print(input('Veux-tu recommencer? Oui ou Non \n > '))
    if suite == 'Oui':
        jeu.new_game()
    else:
        del jeu 


