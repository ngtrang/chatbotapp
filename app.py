from flask import Flask
from model_manager import ModelManager
from rasa_core.channels import HttpInputChannel
from rasa_core.channels.facebook import FacebookInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
import os
#from rasa_core.utils import EndpointConfig
from rasa_core.interpreter import RegexInterpreter


interpreter = RasaNLUInterpreter("models/nlu/default/current")
agent = Agent.load("models\\dialogue", interpreter= interpreter) # RegexInterpreter())

input_channel = FacebookInput(
        fb_verify= os.eviron["VERIFY_TOKEN"],
        fb_secret = os.eviron["FB_SECRET"],
        fb_access_token = os.eviron["PAGE_ACCESS_TOKEN"])
agent.handle_channel(HttpInputChannel(5004, "/app", input_channel))


