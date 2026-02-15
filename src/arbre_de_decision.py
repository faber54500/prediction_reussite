import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score


from load import charger_donnees
from cleaner import nettoyage_donnees
from features import calculer_indicateurs


def entrainer_arbre_decision(df):
    if df is None:
        print(" ARRÊT : Les données sont manquantes pour l'arbre de décision.")
        return
    """
     Fonction transforme les notes en classes (0 ou 1)
     et entraîne un arbre de décision pour prédire la réussite.
    """
    print(" ANALYSE PAR ARBRE DE DÉCISION")

    #  colonne 'reussite' : 1 si note >= 10, sinon 0
    df_arbre = df.copy()
    # liste vide pour stocker nos 0 et 1
    resultats = []

    #  chaque note est transformée une à une
    for note in df_arbre['note']:
        if note >= 10:
            resultats.append(1)  # Réussite
        else:
            resultats.append(0)  # Échec

    # la liste est ajoutée comme une nouvelle colonne dans le tableau
    df_arbre['reussite'] = resultats

    # selection des paramètres
    indicateurs = ['nb_clics', 'nb_jours', 'nb_composants', 'nb_contextes', 'temps_total_sec', 'nb_tests']
    X = df_arbre[indicateurs]
    y = df_arbre['reussite']

    #  profondeur limité à 3 pour avoir une image  lisible
    arbre = DecisionTreeClassifier(max_depth=3, random_state=42)
    arbre.fit(X, y)

    # Evaluation
    predictions = arbre.predict(X)
    precision = accuracy_score(y, predictions)
    print(f"Précision du modèle (Accuracy) : {precision:.2f}")

    # Visualisation de l'arbre
    plt.figure(figsize=(15, 8))
    plot_tree(arbre,
              feature_names=indicateurs,
              class_names=['Échec', 'Réussite'],
              filled=True,
              rounded=True,
              fontsize=10)
    plt.title("Arbre de Décision : Stratégies de réussite sur ARCHE")

    # Sauvegarde de l'image
    plt.savefig("arbre_decision.png")
    print("L'image de l'arbre a été sauvegardée sous 'arbre_decision.png'")

    plt.show()

    return arbre


if __name__ == "__main__":
    from load import charger_donnees
    from cleaner import nettoyage_donnees
    from features import calculer_indicateurs

     # 1. Préparation des données
    df_logs, df_notes = charger_donnees()
    df_logs_clean, df_notes_clean = nettoyage_donnees(df_logs, df_notes)
    df_final = calculer_indicateurs(df_logs_clean, df_notes_clean)

    # 2. Lancement de l'analyse
    entrainer_arbre_decision(df_final)