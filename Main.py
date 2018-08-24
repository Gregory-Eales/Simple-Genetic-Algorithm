import Agent
from matplotlib import pyplot as plt
word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
length = len(word)


Env1 = Agent.Environment(500, 180, length, word)
Env1.genetic_algorithm()

print(Env1.historical_fitness)
plt.plot(Env1.historical_fitness)
plt.show()


