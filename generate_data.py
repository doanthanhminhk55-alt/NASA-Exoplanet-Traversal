import pandas as pd
import random

years = list(range(2010, 2025))

facilities = [
    "Kepler",
    "TESS",
    "Ground",
    "James Webb",
    "Hubble",
    "Spitzer"
]

hostnames = [
    "Kepler",
    "TOI",
    "HD",
    "TRAPPIST",
    "WASP",
    "LHS"
]

rows = []

for i in range(4000):

    year = random.choice(years)
    facility = random.choice(facilities)

    host = random.choice(hostnames) + "-" + str(random.randint(1, 999))

    planet_name = host + random.choice(["b","c","d","e","f"])

    radius = round(random.uniform(0.5, 5.0), 2)
    mass = round(random.uniform(0.2, 50), 2)

    planets = random.randint(1, 8)
    stars = random.randint(1, 2)

    rows.append([
        year,
        facility,
        planet_name,
        radius,
        mass,
        host,
        planets,
        stars
    ])

df = pd.DataFrame(rows, columns=[
    "disc_year",
    "disc_facility",
    "pl_name",
    "pl_rade",
    "pl_bmasse",
    "hostname",
    "sy_pnum",
    "sy_snum"
])

df.to_csv("data/exoplanets.csv", index=False)

print("Generated 4000 rows exoplanet data")