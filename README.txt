===========================================================
PROJET : PRÉDICTION DE LA RÉUSSITE SUR ARCHE
Master 2 Sciences des Données - Université de Lorraine
Faber Jean-Claude
===========================================================

1. DESCRIPTION
--------------
Le logiciel permet d'analyser les traces numériques des étudiants
sur la plateforme ARCHE pour prédire leur réussite aux examens.
Il compare :
- La régression linéaire simple
- La régression linéaire multiple
- Et l'arbre de décision

2. INSTALLATION
---------------
Pour faire fonctionner l'application, vous devez installer les 
bibliothèques Python nécessaires. Dans un terminal, à la racine 
du projet, tapez la commande suivante :

   pip install -r requirements.txt

3. STRUCTURE DU PROJET
----------------------
- src/          : Contient l'ensemble du code source (.py)
- data/         : Contient les fichiers de données (logs.csv, notes.csv)
- requirements.txt : Liste des versions des packages utilisés

4. LANCEMENT DE L'APPLICATION
-----------------------------
Pour tester l'application, lancez le fichier principal situé 
dans le dossier 'src' :

   python src/main.py

5. MODE D'EMPLOI
----------------
Une fois l'interface ouverte, suivez l'ordre des boutons :
1. "Charger & Nettoyer"
2. "Calculer les indicateurs" 
3. "Explorer les données"
4. "Afficher les graphiques"
5. "lancer les régressions simples"
6. "Lancer la régression multiple"
7.  "Arbre de décision"

Note : Les résultats détaillés des calculs et des régressions 
s'affichent directement dans la console Python.
===========================================================