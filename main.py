import csv
import os
from random import shuffle

base_dir = os.path.dirname(os.path.abspath(__file__))

def lire_csv() -> dict:
    places_binomes = {}
    files = os.listdir('./eleves')
    for filename in files:
        with open(os.path.join(base_dir, 'eleves', filename), 'r') as f:
            reader = csv.reader(f, delimiter=',')
            places_binomes[filename] = [x for x in reader]
    return places_binomes

def calculer_poids(places_binomes: dict) -> list:
   poids = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
   for places in places_binomes.values():
       for i in range(4):
           for j in range(4):
               poids[i][j] += int(places[i][j])
   return poids

def creer_plan(places_binomes: dict, poids: list):
    plan = [
            ['','','',''],
            ['','','',''],
            ['','','',''],
            ['','','',''],
            ]
    items = list(places_binomes.items())
    shuffle(items)
    for k, v in items:
        smallest_value = 999
        smallest_i = 0
        smallest_j = 0
        for i in range(4):
            for j in range(4):
                if (poids[i][j] < smallest_value) and (not v[i][j] == '0') and (plan[i][j] == ''):
                    smallest_value = poids[i][j]
                    smallest_i, smallest_j = i, j
        if smallest_value == 999:
            for i in range(4):
                for j in range(4):
                    if (plan[i][j] == ''):
                        smallest_i, smallest_j = i, j
        plan[smallest_i][smallest_j] = k
    return plan


donnees = lire_csv()
poids = calculer_poids(donnees)
plan = creer_plan(donnees, poids)
print(plan)
