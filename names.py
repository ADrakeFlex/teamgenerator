import random

def generate_team_name():
    adjectives = [
        "Giant",
        "Average",
        "Tiny",
        "Magnificent",
        "Marvellous",
        "Crazy",
        "Established",
        "Burbling",
        "Confident",
        "Zimbabwean",
        "Ingolrious",
        "Ravishing",
        "Indubious",
        "Dubious",
        "Realistic",
        "Unrealistic",
        "Loquacious",
        "Luminous",
        "Sclerotic",
        "Withering",
        "Feckless",
        "Boorish"
    ]

    nouns = [
        "Cats",
        "Dogs",
        "Bears",
        "Pelicans",
        "CuntSmashers",
        "FixEngines",
        "Tigers",
        "Bananas",
        "Capybaras",
        "Rowans",
        "FartBlasters",
        "PicklePickers",
        "PeckerHandlers",
        "Rats",
        "Hullaballoos",
        "Wippersnappers",
        "Poppycocks",
        "Otters",
        "FartSplitters",
        "PoopCollectors"
    ]

    return "The " + random.choice(adjectives) + " " + random.choice(nouns)
