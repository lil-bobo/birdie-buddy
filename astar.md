# Algorithme A étoile

Résumé de ce qu'est l'algorithme de A star pour son implémentation dans ce projet

## Entrées:
- G = (S, A) un graphe pondéré à poids positifs strictements
- s_0 le sommet de départ
- s_f le sommet d'arrivée/cible
- h : S -> R+ l'heuristique

## Sortie:

- d(s_0, s_f)
- le plus court chemin de s_0 à s_f

On définit les paramètres suivants

- Vus : l'ensemble des sommets vus
- Dist : l'association s -> dist(s_0, s) distance commune

### Rq: pour un petit graphe on utilise un tableau et pour un grand graphe on utilise une liste

- FP : une file de priorité selon la distance (s_0 ->?? q_f) = dist(s_0, s) + h(s)
- Père : association s -> père(s)

## Algorithme

Dist(s_0) = 0