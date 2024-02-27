# A-star algorithm

Summary of the A star algorithm and its implementation in this project

## Inputs:

- G = (S, A) a weighted graph with strictly positive weights
- s_0 le starting summit
- s_f le destination/target peak
- h : S -> R+ heuristics

## Output:

- d(s_0, s_f)
- the shortest route from s_0 to s_f

We define the following parameters

- Vus : the set of vertices seen
- Dist : association s -> dist(s_0, s) common distance

### Rq: for a small graph we use an array and for a large graph we use a list.

- FP : a priority queue based on distance (s_0 ->?? q_f) = dist(s_0, s) + h(s)
- Père : association s -> père(s)

## Algorithm

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

For heuristics, we use the Manhattan distance (as the crow flies)