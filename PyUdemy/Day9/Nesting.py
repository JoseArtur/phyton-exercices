# A nested diccionary, how you can see, a dictionary inside another
travel_log = {
    "France:": {
        "cities_france": ["Paris", "Lille", "Dijon"],
        "total_visitors": 124,
        "languages_spoken": ["Francais,Anglais,Allemande"]
        },
    "Germany:": {
        "cities_germany": ["Berlin", "Hamburg", "Stuttgart"], 
        "languages_spoken": ["Deutsch", "Englisch"]
        },
}
# A list of diccionaries
travel_loglist = [
    {"country": "France:",
     "cities_france": ["Paris", "Lille", "Dijon"],
     "total_visitors":124, 
     "languages_spoken":["Francais,Anglais,Allemande"],
     },
    {"country": "Germany:", 
    "cities_germany": ["Berlin", "Hamburg", "Stuttgart"], 
    "languages_spoken":["Deutsch", "Englisch"],
    },
]
