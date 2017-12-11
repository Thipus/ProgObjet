class Agent:
	
	def say_hello(self, first_name):
		return "Bien le bonjour " + first_name + " !"

	def __init__(self, agreaableness):
		self.agreaableness = agreaableness

first_agent = Agent(50)
print(first_agent.agreaableness)