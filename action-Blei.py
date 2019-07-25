#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lxml import etree

from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import os
import requests
from io import StringIO, BytesIO

def action_wrapper(hermes, intent_message):
    """ Write the body of the function that will be executed once the intent is recognized. 
    In your scope, you have the following objects : 
    - intent_message : an object that represents the recognized intent
    - hermes : an object with methods to communicate with the MQTT bus following the hermes protocol. 
    - conf : a dictionary that holds the skills parameters you defined. 
      To access global parameters use conf['global']['parameterName']. 
      For end-user parameters use conf['secret']['parameterName'] 
    Refer to the documentation for further details. 
    """
    ###-----------------Get Request an den Server senden und response in variable abspeichern-----------------###
    
    #Antwortsatz und Sprachrückgabe wird erstellt
    result_sentence = (str(intent_message.slots.Stoff.first().value)+" bekommt den Wert "+str(intent_message.slots.Zahlen_mit_Komma.first().value))
 
    #URL für GET Request festlegen
    url = 'http://192.168.200.67:8080/WebAppTest/Basic'
    
    #per GET bekommene XML Datei in var speichern
    ##response = requests.get(url)
    
    #Datei wird ge'parse'd und in var gespeichert
    ##tree = etree.parse(StringIO(response.text))
    
    #Hauptcontainer der Datei wird in var gespeichert 
    ##root = tree.getroot()
    
    #variablen mit den entsprechenden Values werden erstellt
    #labid = "eins zwei drei vier fünf sechs sieben acht neun"##root.get("Name")	
    #probName=str(intent_message.slots.Stoff.first().value)
    #probWert=str(intent_message.slots.Zahlen_mit_Komma.first().value)

    #Dict mit den entsprechenden Übergabewerten wird erstellt
    xmlData = {'laborauftragsId': 'eins zwei drei vier fünf sechs sieben acht neun', 'probenName': 'Blei', 'probenWert':'NA', 'probenId':'Eins Eins'}
    
    #Post Request wird an bestimmte URL mit den entsprechenden Werten gesendet
    postRequestResponse = requests.post(url, data=xmlData)

    #ID der Interaktion wird in var gespeichert
    current_session_id = intent_message.session_id

    #Interaktion wird beendet und der Antwortsatz wird sprachlich Ausgegeben
    hermes.publish_end_session(current_session_id, result_sentence)
	

if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("ttr:Blei", action_wrapper) \
            .start()
