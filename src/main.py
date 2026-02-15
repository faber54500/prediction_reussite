# Importation de la classe ApplicationAnalyse depuis ton fichier interface.py
from interface import ApplicationAnalyse

def main():
    # Création de l'objet mon_interface
    mon_interface = ApplicationAnalyse()

    # Lancement de la boucle de l'application
    print("=== L'INTERFACE DE PRÉDICTION EST PRÊTE ===")
    mon_interface.mainloop()

    # Message affiché une fois que l'utilisateur ferme la fenêtre
    print("=== FERMETURE DE L'APPLICATION ===")

if __name__ == "__main__":
    # Appel de la fonction principale pour démarrer le projet
    main()