import numpy as np
import Candy

class Playfield():
    """
    Classe implémentant le terrain de jeu.
    
    ...
    
    Attributes
    ----------
    matrice : array de booléen

    ... 

    Methods
    -------
    create_matrice():
        Créé le terrain de jeu par un array en 2 dimensions
    
    create_candy():
        Création des Candies sur le terrain de jeu
    
    is_wall(val):
        Annonce au Pacman qu'il ne peut pas se déplacer sur les "1" 
        du terrain de jeu car ils sont considérés comme des murs
    """

    def __init__(self):
        """
        Initialise le terrain de jeu avec deux fonctions :
        create_matrice() qui va créer la matrice
        create_candies() qui va créer les Candies sur la matrice

        """
        self.create_matrice()
        self.create_candies()

    def create_matrice(self):
        """
        Création de la matrice (terrain de jeu) avec un array en 2 dimensions
        """
        self.matrice = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
            [0, 1, 1, 1, 1, 0, 0, 0, 0],  # 1
            [0, 0, 0, 0, 1, 0, 0, 0, 0],  # 2
            [0, 0, 0, 0, 1, 0, 0, 0, 0],  # 3
            [0, 0, 0, 0, 1, 1, 1, 1, 0],  # 4
            [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5
            [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
            [0, 1, 1, 1, 0, 0, 1, 1, 0],  # 7
            [0, 0, 0, 0, 0, 0, 0, 0, 0]  # 8
        ], dtype=bool)
            # 0, 1, 2, 3, 4, 5, 6, 7, 8
            #ligne puis colonne
        print(self.matrice)

    def create_candies(self):
        """
        Créer les Candies en les positionnant sur la matrice 

        ...

        Parameters
        ----------
        Candy : objet
            Instantation de 6 Candies sur le terrain de jeu
            Retourne les Candies
        """
        candy1 = Candy.Candy([8,1],10,True)
        candy2 = Candy.Candy([6,3],10,True)
        candy3 = Candy.Candy([3,8],10,True)
        candy4 = Candy.Candy([5,6],10,True)
        candy5 = Candy.Candy([1,5],5,True)
        candy6 = Candy.Candy([2,5],5,True)
        list_candies = ['candy1', 'candy2', 'candy3', 'candy4', 'candy5', 'candy6']
        return list_candies

    def is_wall(self, val): #Faire appel dans Game
        """
        Vérifie s'il y a un mur ou pas

        ...

        Parameters
        ----------
        val : array int
            0 étant la première valeur de la position
            1 étant la deuxième valeur
            Retourne un True s'il y a un mur (défini comme 1 dans la matrice)
            Retourne un False s'il y a un mur (défini comme 0 dans la matrice)
        """
        return self.matrice[val[0]][val[1]] #0 = première valeur de la position // 1 = deuxième valeur 



#Pf = Playfield()
#matrice = Pf.create_matrice()
#cand = Pf.create_candies()
#print(cand)