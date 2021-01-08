#import Pacman as pc 
#import Game

class Candy():
    """
    Classe implémentant un bonbon.
    
    ...
    
    Attributes
    ----------
    position : int
        Les différentes positions des Candies sur la matrice
    power : int
        Les deux types de pouvoir des Candies (5 et 10)
    status : bool
        Visible où non sur la matrice

    ... 

    Methods
    -------
    is_eaten(status)
        Si le Candy est mangé par un Pacman, 
        il n'apparait plus sur la matrice 
        et son statut devient False
    """

    def __init__(self, position, power, status):
        """
        Initialise le Candy avec une position, un pouvoir et un statut

        ...

        Parameters
        ----------
        position: int
            position dans la matrice, array
        power : int
            différent type de pouvoir (5 ou 10)
        status : bool
            True si toujours présent, False si mangé par un Pacman
        """
        self.position = position
        self.power = power
        self.status = status
    
    def meet_pacman(self):
        """
        Défini si un Candy est mangé ou pas

        ...

        Parameters
        ----------
        status : bool
            Initialement True car le Candy est visible sur le jeu
            Si un Pacman et un Candy sont sur la même position,
            Le statut du Candy devient False car il sera mangé
        NicePacman : objet
            Depend de la position de NicePacman
        BadPacman : objet
            Depend de la position de BadPacman
        """
        self.status == True
        if (pc.NicePacman.position or pc.BadPacman.position) == self.position:
            print("Test")
            self.status == False
            return True
        else:
            self.status == True
            return False


# Test
#candy1 = Candy([8,1],10,True)
#candy2 = Candy([6,3],10,True)
#np = Pacman.NicePacman([8,1],0)
#bp = Pacman.BadPacman([6,3],100)

#candy1.is_eaten() 

# is_eaten() foire 
# NameError: name 'Pacman' is not defined

