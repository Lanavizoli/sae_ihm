import Playfield
import Pacman 
import Candy

class Game: 
    """
    La classe Game initialise le jeu 
    
    Attributes
    ----------
    gamestate : bool
    indique l'état du jeu (en cours ou non), false, le jeu n'est pas en cours, true le jeu est en cours
   
    Methods
    -------
    Newgame : BOOL
        lance le jeu et instancie les éléments nécessaires
    endofgame : BOOL
        regarde si nicepacman ou badpacman est mort et termine le jeu si c'est le cas
    intercept_candy : 
        regarde si un bonbon est rencontré lors du déplacement d'un pacman
    intercept_wall :
        regarde si un mur est rencontré lors du déplacement d'un pacman
        
    
    """
    def __init__(self, gamestate):
        
        """
        Initialise le jeu
        
        Attributes
        ----------
        gameState = indique l'état du jeu (en cours ou non), false, le jeu n'est pas en cours, true le jeu est en cours
        
        """
        self.nicepacman1 = Pacman.NicePacman([7,8],0)
        self.badpacman1 = Pacman.BadPacman([8,8],100)
        self.terrain = Playfield.Playfield()
        self.gamestate = gamestate
    
    def new_game(self):
        """
        Lance le jeu et et créer les éléments nécessaires
     
        """
        start=str(input("Tapez GO pour commencer "))
        if start=="Go":
            print("Ok, let's begin!")
            self.terrain.create_matrice()
            self.terrain.create_candies()
            self.nicepacman1.show_parameters
            self.badpacman1.show_parameters
            #return gamestate == True
        
            
    def tour(self):
        """
        Définit comment un tour du jeu se passe
        
        Returns
        -------
        Retourne les paramètres de chaque pacman
        
        """
        while self.gamestate==True: 
            print ("déplacement Nicepacman")
            print ("déplacement Badpacman")
            self.nicepacman1.move()
            self.badpacman1.move()

            if self.terrain.is_wall(self.nicepacman1.position) == True:
                print("Oups Nice, c'est un mur, tu dois de déplacer à nouveau !")
                self.nicepacman1.move()
            elif self.terrain.is_wall(self.badpacman1.position) == True:
                print("Oups Bad, c'est un mur, tu dois de déplacer à nouveau !")
                self.badpacman1.move()
            else:
                self.nicepacman1.eat() 
                self.badpacman2.eat()
            
            for x in (self.terrain.create_candies):
                if self.nicepacman1.position == self.terrain.create_candies[x].position:
                    self.nicepacman1.eat(self.terrain.create_candies[x])
                elif self.badpacman1.position == self.terrain.create_candies[x].position:
                    self.badpacman1.eat(self.terrian.create_candies[x])

    def end_of_game(self):
            """
            Définit comment le jeu se termine
            
            Returns
            -------
            Retourne l'état du jeu, True si rien ne se passe, False si un des pacman est mort
            
            """
            if (self.badpacman1.is_dead() == True) or (self.nicepacman1.is_dead() == True):
                self.gamestate = False
                return self.gamestate
            else:
                self.gamestate = True
                return self.gamestate

        
    
        

  
    
        
        