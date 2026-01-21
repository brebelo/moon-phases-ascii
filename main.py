from datetime import datetime
import math


#date d'aujourd'hui, format yyyy-mm-dd
#print("la date d'aujourd'hui est", datetime.today().strftime("%Y-%m-%d"))


def entree_utilisateur():
    print("Bonjour! bienvenue dans cet outil CLI qui permet de voir la phase de la Lune quotidiennement :)\n")
    print("HELP : --today (affiche la date d'aujourd'hui) | --date puis dd-mm-yyyy (affiche la date souhaité) | --quit (fin du programme)\n\n")
    
    while True:
        entree_cmd = input()
        if entree_cmd == "--today":
            print("Vous avez choisi la date d'aujourd'hui : ")
            daydate = datetime.today()
            illumination = calcul_phase(daydate)
            print(f"Illumination: {illumination:.2f}%")
        elif entree_cmd == "--date":
            print("merci de rentrez la date souhaitée: ")
            date_saisie = input()
            date_objet = datetime.strptime(date_saisie, "%d-%m-%Y")
            print("Vous avez choisi la date:", date_objet)
            illumination = calcul_phase(date_objet)
            print(f"Illumination : {illumination:.2f}%")

        elif entree_cmd == "--quit":
            print("Fin du programme")
            break
        else:
            print("commande inconnue")

            

def calcul_phase(date_objet):

    nouvelle_lune_reference = datetime(2000, 1, 6) # 6 janvier 2000
    delta = date_objet - nouvelle_lune_reference
    jours_ecoules = delta.total_seconds() / (24 * 3600) # conversion des secondes en jours

    cycle_lunaire = 29.53058867
    age_lune = jours_ecoules % cycle_lunaire

    f = (1 - math.cos(age_lune * (2 * math.pi / cycle_lunaire))) / 2 * 100

    return f



entree_utilisateur()