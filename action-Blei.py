#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lxml import etree

from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import os

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
    #Pfad der Datei wird in variable gespeichert
    base_path = os.path.dirname(os.path.realpath(__file__))
    
    #Datei wird dem Pfad hinzugefügt und in var gespeiechert
    xml_file = os.path.join(base_path, "/testdaten.xml")
    
    #Datei wird ge'parse'd und in var gespeichert
    tree = etree.parse("testdaten.xml")	
    
    #Hauptcontainer der Datei wird in var gespeichert 
    root = tree.getroot()

    Kommazahlen = float(intent_message.slots.Zahlen_mit_Komma.first().value)
    
    #Antwortsatz und Sprachrückgabe wird erstellt
    result_sentence = (str(intent_message.slots.Stoff.first().value)+" bekommt den Wert "+str(intent_message.slots.Zahlen_mit_Komma.first().value))
    
    #Parameter werden dem Hauptcontainer hinzugefügt und mit einem Wert versehen
    etree.SubElement(root, "parametereins").text = str(intent_message.slots.Stoff.first().value)
    etree.SubElement(root, "parameterzwei").text = "{}".format(Kommazahlen)
    etree.SubElement(root, "parameterdrei").text = str(result_sentence)
    
    #Hauptcontainer mit neuem Inhalt wird in Dateiformat geschrieben	
    tree = etree.ElementTree(root)
    
    #Datei wird gespeichert und codiert
    tree.write("testdaten.xml", encoding="UTF-8")

    #ID der Interaktion wird in var gespeichert
    current_session_id = intent_message.session_id

    #Interaktion wird beendet und der Antwortsatz wird sprachlich Ausgegeben
    hermes.publish_end_session(current_session_id, result_sentence)
	

if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("ttr:Blei", action_wrapper) \
            .start()
