#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lxml import etree

from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import os

def action_wrapper(hermes, intent_message, conf):
    """ Write the body of the function that will be executed once the intent is recognized. 
    In your scope, you have the following objects : 
    - intent_message : an object that represents the recognized intent
    - hermes : an object with methods to communicate with the MQTT bus following the hermes protocol. 
    - conf : a dictionary that holds the skills parameters you defined. 
      To access global parameters use conf['global']['parameterName']. 
      For end-user parameters use conf['secret']['parameterName'] 
    Refer to the documentation for further details. 
    """

    result_sentence = "Hallo"
    
    unternehmen = etree.Element("unternehmen")
    probe = etree.SubElement(unternehmen, "probe")

    etree.SubElement(probe, "parametereins").text = result_sentence
    etree.SubElement(probe, "parameterzwei").text = str(intent_message)
    etree.SubElement(probe, "parameterdrei").text = str(intent_message.session_id)
	
    tree = etree.ElementTree(unternehmen)
    tree.write("testdaten.xml", encoding="UTF-8")
	
    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, result_sentence)
	

if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("ttr:giveMaterial", action_wrapper) \
            .start()