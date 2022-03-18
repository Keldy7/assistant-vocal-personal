import speech_recognition as sr
#speech_recognition est une librairie qui comprend le langage humain et qui le convertir en texte

import pyttsx3
#pyttsx3 permet de lire du texte.Il est une librairie de conversion en Python

import wikipedia
#wikipedia permet d'extraire des informations depuis l'encyclopedie en ligne Wikipédia

import webbrowser
#wzbbroswer permet d'extraire des données depuis le web

import os
#os permet d'interagir avec le système d'exploitation de mon pc

import time
#time permet d'afficher l'heure

import keyboard
#permet de prendre le contrôle total de mon clavier

import ctypes
import winshell
import playsound
#playsound permet de jouer le son d'une vidéo

import subprocess
import pywhatkit
#permet d'envoyer un message/image à un groupe ou à un contact WhatsApp

import pyautogui
#permet de faire une capture d'ecran du pc
from ecapture import ecapture as ec
import wolframalpha
#une API 
import json
import datetime
import calendar
import requests
import random


global preoccupation

print('Chargement de ton assistant personnel Mado')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

#id est soit 0 pour une voix masculine soit 1 pour une voix feminine
engine.setProperty('voice','voices[1].id')


def parler(text):
    engine.say(text)
    engine.runAndWait()

def salutations():
    heure = datetime.datetime.now().hour
    if heure >= 6 and heure < 12:
        parler("Bonjour Aude")
        print("Bonjour Aude")
    elif heure >= 12 and heure < 18:
        parler("Bon après-midi Aude")
        print("Bon après-midi Aude")
    else:
        parler("Bonsoir Aude")
        print("Bonsoir Aude")


def ecouter():
    au_dio = sr.Recognizer()
    with sr.Microphone() as source:
        print("En écoute...")
        audio = au_dio.listen(source)

        try:
            preoccupation = au_dio.recognize_google(audio,language='fr')
            print(f"Mado a entendu :{preoccupation}\n")

        except Exception as e:
            parler("Excuse moi, peux-tu répéter ta préoccupation?")
            return "None"
        return preoccupation

parler("Je suis l'assistant personnel de Aude KOUASSY")
salutations()

#  
def analyser():
            
    thisdict = {
        "météo": meteo,
        "au revoir": bye,
        "wikipédia": go_wiki,
        "wiki": go_wiki,
        "à plus": bye,
        "ouvre youtube":open_youtube,
        "allons sur youtube":research_youtube,
        "ouvre google":open_google,
        "allons sur google":open_google,
        "ouvre gmail":open_gmail,
        "allons sur gmail":open_gmail,
        "heure": hour,
        "quelle heure est-il": hour,
        "qui es-tu": identity,
        "qu'est-ce que tu sais faire": identity,
        "comment vas-tu": health,
        "ta santé": health,
        "qui t'a créé": creator,
        "qui t'a fait": creator,
        "comment est-ce que Aude prévois de te rendre": future,
        "comment serais-tu bientôt": future,
        "vérrouillage de l'ordinateur": lock_pc,
        "vérrouille-toi": lock_pc,
        "éteins l'ordinateur":shutdown_pc,
        "éteins toi": shutdown_pc,
        "localise-moi une ville": localisation,
        "besoin de localiser une ville": localisation,
        "fais-moi une recherche sur Google Chrome": search,
        "aujourd'hui": today_date,
        "microsoft": open_microsoftoffice,
        "musique": play_music,
        "corbeille": empty_bin,
        "note": save_note,
        "ouvre mon editeur de code": open_vscode,
        "année": annee
        }
    
    try:
        
        if preoccupation in thisdict:
            thisdict[preoccupation]()

    except Exception as e:
        
        print("Erreur pas dans le dico")
        parler("Excuse moi,Aude. pouvez-vous répéter votre préoccupation?")
        return "None"
    
    return preoccupation
      
      
def bye():
    parler("Aurevoir Aude, je m'eteins")
    print('Aurevoir, je m\'eteins')
    exit()


#Ouvre Wikipédia / Open Wikipedia
def go_wiki():
    parler('Recherche sur Wikipédia...')
    preoccupation = preoccupation.replace("Wikipédia", "")
    resultats = wikipedia.summary(preoccupation, sentences=2)
    parler("Selon Wikipédia" + resultats)
    print(resultats)


#ouvre l'IDE Vs Code / open Visual Studio Code IDE
def open_vscode():
    parler("Ouverture de Visual Studio Code maintenant")
    os.startfile(r"C:\Users\Aude KOUASSY\AppData\Local\Programs\Microsoft VS Code\Code.exe")


#Ouvre Youtube / Open Youtube
def open_youtube():
    webbrowser.open_new_tab("https://www.youtube.com")
    parler("Ouverture de youtube maintenant")
    time.sleep(5)
 
 
#Ouvre Google / Open Google 
def open_google():
    webbrowser.open_new_tab("https://www.google.com")
    parler("Ouverture de Google Chrome maintenant")
    time.sleep(5)


#Ouvre Gmail / Open Gmail    
def open_gmail():
    webbrowser.open_new_tab("gmail.com")
    parler("Ouverture de Google Mail maintenant")
    time.sleep(5)
    
    
#Ouvre une application d'Office / Open a Office's app 
def open_microsoftoffice():
    parler("quelle application de microsoft office voudrais-tu que je lance?")
    preoccupation = ecouter()
    
    if "word" in preoccupation:
        parler("Ouverture de Microsft Word maintenant")
        os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
    
    elif "excel" in preoccupation:
        parler("Ouverture de Microsft Excel maintenant")
        os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")

    elif "powerpoint" in preoccupation:
        parler("Ouverture de Microsft PowerPoint maintenant")
        os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE")
        
    elif "project" in preoccupation:
        parler("Ouverture de Microsoft Project maintenant")
        os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINPROJ.EXE")
        
    elif "publisher" in preoccupation:
        parler("Ouverture de Microsoft Publisher maintenant")
        os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\MSPUB.EXE")
        
    elif "one note" in preoccupation:
        parler("Ouverture de Microsoft Onenote maintenant")
        os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\ONENOTE.EXE")
        
    elif "outlook" in preoccupation:
        parler("Ouverture de Microsoft Outlook maintenant")
        os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE")
       
    elif "visio" in preoccupation:
        parler("Ouverture de Microsoft Visio maintenant")
        os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\VISIO.EXE")
    
    else:
        print("Application non disponible dans Microsft Office")
        parler("Application non disponible dans Microsft Office")



#Prend une capture d'ecran / Take a screenshot
def screenshot():
    parler("quel nom veux-tu donner au fichier?")
    name_file = ecouter()
    complet_name = name_file + ".png"

    
    
#permet de vider la corbeille du pc / Empty recycle bin
def empty_bin():
    winshell.recycle_bin().empty(confirm = True, show_progress = False, sound = True)
    parler("Corbeille vidée")
    
    
#fais une recherche sur Youtube / Research on Yutube
def research_youtube():
    parler("qu'est-ce que tu veux rechercher sur Youtube?")
    preoccupation = ecouter()
    search = preoccupation
    print(f"Mado a entendu :{search}\n")
    parler(f"Ouverture de Youtube maintenant pour la recherche de {search}")
    webbrowser.open_new_tab("https://www.youtube.com/results?search_query=" + "+".join(search))
    #preoccupation = preoccupation.replace("search", "")
    time.sleep(5)


#permet d'enregistrer une note dans Notepad / Save a vocal message in text file
def save_note():
    parler("qu'est-ce que tu veux que je sauvegarde pour toi?")
    preoccupation = ecouter()
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(preoccupation)
    
    
#L'heure GMT de mon système
def hour():
    heure = datetime.datetime.now().strftime("%H:%M:%S")
    parler(f"Il est {heure}")

#Donne l'année en cours / Give the current year
def annee():
    the_year = datetime.datetime.now().year
    parler(f"Nous sommes en {the_year}")
    print(f"Nous sommes en {the_year}")


#L'heure GMT de mon système
def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day
    
    mois = ["Janvier", "Février",
            "Mars", "Avril", "Mai",
            "Juin", "Juillet", "Août", "Septembre",
            "Octobre", "Novembre", "Decembre"] 
    
    #days = list(range(1, 32))
    days = ["1", "2", "3", "4", "5", "6",
            "7", "8", "9", "10", "11", "12", "13",
            "14", "15", "16", "17", "18", "19",
            "20", "21", "22", "23", "24", "25",
            "26", "27", "28", "29", "30", "31"]
    
    parler(f"Aujourd'hui est le {week_now}, {days[day_now - 1]}, {mois[month_now - 1]}")
    print(f"Aujourd'hui est {week_now}, {days[day_now - 1]}, {mois[month_now - 1]}")


#L'identité de Mado
def identity():
    parler("Je suis Mado la version 1 avancé de l'assistant personnel de Aude. J'ai été programmé pour exécuter les petites tâches quotidiennes de Aude comme ouvrir youtube; google chrome; gmail; donner l'heure et la météo d'une ville donnée; prendre une photo; faire une recherche sur wikipedia")
    
    
#L'état de santé de Mado
def health():
    parler("Je vais bien. Je suis au top de ma forme même si je ne suis que virtuel c'est gentil que tu te préoccupe de moi et toi comment te portes-tu?")
    preoccupation = ecouter()
    list_sante = ["bien", "je me porte bien", "je vais bien merci", "je suis calé"]
    print(preoccupation)
    
    if preoccupation in list_sante:
        parler('cool. dieu merci')


#la créatrice de Mado / 
def creator():
    parler("J'ai été fais par Aude, c'est elle qui est à la base de ma création")
    print("J'ai été fais par Aude")
    
    
#Le futur de Mado / The become of my own personal assistant   
def future():
    parler("Aude est trop géniale, elle veut que je sois en mesure de pouvoir communiquer"
    "avec elle à distance; que je puisse exécuter des tâches sous ses ordres en son absence. Et le plus fabuleux dans tous ça; elle veut qu'on puisse communiquer en Ebrié; elle y travaille dessus en ce moment.")


#Verrouiller le pc / Lock the pc
def lock_pc():
    parler("Mode vérrouillage dans quelques instants")
    subprocess.call(["shutdown", "-l"])


#Eteindre le pc / Shutdown the pc
def shutdown_pc():
    parler("Ok ,l'ordinateur s'eteindra dans quelques secondes")
    os.system("shutdown /s /t 30")


#affiche la météo d'une ville donnée / Display the given city's weather 
def meteo():
    api_key = "8ef61edcf1c576d65d836254e11ea420"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    unit = "metric"  #metric = Celsius
    lang = "fr"
    parler("quelle est le nom de la ville?")
    city_name = ecouter()
    complete_url = base_url+"appid="+api_key+"&q="+city_name+"&units="+unit+"&lang="+lang
    reponse = requests.get(complete_url)
    x = reponse.json()
    
    if x["cod"] != "404":
        
        y = x["main"]
        temperature = y["temp"]
        humidite = y["humidity"]
        z = x["weather"]
        description_meteo = z[0]["description"]
        parler(" La temperature en unité est " +
              str(temperature) +
              "l'humidité en pourcentage est " +
              str(humidite) +
              "\n et la description est " +
              str(description_meteo))
        print(" La temperature en unité est " +
              str(temperature) +
              "\n humidité en pourcentage est " +
              str(humidite) +
              "\n description  " +
              str(description_meteo))
        
    else:
        
        parler("Désolé, ville non trouvée.")


#affiche la localisation d'une ville donnée / Display the given city's localisation 
def localisation():
    parler("quelle ville veux-tu localiser?")
    preoccupation = ecouter()
    url = 'https://google.com/maps/place/' + preoccupation + '/&amp;'
    parler(f"Ouverture de Google Maps pour la localisation de {preoccupation}")
    print(f"Nous effectuons une localisation de {preoccupation} sur Google Maps")
    webbrowser.get().open_new_tab(url)


#Joue une musique choisi aléatoirement du Pc / Play music on PC
def play_music():
    music_dir = r"C:\Users\Aude KOUASSY\Music"
    # or by a other method: music_dir = "C:\\Users\\Aude KOUASSY\\Music"
    sons = os.listdir(music_dir)
    print(sons) 
    tri = random.choice(sons)
    song_choosen = os.path.join(music_dir, tri)
    playsound.playsound(song_choosen)


#Recherche une information sur Google / Research a thing on Google
def search():
    parler("qu'est-ce que veux-tu rechercher?")
    preoccupation = ecouter()
    search = preoccupation
    print(f"Mado a entendu :{search}\n")
    url = 'https://google.com/search?q=' + search
    parler(f"Ouverture de Google Chrome maintenant pour la recherche de {search}")
    print(f"Nous effectuons une recherche de {search} sur Google Chrome")
    webbrowser.get().open_new_tab(url)
    time.sleep(5)


if __name__ == '__main__':

    while True:
        
        parler("Dis moi comment je peux t'aider?")
        preoccupation = ecouter().lower()
        preoccupation = str(preoccupation)
        analyser()
        
time.sleep(3)