#import Candy
#import Playfield

class Pacman() :
    """
    Classe pour Pacman.
    
    ...
    
    Attributes
    ----------
    position : list
        Renseigne la position du pacman sur le terrain de jeu.
    jauge : int
        Renseigne le nombre de points score du pacman joué.
    
    Methods
    -------
    show_parameters :
        Affiche les caractéristiques du pacman joué (jauge, position).
    
    eat :
        Initialise l'action de manger du pacman joué.
        Ajoute ou retire un certain nombre de points relatif
        au type de bonbon mangé à la jauge du joueur.
    
    move :
        Initie le déplacement du pacman joué en renvoie sa nouvelle position.
        
    is_dead :
        Conclue sur la mort du pacman joué.
        
    def meet_wall : 
        Intercepte la rencontre du Pacman joué avec un mur d'un terrain.

    """    

    def __init__(self, position):
        """
        Initialise les caractéristiques du pacman joué avec une jauge et une position.
       
        ...

        Parameters
        ----------
    jauge : int
        Renseigne le nombre de points score du pacman joué.
    position : list
        Renseigne la position du pacman sur le terrain de jeu.

        """
        self.position = position
        
    def show_parameters(self):
        """
        Affiche les caractéristiques du pacman joué (jauge, position).

        """
        print(self.jauge)
        print(self.position)
        
    def move(self):
        """
        Initie le déplacement du pacman joué en renvoie sa nouvelle position.

        Parameters
        ----------
        moving : str
            Renseigne la direction prise par le joueur (entrée clavier)

        """       
        moving = input("Pour te déplacer, appuie sur q pour aller à gauche, d pour la droite, z en haut, s en bas")
        if moving == "q":
            self.position[0] -= 1
        elif moving == "d":
            self.position[0] += 1
        elif moving == "z":
            self.position[1] -= 1
        elif moving == "s":
            self.position[1] += 1
        return moving, self.position

class NicePacman(Pacman):
    """
    Sous-classe pour le joueur incarnant le Pacman "NicePacman".
    Modifie le nombre de points de jauge au départ de la partie,
    la manière de perdre le jeu et le résultat de l'action de manger un bonbon.
    
    Pour le NicePacman :
    Jauge de départ : 0 points
    Manger un bonbon : jauge + 5 ou + 10 points
    Etre mangé par l'autre joueur BadPacman : perte de la partie

    ...
    
    Attributes
    ----------
    jauge : int
        Renseigne le nombre de points score du pacman joué.
    position : list
        Renseigne la position du pacman sur le terrain de jeu.
    
    Methods
    -------
    show_parameters :
        Affiche les caractéristiques du pacman joué (jauge, position).
    
    eat :
        Initialise l'action de manger du pacman joué.
        Ajoute un certain nombre de points relatif
        au pouvoir du bonbon mangé à la jauge du joueur.
        
    is_dead :
        Conclue sur la mort du pacman joué.

    """   

    def __init__(self, position, jauge=0):
        """
        Initialise les caractéristiques du pacman joué.

        Parameters
        ----------
        position : list
            Renseigne la position du pacman sur le terrain de jeu.
        jauge : int
            Initialise à 0 le nombre de points score du pacman joué.

        """
        Pacman.__init__(self, position)
        self.jauge = jauge

    def eat(self,bonbon):
        """
        Initialise l'action de manger du pacman joué.
        Ajoute un certain nombre de points (5 ou 10) relatif au pouvoir
        du bonbon mangé à la jauge du joueur.

        """
        #bonbon = Candy.Candy      
        if bonbon.meet_pacman == True:
            self.jauge += bonbon.power()
        print(self.jauge)
        

    def is_dead(self):
        """
        Conclue sur la mort du NicePacman joué. Lorsqu'il atteint la même
        position que l'autre joueur BadPacman, le joueur NicePacman meurt et
        perd la partie.'

        Returns
        -------
        bool
            Indique si oui ou non le NicePacman joué est mort.

        """
        if self.jauge >= 100:
            print("Bien joué, Tu as gagné ! Le méchant Pacman est mort !")
            return False
        elif BadPacman.position == self.position:
            print("Oops, tu as perdu ! Le méchant Pacman a gagné !")
            return True            
        else:
            print(self.jauge)
            return False

class BadPacman(Pacman):
    """
    Sous-classe pour le joueur incarnant le Pacman "BadPacman".
    Modifie le nombre de points de jauge au départ de la partie,
    la manière de perdre le jeu et le résultat de l'action de manger un bonbon.
    
    Pour le BadPacman :
    Jauge de départ : 100 points
    Manger un bonbon : jauge - 5 ou - 10 points
    Jauge à 0 point : perte de la partie

    ...
    
    Attributes
    ----------
    jauge : int
        Renseigne le nombre de points score du pacman joué.
    position : list
        Renseigne la position du pacman sur le terrain de jeu.
    
    Methods
    -------
    show_parameters :
        Affiche les caractéristiques du pacman joué (jauge, position).
    
    eat :
        Initialise l'action de manger du pacman joué.
        Retire un certain nombre de points relatif
        au pouvoir du bonbon mangé à la jauge du joueur.
        
    is_dead :
        Conclue sur la mort du pacman joué.

    """   
    
    def __init__(self, position, jauge=100):
        """
        Initialise les caractéristiques du pacman joué.

        Parameters
        ----------
    position : list
        Renseigne la position du pacman sur le terrain de jeu.
    jauge : int
        Initialise à 100 le nombre de points score du pacman joué.

        """
        Pacman.__init__(self, position)
        self.jauge = jauge
        
    def eat(self, bonbon):
        """
        Initialise l'action de manger du pacman joué.
        Ajoute un certain nombre de points (5 ou 10) relatif au pouvoir
        du bonbon mangé à la jauge du joueur.

        """             
        #bonbon = Candy.Candy()          
        if bonbon.meet_pacman == True:
            self.jauge -= bonbon.power()
        print(self.jauge)

    def is_dead(self):
        """
        Conclue sur la mort du BadPacman joué. Lorsqu'il atteint une jauge
        de 0 point, le BadPacman meurt et perd la partie.'

        Returns
        -------
        bool
            Indique si oui ou non le BadPacman joué est mort.

        """
        if self.jauge == 0:
            print("Oops, tu as perdu !")
            return True
        elif self.position == NicePacman.position:
            print("Bien joué, tu as gagné !")
            return False
        else:
            print(self.jauge)
            return False              


#-----------------------------------------------------------------------------

# Test
#np = NicePacman([4,7])
#bp = BadPacman([2,1])

#np.show_parameters()
#bp.show_parameters()

#bonbon = Candy.Candy([6,3],10,True)

#np.eat(bonbon)