#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains the result sentences and intents for the German version
of the Say it again skill.
"""

# Result sentences
RESULT_SAY_SORRY = "Entschuldigung, ich weis nicht was ich gesagt habe. Ich muss wohl eingeschlafen sein"
RESULT_TEXT_SORRY = "Entschuldigung, ich habe vergessen was du gesagt hast."
RESULT_TEXT = "Ich habe mit einer Wahrscheinlichkeit von {1} gehört: \"{0}\""
RESULT_TEXT_NOTHING = "Entschuldigung, ich habe nichts gehört."
RESULT_INTENT_SORRY = "Entschuldigung, ich weiß nicht was ich wiederholen soll."

# Intents
INTENT_SAY_IT_AGAIN = "hermes/intent/Philipp:SayItAgain"
INTENT_WHAT_DID_I_SAY = "hermes/intent/Philipp:WhatDidISay"
INTENT_REPEAT_ACTION = "hermes/intent/Philipp:RepeatAction"
