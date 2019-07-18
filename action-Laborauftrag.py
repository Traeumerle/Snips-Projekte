#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lxml import etree

from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import os
import requests

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

    #Antwortsatz für Sprachrückgabe wird erstellt	
    result_sentence = ("Der "+str(intent_message.slots.Dokument.first().value)+" bekommt die Kennzeichnung "+str(intent_message.slots.Zahlenfolgen.first().value))
    
    #neuer Container wird erstellt und mit einem Wert versehen
    #Laborauftrag = etree.Element(str(intent_message.slots.Dokument.first().value), name = str(intent_message.slots.Zahlenfolgen.first().value))
    
    #Hauptcontainer mit neuem Inhalt wird in Dateiformat der XML geschrieben
    #tree = etree.ElementTree(Laborauftrag)

    #Datei wird gespeichert und codiert
    #tree.write("testdaten.xml", encoding="UTF-8")

    url = 'http://192.168.200.71:8080/WebAppTest/Basic'
    
    xmlData = {'laborauftragsId': str(intent_message.slots.Zahlenfolgen.first().value), 'probenName': 'NA', 'probenWert':'NA', 'probenId':'187'}
    
    r = requests.post(url, data=xmlData)
	
    #ID der Interaktion wird in var gespeichert
    current_session_id = intent_message.session_id
	
    #Interaktion wird beendet und der Antwortsatz wird sprachlich Ausgegeben
    hermes.publish_end_session(current_session_id, result_sentence)
	

if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("ttr:Laborauftrag", action_wrapper) \
            .start()
