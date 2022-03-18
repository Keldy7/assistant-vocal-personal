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

import pyjokes
#pyjokes permet de faire des blagues pour les programmeurs 
import subprocess
from ecapture import ecapture as ec
import wolframalpha
#une API 
import json
import datetime
import requests


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
    if heure >= 0 and heure < 12:
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

if __name__ == '__main__':



    while True:
        parler("Dis moi comment je peux t'aider?")
        preoccupation = ecouter().lower()
        if preoccupation == 0:
            continue
        
        #pour arreter le programme
        if "au revoir" in preoccupation or "ok bye" in preoccupation or "à plus" in preoccupation:
            parler('Aurevoir Aude, je m\'eteins')
            print('Aurevoir, je m\'eteins')
            break
        
        if 'wikipédia' in preoccupation or "wiki" in preoccupation:
            parler('Recherche sur Wikipédia...')
            preoccupation = preoccupation.replace("wikipédia", "")
            resultats = wikipedia.summary(preoccupation, sentences=3)
            parler("Selon Wikipédia")
            print(resultats)
            parler(resultats)

        #Pour ouvrir Youtube
        elif 'ouvre youtube' in preoccupation or 'allons sur youtube' in preoccupation:
            webbrowser.open_new_tab("https://www.youtube.com")
            parler("Ouverture de youtube maintenant")
            time.sleep(5)
        
        #Pour ouvrir Google
        elif 'ouvre google' in preoccupation or 'allons sur google' in preoccupation:
            webbrowser.open_new_tab("https://www.google.com")
            parler("Ouverture de Google Chrome maintenant")
            time.sleep(5)
        
        #Pour ouvrir Gmail sur Google Chrome
        elif 'ouvre gmail' in preoccupation or 'allons sur gmail' in preoccupation:
            webbrowser.open_new_tab("gmail.com")
            parler("Ouverture de Google Mail maintenant")
            time.sleep(5)
            
        #elif "musique" in preoccupation:
            #webbrowser.open('C:\Users\Aude KOUASSY\Music')
            #projectpath =
            
        #Pour donner la météo d'une ville donnée
        elif "météo" in preoccupation or 'donne moi la météo d\'aujourd\'hui' in preoccupation:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            parler("quelle est le nom de la ville")
            city_name = ecouter()
            complete_url = base_url+"appid="+api_key+"&q="+city_name
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
                      "\n humidité en pourcentage est " +
                      str(humidite) +
                      "\n description  " +
                      str(description_meteo))
                print(" La temperature en unité est " +
                      str(temperature) +
                      "\n humidité en pourcentage est " +
                      str(humidite) +
                      "\n description  " +
                      str(description_meteo))
                
            else:
                parler("Désolé, ville non trouvée")
        
        #L'heure GMT de mon système
        elif 'heure' in preoccupation or 'quelle heure est-il' in preoccupation:
            heure = datetime.datetime.now().strftime("%H:%M:%S")
            parler(f"Il est {heure}")
        
        #L'identité de Mado
        elif 'qui es-tu' in preoccupation or "qu'est-ce que tu sais faire" in preoccupation:
            parler('Je suis Mado la version 1 de l\'assistant personnel de Aude. J\'ai été programmé pour exécuter les petites taches quotidiennes de Aude comme'
                  'ouvrir youtube; google chrome; gmail; donner l\'heure et la météo d\'une ville donnée; prendre une photo; faire une recherche sur wikipedia')
            parler(pyjokes.get_joke()) #par défaut la langue est fr
        
        #L'état de santé de Mado
        elif "comment vas-tu" in preoccupation or "ordinateur" in preoccupation:
            parler("Baaahh. Je vais bien. Je suis au top de ma forme même si je ne suis que virtuel c'est gentil que tu te préoccupe de moi et toi comment te portes-tu?")
            preoccupation = ecouter()
            list_sante = ["bien", "je me porte bien", "je vais bien merci", "je suis calé"]
            print(preoccupation)
            if preoccupation in list_sante:
                parler('ah cool. dieu merci')
            #for index_rep in range (0, len(list_sante)):
                #if preoccupation == list_sante[index_rep]:
                    #parler('ah cool. dieu merci')
                
        #la créatrice de Mado
        elif "qui t'a créé" in preoccupation or "qui t'a fait" in preoccupation:
            parler("J'ai été fais par Aude, c'est elle qui est à la base de ma création")
            print("J'ai été fais par Aude")
        
        #Le futur de Mado
        elif "comment est-ce que Aude prévois de te rendre" in preoccupation or "comment serais-tu bientôt" in preoccupation:
            parler("Aude est trop géniale, elle veut que je sois en mesure de pouvoir communiquer"
                  "avec elle à distance; que je puisse exécuter des tâches sous ses ordres en son absence. Et le plus fabuleux dans tous ça; elle veut qu'on puisse communiquer en Ebrié; elle y travaille dessus en ce moment.")

        #elif "caméra" in preoccupation or "prends une photo" in preoccupation or "appareil photo" in preoccupation:
            #ec.capture(0,"robo camera","img.jpg")

        elif 'rechercher'  in preoccupation:
            parler("qu'est-ce que tu veux rechercher?")
            preoccupation = ecouter()
            search = preoccupation
            print(f"Mado a entendu :{search}\n")
            url = 'https://google.com/search?q=' + search
            #preoccupation = preoccupation.replace("search", "")
            parler(f"Ouverture de Google Chrome maintenant pour la recherche de {search}")
            print(f"Nous effectuons une recherche de {search} sur Google Chrome")
            webbrowser.get().open_new_tab(url)
            time.sleep(5)
        
        #Trouver une localisation actuelle
        elif "localisation" in preoccupation:
            parler("localisons quelle ville")
            preoccupation = ecouter()
            url = 'https://google.com/maps/place/' + preoccupation + '/&amp;'
            parler(f"Ouverture de Google Mapspour la localisation de {preoccupation}")
            print(f"Nous effectuons une localisation de {preoccupation} sur Google Maps")
            webbrowser.get().open_new_tab(url)

              
         #Vérrouiller le pc  
        elif "vérrouillage de l'ordinateur" in preoccupation or "vérrouille-toi" in preoccupation:
            parler("Mode vérrouillage dans quelques instants")
            subprocess.call(["shutdown", "-l"])
     
        #Eteindre le pc
        elif "éteins l'ordinateur" in preoccupation or 'éteins toi' in preoccupation:
            parler("Ok ,l'ordinateur s'eteindra dans quelques secondes ")
            os.system("shutdown /s /t 30")
            #subprocess.call(["turn off", "-l"]) ne passe pas

time.sleep(3)




#pour eviter de'avoir assez de if et elif dans le code il y a possilibilité
#de créer un dico et dajouter des fonctions comme valeurs et de pouvoir avoir des
#clés qui seront les préoccupations dits dans le microphones de mon téléphone

