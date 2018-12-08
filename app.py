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
   fb_verify="hello_bot",
   fb_secret="59dcc45952f56b363997cecc6333b28c",
   fb_access_token="EAAZAQIuo9HbIBALIt1fSHTKRTfA7ZCrMAMEY2AAVCGu7Y5kS4RICyffR9qU0IUuv1395p5zo0JYdwy3Ol1397ZBBqCrSZB4dZA9cvjo1Cs2sOd1TZAfru9s32MST89ZArJSLNlVQNST70US9gvRHSP3UFm8IE8IXJWAZAtyQfQPaZAgZDZD",
   )

# or `agent.handle_channel(...)` for synchronous handling
agent.handle_channel(HttpInputChannel(5004, "/app", input_channel))

#agent.handle_channel([input_channel])
