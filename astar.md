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

```
Dist(s_0) = 0
Vus += s_0
ajouterFP((s_0, O + h(s_0)))
tant que FP non vide:
    s <- extraireMin(FP)
    si s = s_f:
        renvoyer Dist(s) + reconstruire le chemin s_0 -> s_f
    sinon
        pour chaque voisin s' de s:
            s -> s'
            si s' déja vu:
                met on a jour dist(s') + remise en FP
            si s' jamais vu:
                dist(s') = ... + on ajouter en FP

```

Pour l'heursitique on utilise la distance Manhattan (vol d'oiseau)
