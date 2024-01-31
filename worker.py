import time

class Chemin:
    """
    Classe définissant le chemin que parcour les minerais de la mine.
    
    """
    def __init__(self, niveau, money, typeminerais="Argent", kgtotal=0, vitesse=10, nbminerais=1, minerais1=0, minerais2=0, minerais3=0):
        """
        

        Parameters
        ----------
        niveau : int,
            Niveau de la mine.
        money : int,
            Money de l'utilisateur.
        typeminerais : string, Or, Ruby, Diamant, Palladium, Rhodium
            Type de minerais que le mineur mine. The default is "Argent".
        kgtotal : int,
            Kilogrammes totaux miné. The default is 0.
        vitesse : int,
            Vitesse des employés de la mine. The default is 10.
        nbminerais : int,
            Nombre de minerais que mine le mineur. The default is 1.
        minerais1 : int,
            Minerais miné. The default is 0.
        minerais2 : int,
            Minerais transporté. The default is 0.
        minerais3 : int,
            Minerais transféré et stocké. The default is 0.

        Returns
        -------
        None.

        """
        self.__niveau = niveau
        self.__vitesse = vitesse
        self.minerais1 = minerais1
        self.minerais2 = minerais2
        self.minerais3 = minerais3
        self.__money = money
        self.__nbminerais = nbminerais
        self.typeminerais = typeminerais
        self.kgtotal = kgtotal
    
    
    def miner(self):
        """
        

        Mine
        ----
        x minerais en fonction du niveau de la mine..

        """
        #On ajoute un certains une certaine valeur à self.minerais1 en x secondes (en fonction de la vitesse du niveau de mine)
        
        print("Le Mineur mine",self.__nbminerais,"kg",self.typeminerais,"...")
        time.sleep(self.__vitesse)
        if self.minerais1 >= 0:
            self.minerais1 = self.minerais1 + self.__nbminerais

    def transporter(self):
        """
        

        Transporte
        ----------
        Les minerais que mine le mineur à l'éxterieur de la mine.

        """
        #On transfère la valeur présente dans self.minerais1 à self.minerais2 en x secondes (en fonction de la vitesse du niveau de mine)
        
        if self.minerais1 >= 1:
            self.minerais2 = self.minerais1
            self.minerais1 = self.minerais1 - self.minerais1
            print("Le Liftier monte",self.minerais2,"kg",self.typeminerais,"...")
            time.sleep(self.__vitesse)
        else:
            #Si il n'y a pas au moins 1 minerais l'action est impossible
            print("Vous ne pouvez pas executer cette action.")

    def transferer(self):
        """
        

        Transfère
        ---------
        Les minerais que monte le liftier au point de vente.

        """
        #On transfère la valeur présente dans self.minerais2 à self.minerais3 en x secondes (en fonction de la vitesse du niveau de mine)

        if self.minerais2 >= 1:
            self.minerais3 = self.minerais3 + self.minerais2
            self.minerais2 = self.minerais2 - self.minerais2
            print("Le Pousseur de chariot ramène",self.minerais3,"kg",self.typeminerais,"...")
            time.sleep(self.__vitesse)
        else:
            #Si il n'y a pas au moins 1 minerais l'action est impossible
            print("Vous ne pouvez pas executer cette action.")

    def get_money(self):
        """
        

        Returns
        -------
        La money que possède l'utilisateur.

        """
        return self.__money
    
    def __set_money(self,valeur):
        """
        
        Set
        ---
        Met la money de l'utilisateur à la valeur du paramètre valeur.
        
        """
        self.__money = valeur
        
    def money(self):
        """
        

        Transforme
        -------
        Les minerais en argent en fonction du niveau de la mine.

        """
        #Convertit la valeur (minerais) présent dans self.minerais3 en money en fonction du minerais miné (niveau de mine)
        
        if self.__niveau < 20:
            temp = 1000
    
        elif self.__niveau >= 20 and self.__niveau < 40:
            temp = 5000
        
        elif self.__niveau >= 40 and self.__niveau < 60:
            temp = 10000
        
        elif self.__niveau >= 60 and self.__niveau < 80:
            temp = 15000
        
        elif self.__niveau >= 80 and self.__niveau < 100:
            temp = 20000
        
        elif self.__niveau >= 100:
            temp = 25000
            
            
        if self.minerais3 > 0:
            self.__money = self.__money + self.minerais3*temp
            print("+ ",self.minerais3*temp)
            self.kgtotal = self.kgtotal + self.minerais3
            self.minerais3 = self.minerais3 - self.minerais3
        else:
            print("Vous ne pouvez pas executer cette action.")
        
    def get_kgtotal(self):
        """
        

        Returns
        -------
        Les kilogrammes totaux miner par l'utilisateur.

        """
        return self.kgtotal
    
    def get_niveau(self):
        """
        

        Returns
        -------
        Le niveau de mine de l'utilisateur.

        """
        return self.__niveau
    
    def __set_niveau(self,valeur):
        """
        
        Set
        ---
        Met le niveau de mine de l'utilisateur à la valeur du paramètre valeur.
        
        """
        self.__niveau = valeur
    
    def up(self):
        """
        
        
        Augmente
        --------
        Le niveau de mine de l'utilisateur si il a assez d'argent.
        
        """
        #Achète un niveau si l'utilisateur à assez d'argent.
        #A chaque niveau augmenté la vitesse de minage diminue de 3% et le prix des minerais augmente de 3%
        #A certains niveaux le minerais à miner change et deviens plus rare donc plus cher
        temp = 100*self.__niveau**2
        if self.__money >= temp:
            self.__money = self.__money - temp
            self.__niveau = self.__niveau + 1
            print("Votre mine est au niveau {}.".format(mineur.get_niveau()))
            self.__vitesse = self.__vitesse*0.97
            self.__nbminerais = self.__nbminerais * 1.03
            if self.__niveau == 20:
                print("Vous minez à présent de l'Or")
                self.typeminerais = "Or"
            elif self.__niveau == 40:
                print("Vous minez à présent du Ruby")
                self.typeminerais = "Ruby"
            elif self.__niveau == 60:
                print("Vous minez à présent du Diamant")
                self.typeminerais = "Diamant"
            elif self.__niveau == 80:
                print("Vous minez à présent du Palladium")
                self.typeminerais = "Palladium"
            elif self.__niveau == 100:
                print("Vous minez à présent du Rhodium")
                self.typeminerais = "Rhodium"
            
        else:
            print("Vous n'avez pas l'argent nécessaire, il vous manque : ",temp-self.__money)
            
    def get_temp(self):
        """
        

        Returns
        -------
        Le coût du prochain niveau de mine.

        """
        tempo = 100*self.__niveau**2
        return tempo

        
    def get_vitesse(self):
        """
        

        Returns
        -------
        La vitesse d'action des employés de la mine.

        """
        return self.__vitesse
    
    def __set_vitesse(self,valeur):
        """
        
        
        Set
        ---
        Met la vitesse des employés de la mine à la valeur du paramètre valeur.
        
        """
        self.__vitesse = valeur



mineur = Chemin(1,0,"Argent",0,10,1,0,0,0)


