import requests
from jyquickhelper import JSONJS
from datetime import datetime, timedelta
import sys
from pprint import pprint

token_auth = 'd10d24d4-5dd4-4370-827a-8083ff217b34'
id_paris = 'stop_area:SNCF:87686006'

def page_gares(numero_page) :
    return requests.get(
        ('https://api.sncf.com/v1/coverage/sncf/stop_areas?start_page={}').format(numero_page),
        auth=(token_auth, ''))
    
def convertir_en_chaine(dt) :
    ''' on convertit en chaîne de caractères un datetime'''
    return datetime.strftime(dt, '%Y%m%dT%H%M%S')

def convertir_en_temps(chaine) :
    ''' on convertit en date la chaine de caractères de l API'''
    return datetime.strptime(chaine.replace('T',''),'%Y%m%d%H%M%S')
    
#page_initiale = page_gares(4).json()
#print(page_initiale)
#item_per_page = page_initiale.json()['pagination']['items_per_page']
#total_items = page_initiale.json()['pagination']['total_result']


# on fait une boucle sur toutes les pages suivantes
print_done = {}

##########################################GARE ACCESSIBLE DEPUIS LYON ########################################################################



#def depart_gare(id_gare):
#    return requests.get(
 #       ('https://api.sncf.com/v1/coverage/sncf/stop_areas/'
 #        ''+id_gare+'/departures'),
  #       auth=(token_auth, '')).json()
    
    
now = datetime.now()
dt = now + timedelta(14)  # dans deux semaines

date_depart = convertir_en_chaine(dt)
    
departs_paris = requests.get(
    ('https://api.sncf.com/v1/coverage/sncf/stop_areas/stop_area:SNCF:'
     '87686006/departures?from_datetime={}').format(
        date_depart), auth=(token_auth, '')).json()
    
#print(departs_paris) 
#clear
# cdepart_gare(id_lyon)
JSONJS(departs_paris)

###########################################################################################

def trouver_destination_tgv(origine, datetime) :
    '''Permet d avoir les 10 prochains départs d une gare donnée '''
    return requests.get('https://api.sncf.com/v1/coverage/sncf/stop_areas/{}/' \
                        'departures?from_datetime={}&forbidden_uris[]=physical_mode:RapidTransit'.format(origine, datetime) ,
                        auth=(token_auth, '')).json()
    


""" def to_filetrouver_destination_tgv(origine, datetime):
# We open the log file in writting mode
    with open('myLoglsFile.json', 'w') as f:
    # We redirect the 'sys.stdout' command towards the descriptor file
     sys.stdout = f
     print(trouver_destination_tgv(id_paris, convertir_en_chaine(now))) 

    
to_filetrouver_destination_tgv(id_paris, convertir_en_chaine(now)) """

###########################################################################################

""" url  = trouver_destination_tgv(id_paris, convertir_en_chaine(now))

print(url['departures']) """


""" def garesaccessible(origine, date_min, date_max):
     '''Permet d avoir les gares pour lesqeulles il y a un train de départ entre date_min et date_max à partir de la gare d'origine et avoir leur nombres  '''
     " Contrainte : date_min est supérieure à la date actuelle "
     
     tochain_datemin = convertir_en_chaine(date_min)
     tochain_datemax = convertir_en_chaine(date_max)
     
     
     " Train qui a l'horaire max pour recommencer a partir de ce point quand on réutilise la fonction trouver destinations "
     horairemaxtrain = date_min
     
     "  Tableau qui contient les gares darrivée, leur ville l'heure de départ et l'heure d'arrivée"
     
     gares_tab = []
     
     while horairemaxtrain < date_max:
         request = trouver_destination_tgv(origine, horairemaxtrain)
         for i in request['departures'] :
             infos = request['departures'][i]['display_informations']['direction']
             gares_tab.append() """
####################################################"clea######### A FINIR >###############################################################""""""""            
             

url = requests.get('https://api.sncf.com/v1/coverage/sncf/stop_areas/{}/' \
                        'departures?from_datetime={}&forbidden_uris[]=physical_mode:RapidTransit'.format('stop_area:SNCF:87686006', convertir_en_chaine(now)) ,
                        auth=(token_auth, '')).json()

direction = url['departures'][0]['display_informations']['direction']
datdepart = url['departures'][0]['stop_date_time']['departure_date_time']
datearrival = url['departures'][0]['stop_date_time']['arrival_date_time']
tripname = url['departures'][0]['display_informations']['trip_short_name']

""" print(url['departures'][0]['display_informations']['direction'])
print(url['departures'][0]['stop_date_time']['departure_date_time'])
print(url['departures'][0]['stop_date_time']['arrival_date_time'])
print(url['departures'][0]['display_informations']['trip_short_name']) """

gares_tab = []
gares_tab.append({'direction':direction,'datdepart': datdepart, 'datearrival':datearrival, 'tripname':tripname})
print(gares_tab['direction'])