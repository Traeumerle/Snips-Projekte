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

    base_path = os.path.dirname(os.path.realpath(__file__))
	xml_file = os.path.join(base_path, "/testdaten.xml")
	
	tree = etree.parse("testdaten.xml")
	
	root = tree.getroot()


    result_sentence = (str(intent_message.slots.Stoff.first().value)+" bekommt den Wert "+str(intent_message.slots.Zahlen_mit_Komma.first().value))
    
    unternehmen = etree.Element("unternehmen")
    probe = etree.SubElement(unternehmen, "probe")

    etree.SubElement(probe, "parametereins").text = str(intent_message.slots.Stoff.first().value)
    etree.SubElement(probe, "parameterzwei").text = str(intent_message.slots.Zahlen_mit_Komma.first().value)
    etree.SubElement(probe, "parameterdrei").text = str(root)
	
    tree = etree.ElementTree(unternehmen)
    tree.write("testdaten.xml", encoding="UTF-8")
	
    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, result_sentence)
	

if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("ttr:Laborauftrag", action_wrapper) \
            .start()
