import numpy as np
import matplotlib
import matplotlib.pyplot as plt


class Terrain:
    def __init__(self, width, length, ratio, depart, arrivee):
        self.width = width
        self.length = length
        self.ratio = ratio
        self.depart = depart
        self.arrivee = arrivee

class Obstacle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

from random import randint
from math import sqrt, floor

offset = 1

def creer_obstacles(terrain, n):
    obstacles = []
    for _ in range(n):
        x = randint(offset, terrain.width * 10 - offset) / 10
        y = randint(offset, terrain.length * 10 - offset) / 10
        while any(sqrt((obstacle.x - x <= obstacle.r) + (obstacle.y - y <= obstacle.r)) for obstacle in obstacles):
            x = randint(offset, terrain.width * 10 - offset) / 10
            y = randint(offset, terrain.length * 10 - offset) / 10
            # print("DEBUG")
        mini = min(sqrt((x - obstacle.x)**2 + (y - obstacle.y)**2) for obstacle in obstacles) if obstacles else 1
        mini = np.log(1 + mini)
        obstacles.append(Obstacle(x, y, mini))
        print((x, y, mini))
    return obstacles

def creer_grille(terrain, obstacles):
    # grille = [0] * ratio * terrain.width * ratio * terrain.length
    # grille = np.zeros(ratio * terrain.width * ratio * terrain.length)
    grille = np.zeros((terrain.length * terrain.ratio, terrain.width * terrain.ratio))
    for obstacle in obstacles:
        for t in range(0, 360, 1):
            centre_x = obstacle.x * terrain.ratio
            centre_y = obstacle.y * terrain.ratio
            rayon = obstacle.r * terrain.ratio
            for i in range(100 + 1):
                x = centre_x + np.cos(t) * rayon * i / 100
                y = centre_y + np.sin(t) * rayon * i / 100
                x = floor(x)
                y = floor(y)
                if 0 <= x < terrain.width * terrain.ratio and 0 <= y < terrain.length * terrain.ratio:
                    grille[y][x] = 1
    depart_x, depart_y = terrain.depart
    arrivee_x, arrivee_y = terrain.arrivee
    grille[floor(depart_y * terrain.ratio)][floor(depart_x * terrain.ratio)] = 2
    grille[floor(arrivee_y * terrain.ratio)][floor(arrivee_x * terrain.ratio)] = 3
    return grille

def upscale(vec, scale):
    x, y = vec
    return (int(scale * x), int(scale * y))

def parcours_en_largeur(terrain, grille):
    visited = np.zeros((terrain.length * terrain.ratio, terrain.width * terrain.ratio))
    queue = [(upscale(terrain.depart, terrain.ratio), [upscale(terrain.depart, terrain.ratio)])]
    while queue:
        position, path = queue.pop(0)
        x, y = position
        if position == upscale(terrain.arrivee, terrain.ratio):
            return path
        for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < terrain.width * terrain.ratio and 0 <= ny < terrain.length * terrain.ratio and grille[ny][nx] != 1 and not visited[ny][nx]:
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited[ny][nx] = 1
    return queue

def reconstruct_path(parents, goal, start):
    path = [goal]
    current = goal
    while current != start:
        current = parents[current]
        path.insert(0, current)
    return path

def norme(dx, dy):
    return abs(dx) + abs(dy)

import heapq

def astar(terrain, grille):
    parents = {}
    def heuristique(s1, s2):
        return abs(s1[0] - s2[0]) + abs(s1[1] - s2[1])
    start = upscale(terrain.depart, terrain.ratio)
    goal = upscale(terrain.arrivee, terrain.ratio)
    queue = []
    vus = set()
    heapq.heappush(queue, (heuristique(start, goal), start, 0))
    while queue:
        # queue.sort(reverse=True, key=lambda x: x[0])
        _, s, dist = heapq.heappop(queue)
        if s == goal:
            # renvoyer dist, vus etc
            return (reconstruct_path(parents, goal, start)), vus
        else:
            voisins = []
            for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1), (-1, 1), (-1, -1), (1, -1), (1, 1)]:
                new_x, new_y = s[0] + dx, s[1] + dy
                if 0 <= new_x < terrain.width * terrain.ratio and 0 <= new_y < terrain.length * terrain.ratio:
                    if grille[new_y][new_x] != 1:
                        voisins.append((new_x, new_y))
            for v in voisins:
                if v not in vus:
                    parents[v] = s
                    vus.add(v)
                    d = norme(dx, dy)
                    heapq.heappush(queue, (dist + d + heuristique(v, goal), v, dist + d))
    return None

theta = np.pi / 4 # radians
m = 46 / 1000 # 46 grammes en kilogrammes
g = 9.81
p = m * g * (np.cos(theta) - np.sin(theta))

def chute_libre(terrain, chemin):
    v_0 = 41.5 # m/s
    g = 9.81 # m/s/s
    dist_max = 2 * v_0 * v_0 / g / g
    # dist_max = 2
    x, y = chemin[0]
    rest = [(x, y)]
    destination = upscale(terrain.arrivee, terrain.ratio)
    while (x, y) != destination:
        if dist_max < sqrt((x - terrain.arrivee[0] * terrain.ratio)**2 + (y - terrain.arrivee[1] * terrain.ratio)**2):
            moins_de_points = filter(lambda p: sqrt((p[0] - x)**2 + (p[1] - y)**2) <= dist_max, chemin)
            moins_de_points = list(moins_de_points)
            # on garde que le points qui sont accessible depuis (x, y)
            pt = min(
                moins_de_points,
                key=lambda v: sqrt((v[0] - terrain.arrivee[0] * terrain.ratio)**2 + (v[1] - terrain.arrivee[1] * terrain.ratio)**2)) if moins_de_points else (x, y)
            x, y = pt
            rest.append(pt)
        else:
            x, y = upscale(terrain.arrivee, terrain.ratio)
            rest.append((int(x), int(y)))
    return rest

# fig, ax = plt.subplots()

terrain = Terrain(10, 20, 30, (8, 2), (1.2, 18))

obstacles = [
    Obstacle(1, 2, 2),
    Obstacle(6, 7, 3),
    Obstacle(7, 18, 4),
    Obstacle(1.5, 12, 1)
]

res = creer_grille(terrain, obstacles)
# chemin = parcours_en_largeur(terrain, res)
# for (x, y) in chemin:
#     res[y][x] = 2

meilleur_chemin, vus = astar(terrain, res)
# print(meilleur_chemin)
# for (x, y) in meilleur_chemin:
#     res[y][x] = 4
# chute = chute_libre(terrain, chemin)
# for (x, y) in chute:
#     res[y][x] = 3
# plt.imshow(res, origin='lower')
# plt.show()
# plt.savefig('foo.png')

# On va fixer les obstacles pour l'instant : FAIT

# Maintenant on va chercher le plus court chemin : FAIT

# REMARQUE: LES INDICES SONT INVERSES CAR LES MATRICES FONT DABORD NB LIGNES ET APRES NB COLONNES
    
# On s'intéresse désormais à la trajectoire de la balle de golf.
    
"""
    On va tracer une cercle de centre (x,y) et on cherche l'intersection de ce cercle avec le chemin tracé avec le parcours en largeur. Dans un repère sphérique, on suppose que l'angle theta est fixe et vaut 45 deg (pi/4 rad).
"""

# Equation de chute libre, pas de frottements pour l'instant

# On a implémenté l'algorithme de parcours en largeur et il est évident que ce n'est pas le meilleur. C'est pourquoi on va d'emblée commencer l'implémentation de l'algorithme A étoile