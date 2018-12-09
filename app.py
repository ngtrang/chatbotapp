from rasa_core.channels import HttpInputChannel
from rasa_core.channels.facebook import FacebookInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
import os
#from rasa_core.utils import EndpointConfig
from rasa_core.interpreter import RegexInterpreter

if __name__ == '__main__':
   interpreter = RasaNLUInterpreter("models/nlu/default/current")
   agent = Agent.load("models\\dialogue", interpreter= interpreter) # RegexInterpreter())

   input_channel = FacebookInput(
      fb_verify= os.environ["VERIFY_TOKEN"],
      fb_secret=os.environ["FB_SECRET"],
      fb_access_token=os.environ["PAGE_ACCESS_TOKEN"],
      )

   # or `agent.handle_channel(...)` for synchronous handling
   agent.handle_channel(HttpInputChannel(5004, "/app", input_channel))

