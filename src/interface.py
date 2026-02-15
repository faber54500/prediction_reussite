import tkinter as tk
from tkinter import messagebox
from load import charger_donnees
from cleaner import nettoyage_donnees
from features import calculer_indicateurs
from regression import analyser_regressions
from regression_multiple import analyser_regression_multiple
from view import afficher_graphiques
from arbre_de_decision import entrainer_arbre_decision
from exploration import exploration_data, voir_les_absents

class ApplicationAnalyse(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Prédiction de Réussite - ARCHE")
        self.geometry("450x350")

        # Titre dans la fenêtre
        tk.Label(self, text="Analyse des logs de connexion", font=("Arial", 14, "bold")).pack(pady=10)

        # Bouton 1 : Charger et Nettoyer les données
        tk.Button(self, text="1. Charger & nettoyer les données", command=self.etape_nettoyage, width=35, bg="#FFF3E0").pack(pady=5)

        # Bouton 2 : Calculer les indicateurs
        tk.Button(self, text="2. Calculer les indicateurs", command=self.etape_calcul, width=35, bg="#F3E5F5").pack(pady=5)

        #  Bouton 3 : Exploration des données
        tk.Button(self, text="3. Explorer les données ", command=self.etape_exploration, width=35,bg="#E0F2F1").pack(pady=5)

        # Bouton 4 : Voir les Graphiques
        tk.Button(self, text="4. Afficher les graphiques", command=self.etape_visu, width=35, bg="#D1E8FF").pack(pady=5)

        # Bouton 5 : Régression simple
        tk.Button(self, text="5. Lancer les régressions simples", command=self.etape_stats, width=35, bg="#D1FFD1").pack(pady=5)

        # Bouton 6 : Régression Multiple
        tk.Button(self, text="6. Lancer la régression multiple", command=self.etape_stats_multiple, width=35, bg="#FFFFD1").pack(pady=5)

        #  BOUTON 7 : Arbre de décision
        tk.Button(self, text="7. Arbre de décision ", command=self.etape_arbre, width=35, bg="#D1C4E9").pack(pady=5)

        # Variables pour stocker les données entre les étapes
        self.df_final = None

    def etape_nettoyage(self):
        # On récupère les données brutes (df_logs, df_notes)
        df_logs, df_notes = charger_donnees()

        if df_logs is not None:
            # On stocke les données nettoyées dans l'application (self.df_logs_clean, self.df_notes_clean)
            self.df_logs_clean, self.df_notes_clean = nettoyage_donnees(df_logs, df_notes)
            messagebox.showinfo("Succès", "Données chargées et nettoyées !")
        else:
            messagebox.showerror("Erreur", "Fichiers introuvables.")

    def etape_exploration(self):
        # Vérification que les données nettoyées existent
        if hasattr(self, 'df_logs_clean'):
            print("\n--- EXPLORATION DES DONNÉES ---")
            exploration_data(self.df_logs_clean, self.df_notes_clean)
            voir_les_absents(self.df_logs_clean, self.df_notes_clean)
            messagebox.showinfo("Exploration", "L'exploration a été affichée dans la console.")
        else:
            messagebox.showwarning("Attention", "Veuillez d'abord charger et nettoyer les données.")

    def etape_calcul(self):
        # Utilisation des noms complets pour le calcul des indicateurs
        if hasattr(self, 'df_logs_clean'):
            self.df_final = calculer_indicateurs(self.df_logs_clean, self.df_notes_clean)
            messagebox.showinfo("Succès", f"Indicateurs calculés pour {len(self.df_final)} étudiants.")
        else:
            messagebox.showwarning("Attention", "Veuillez d'abord charger les données.")

    def etape_visu(self):
        if self.df_final is not None:
            afficher_graphiques(self.df_final)
        else:
            messagebox.showwarning("Attention", "Calculs non effectués.")

    def etape_stats(self):
        if self.df_final is not None:
            analyser_regressions(self.df_final)
            messagebox.showinfo("Analyse", "Résultats régressions simples générées dans la console.")
        else:
            messagebox.showwarning("Attention", "Données non prêtes.")

    def etape_stats_multiple(self):
        if self.df_final is not None:
            analyser_regression_multiple(self.df_final)
            messagebox.showinfo("Analyse Multiple", "Résultat régression multiple généré dans la console.")
        else:
            messagebox.showwarning("Attention", "Données non prêtes.")

    def etape_arbre(self):
        if self.df_final is not None:
            entrainer_arbre_decision(self.df_final)
            messagebox.showinfo("Arbre", "L'Arbre de Décision a été généré avec succès !")
        else:
            messagebox.showwarning("Attention", "Données non prêtes.")

if __name__ == "__main__":
    app = ApplicationAnalyse()
    app.mainloop()