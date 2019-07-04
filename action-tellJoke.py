#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lxml import etree

from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import random
import os


def subscribe_intent_callback(hermes, intent_message):
    conf = None
    action_wrapper(hermes, intent_message, conf)


def random_line(afile):
    """ See Waterman's Reservoir Algorithm """

    line = next(afile)
    for num, aline in enumerate(afile, 2):
        if (random.randrange(num) == 0):
            line = aline
    return line

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

    file = open(os.path.dirname(os.path.realpath(__file__)) + "/witze.txt")
    result_sentence = "Hallo, ich bin ein String und wurde hier her geschrieben."
    file.close()    
    
    root = etree.Element("root")
    doc = etree.SubElement(root, "doc")

    etree.SubElement(doc, "field1", name="blah").text = result_sentence
    etree.SubElement(doc, "field2", name="asdfasd").text = result_sentence

    tree = etree.ElementTree(root)
    tree.write("Testdaten.xml")
	
    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, result_sentence)
	

if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("DANBER:tellJoke", subscribe_intent_callback) \
            .start()
