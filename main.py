from worker import*


"""
MAIN
"""

print("Vous êtes le propriétaire d'une mine et vous devez gérer vos employés.\n")
time.sleep(2)
print("Vous pouvez augmenter le niveau de vos employés pour augmenter les capacités de la mine.\n")
time.sleep(2)

nom = input("Mais avant de pouvoir commencer veuillez nous donner votre pseudo : ")

print("\nVotre niveau est pour l'instant de 0 good luck ",nom,"!\n")

protemp = len(nom) + 2




def main():
    demand = input("que voulez vous faire ? (/help)\n")
    if demand == "/all":
        nb_mine = int(input("combien de fois voulez-vous miner ?\n"))
        for i in range(nb_mine):
            mineur.miner()
            mineur.transporter()
            mineur.transferer()
            mineur.money()
        main()
    
    elif demand == "/miner":
        nb_mine = int(input("combien de fois voulez-vous miner ?\n"))
        for i in range(nb_mine):
            mineur.miner()
        main()
    
    elif demand == "/liftier":
        mineur.transporter()
        main()
        
    elif demand == "/chariot":
        mineur.transferer()
        main()
        
    elif demand == "/sell":
        mineur.money()
        main()
        
    elif demand == "/money":
        print("Vous possédez {}.".format(mineur.get_money()))
        main()
        
    elif demand == "/leave":
        print("Pendant cette partie vous avez miné {}".format(mineur.get_kgtotal()),"kg de minerais.")
        print("arrêt du jeu...")
        time.sleep(3)
        quit()
        
    elif demand == "/up":
        mineur.up()
        main()
        
    elif demand == "/level":
        print("Votre mine est au niveau {}.".format(mineur.get_niveau()),"prochain niveau coûte : {}".format(mineur.get_temp()))
        main()
        
    elif demand == "/profil":
        print("=================",nom,"=================\n| Mine level : {}".format(mineur.get_niveau()),"\n| Money : {}".format(mineur.get_money()),"\n| Vitesse : {}".format(mineur.get_vitesse()),"\n| Total miné : {}".format(mineur.get_kgtotal()),"kg de minerais")
        print("=================",protemp*"=","=================\n",sep="")
        main()
        
    elif demand == "/help":
        print("================== /help ==================\n| Faire tout le chemin : /all\n| Miner : /miner\n| Transporter : /liftier\n| Transferer : /chariot\n| Vendre les minerais : /sell\n| Regarder votre nombre d'argent : /money\n| Regarder votre niveau de mine : /level\n| Regarder votre profil : /profil\n| Augmenter votre niveau de mine : /up\n| Quitter le jeu : /leave\n===========================================")
        main()
        
    else:
        print("Commande inexistante")
        main()
    
        
main() 
