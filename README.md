# Prix Goncourt 2025
L'application est un programme console en Python permettant aux utilisateurs d'afficher les livres de chaque sélection du prix Goncourt 2025,  
Permettre à un président du jury d'indiquer les livres des sélections,  
Et également lui permettre d'indiquer le nombre de votes pour le dernier tour.  

-----

## Documents :
Le projet est séparé en 3 documents principaux :
- bdd : Export des éléments dans la base de donnée,
- doc -> uml (fichiers + png) :
  - Diagramme de classe,
  - Diagramme de cas d'utilisation,
  - Diagrammes de séquences.
- goncourt : Dossier de l'application Python.

## Téléchargement et versions :
Le programme est écrit en Python 3.13 et utilise plusieurs modules (mentionnés dans le fichiers requirements.txt),  

-----

## Fonctionnement :
Le programme demande de se connecter soit en tant qu'utilisateur ou admin en écrivant 0 ou 1.  
En mode utilisateur le programme affiche la sélection disponible des livres,  
L'admin (une fois connecté) va pouvoir indiquer les livres qui passeront à la sélection 2 et 3,  
Le lauréat est choisit par le jury lors de la finale et les 4 finalistes sont affichés par nombre de vote (décroissant).
