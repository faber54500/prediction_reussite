import matplotlib.pyplot as plt


def afficher_graphiques(df):
    print("\n--- GÉNÉRATION DES GRAPHIQUES ---")

    # On crée une grande fenêtre pour mettre les 5 graphiques ensemble
    # 2 lignes, 3 colonnes (la 6ème case restera vide)
    plt.figure(figsize=(15, 10))

    # 1. VOLUME
    plt.subplot(2, 3, 1)
    plt.scatter(df['nb_clics'], df['note'], color='blue')
    plt.title('Note vs Volume (clics)')
    plt.xlabel('Nombre de clics')
    plt.ylabel('Note / 20')

    # 2. RÉGULARITÉ
    plt.subplot(2, 3, 2)
    plt.scatter(df['nb_jours'], df['note'], color='red')
    plt.title('Note vs Régularité (jours)')
    plt.xlabel('Nombre de jours')
    plt.ylabel('Note / 20')

    # 3. DIVERSITÉ
    plt.subplot(2, 3, 3)
    plt.scatter(df['nb_composants'], df['note'], color='green')
    plt.title('Note vs Diversité (outils)')
    plt.xlabel('Nombre d\'outils')
    plt.ylabel('Note / 20')

    # 4. ÉTENDUE
    plt.subplot(2, 3, 4)
    plt.scatter(df['nb_contextes'], df['note'], color='orange')
    plt.title('Note vs Étendue (ressources)')
    plt.xlabel('Nombre de chapitres')
    plt.ylabel('Note / 20')

    # 5. TEMPS
    plt.subplot(2, 3, 5)
    # On divise par 60 pour avoir des minutes, c'est plus simple à lire
    plt.scatter(df['temps_total_sec'] / 60, df['note'], color='purple')
    plt.title('Note vs Temps (minutes)')
    plt.xlabel('Temps total en min')
    plt.ylabel('Note / 20')

    # 6. PERFORMANCE (Tests)
    plt.subplot(2, 3, 6)
    plt.scatter(df['nb_tests'], df['note'], color='teal', alpha=0.6)
    plt.title('Note vs Performance (tests)')
    plt.xlabel('Nombre de tests effectués')
    plt.ylabel('Note / 20')

    # ajuste l'espacement pour que les titres ne se chevauchent pas
    plt.tight_layout()

    print("Affichage terminé. Fermez la fenêtre du graphique pour quitter.")
    plt.show()