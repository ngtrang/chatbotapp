from rasa_core.channels import HttpInputChannel
from rasa_core.channels.facebook import FacebookInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
#from rasa_core.utils import EndpointConfig
from rasa_core.interpreter import RegexInterpreter

# load your trained agent
#nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/current')
#action_endpoint = EndpointConfig(url="https://8a5fd609.ngrok.io")
#agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)
interpreter = RasaNLUInterpreter("models/nlu/default/current")
agent = Agent.load("models\\dialogue", interpreter= interpreter) # RegexInterpreter())

input_channel = FacebookInput(
   fb_verify="FB_SECRET",
   fb_secret="VERIFY_TOKEN",
   fb_access_token="PAGE_ACCESS_TOKEN",
   )

# or `agent.handle_channel(...)` for synchronous handling
agent.handle_channel(HttpInputChannel(5004, "/app", input_channel))

#agent.handle_channel([input_channel])
