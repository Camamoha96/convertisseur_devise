print( "_____ CONVERTISSEUR MONNAIE _____ ")

# 📊 Dictionnaire contenant les taux de change entre différentes devises
devise = {
        'XAF':{'EUR':0.0015 , 'USD':0.0018 , 'GBP':0.0013 ,'BTC':0.000000017 },
        'EUR':{'XAF':655.95 , 'USD':1.15 , 'GBP':0.85 ,'BTC':0.000011 },
        'USD':{'EUR':0.87 , 'XAF':569.91 , 'GBP':0.74 ,'BTC':0.0000095 },
        'GBP':{'EUR':1.17 , 'USD':1.35 , 'XAF':767.26 ,'BTC':0.000013 },
        'BTC':{'EUR':91244 , 'USD':105021 , 'XAF':59852130 ,'GBP':78008 }}

# 📊 Dictionnaire contenant les taux de change entre différentes devises

def demande_devise():
    monnaie_actuel = ''
    liste_devise = list(devise.keys())  # Création de la liste des devises disponibles

    while monnaie_actuel not in liste_devise:   

        try:
            monnaie_actuel = input(f'Quel est votre devise actuel ({liste_devise}): ').upper()
            
            if monnaie_actuel not in liste_devise:
                raise ValueError(f'entrer une devise correcte et disponible ({liste_devise}) ')
            break
    
        except ValueError as e:
            print(f'erreur , {e} ')
    
    # Passe à l'étape suivante avec la devise source choisie

    demande_monnaie_actuelle(liste_devise , monnaie_actuel)

#_______________________________________________________________

# 🔁 Étape 2 : Demande à l'utilisateur la devise cible pour la conversion

def demande_monnaie_actuelle(liste_devise , monnaie_actuel):
    
    monnaie_echange = ''
    copie_liste = liste_devise.copy()  # Copie de la liste des devises pour ne pas altérer l'originale
    if monnaie_actuel in copie_liste:
            copie_liste.remove(monnaie_actuel)  # Retirer la devise source de la liste cible
        
    while monnaie_echange not in copie_liste:
            try:
                monnaie_echange = input(f'Quel est la devise de sortie ({copie_liste}): ').upper()
        
                if monnaie_echange not in liste_devise:
                    raise ValueError(f'entrer une devise correcte et disponible ({copie_liste}) ')
                break
    
            except ValueError as erreur:
                print(f'erreur {erreur}')
    
    # Passe à l'étape suivante avec les deux devises sélectionnées

    demande_montant_conversion(monnaie_actuel , monnaie_echange )

# #______________________________________________________

# 🔁 Étape 3 : Demande le montant à convertir et affiche le résultat

def demande_montant_conversion(monnaie_actuel , monnaie_echange):
    while True:
        try:
                montant = input('Montant a convertir: ')
                montant_float =float(montant)  # Conversion en float pour accepter les décimales
                if montant_float <= 0:
                    raise ValueError('"Le montant doit être supérieur à zéro.')
                break
        except ValueError:
                print(f'Veuillez entrer un **nombre valide positif** svp 🚨')

    # 💱 Calcul de la conversion avec le taux correspondant
        
    taux_echange = devise[monnaie_actuel][monnaie_echange]
    resultat =  montant_float * taux_echange 
    print(f'{montant}{monnaie_actuel} ----> {(resultat):.0F}{monnaie_echange} ')

    # Propose de quitter ou de refaire une conversion
    quitter_convertisseur()

#________________________________
# 🔁 Étape 4 : Quitter ou relancer le convertisseur

def quitter_convertisseur():
    q = ''

    # Boucle de saisie jusqu’à ce qu’une réponse valide soit donnée
    while q.upper() != 'n' and q.upper() != 'o':
        q = input('Voulez vous quitter (o/n) ?').upper()

        if q == 'O'.upper():
         print('Merci d\'avoir utilisé notre logiciel💱')
         exit()
        else:
             demande_devise()  # Redémarre le programme
         
demande_devise()

print('BRAVO')