import pandas as pd
import os

# chemin vers les fichiers
def charger_donnees():
    chemin_logs= "../data/logs.csv"
    chemin_notes="../data/notes.csv"

# message d'erreur si on ne trouve pas les fichiers
    if not os.path.exists(chemin_logs) or not os.path.exists(chemin_notes):
        if not os.path.exists(chemin_logs):
            print ("ERREUR : Le fichier des logs est manquant")
            print ("Vérifie que tu as bien copié les fichiers dans data")
        if not os.path.exists(chemin_notes):
            print("ERREUR : Le fichier des notes est manquant")
            print("Vérifie que tu as bien copié les fichiers dans data")
            return None, None

    else :
        try :#lecture des fichiers
            df_logs= pd.read_csv(chemin_logs)
            df_notes= pd.read_csv(chemin_notes)
            print ("les données ont été chargées avec succès!")
            print (f"Fichier logs :{len(df_logs)} lignes lues")
            print(f"Fichier notes :{len(df_notes)} lignes lues")

            return df_logs, df_notes

        except FileNotFoundError:
            print("ERREUR : Le fichier est introuvable vérifie si le dossier data est présent?")
            return None, None

        except pd.errors.EmptyDataError:
            print(" ERREUR : Le fichier CSV est vide ! ajoute le fichier")
            return None, None

        except PermissionError:
            print(" ERREUR : Le fichier est déjà ouvert dans un autre programme merci de le fermer pour que cela fonctionne")
            return None, None

        except Exception as erreur_inconnue:
             print(f" ERREUR IMPRÉVUE lors du chargement des données: {erreur_inconnue}")
             return None, None

if __name__ == "__main__":
    charger_donnees()