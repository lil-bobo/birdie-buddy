# Birdie Buddy

Ce projet est le sujet central de mon TIPE (session 2023/2024).

# Description

Le golf est le jeu individuel le plus répandu aux État-Unis. Il requiert précision, concentration et technicité ce qui rend le sport compliqué d'accès. C'est pourquoi j'ai pris l'initiative de créer un programme assistant pour aider les débutants à mieux apercevoir les coups et opportunités pour évoluer rapidemment. Comment aider les jeunes golfeurs à s'améliorer plus vite ?

# Démarche

Pour résoudre ce problème, j'exploite les différents algorithmes de recherche du chemin le plus court dans un graphe. Le graphe utilisé sera un graphe grille (pour l'instant 2D) représentant le terrain de golf sur lequel on implémente deux algorithmes : le parcours en largeur et l'algorithme de A\*.
Le mouvement de la balle est une chute libre élémentaire : cette modélisation permet de focaliser l'objet travail sur l'implémentation des algorithmes.

# Polygones et Maillages

Afin de rendre plus réaliste la simulation, plusieurs outils numériques existent pour représenter le relief en informatique. Parmis ces derniers : le maillage semble être une solution adéquate.

# Suivi de recherches

Je m'interroge actuellement sur le concept de maillage. Comment représenter une maille et comment s'y orienter.
J'envisage utiliser le logiciel d'édition de scène 3D Blender car il est gratuit et offre plusieurs formats de fichier.
Parmis les formats de fichier:

- STL
- PLY
- OBJ
- Collada

Le Wavefront OBJ est le plus efficace car il peut contenir des informations sur les polygons et la texture de ces derniers. Le "code" .obj est ASCII donc facile à visualiser. On va maintenant modéliser un terrain de golf dans le logiciel Blender qu'on exportera en .obj puis on cherchera une méthode pour exploiter les données du terrain et y appliquer des lois physiques pour le mouvement de la balle de golf.

On commence par un terrain plat, avec éventuellement quelques courbures, car on veut d'abord pouvoir faire comprendre au programme à quoi ressemble de terrain de golf.

# TODO

[] Modéliser un terrain de golf minimal (i.e. pas trop complexe) dans Blender puis l'exporter au format obj.

[] Importer les informations du fichier obj dans un programme C (ou C++)

[] Commencer à traduire le code Python en code C (ou C++)

[] Envisager une implémentation d'une interface graphique OpenGL (pour voir à quoi ressemblent les coups conseillés par l'ordinateur)
