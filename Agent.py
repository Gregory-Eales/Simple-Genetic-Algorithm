from fuzzywuzzy import fuzz
import string
import random


class Agent(object):

    def __init__(self, length):
        self.length = length
        self.string = self.init_string()
        self.fitness = -1

    def init_string(self):
        word = ""
        for i in range(self.length):
            word = word + random.choice(string.ascii_lowercase)
        return word

    def __str__(self):
        return "String: " + self.string + ", Fitness: " + str(self.fitness)


class Environment(object):

    def __init__(self, population, generations, length, input_string):
        self.population = population
        self.generations = generations
        self.length = length
        self.in_string = input_string
        self.in_string_length = length
        self.agents = self.initialize_agents()
        self.historical_fitness = []

    def genetic_algorithm(self):

        for generation in range(self.generations):
            #print("Generation: " + str(generation))
            if generation % 20 == 0:
                print(len(self.agents))
            self.fitness()

            self.selection()

            self.crossover()

            self.mutation()


            for agent in self.agents:
                if agent.fitness >= 99:
                    #print("Genetic Selection Complete")
                    #print(self.agents[0].string)
                    break

    def initialize_agents(self):
        agents = []
        for i in range(self.population):
            agents.append(Agent(self.length))
        return agents

    def fitness(self):
        for agent in self.agents:
            agent.fitness = fuzz.ratio(agent.string, self.in_string)

    def selection(self):
        self.agents = sorted(self.agents, key=lambda agent: agent.fitness, reverse=True)
        self.historical_fitness.append(self.agents[0].fitness)
        print(len(self.agents))
        self.agents = self.agents[0:int(len(self.agents)*0.3)]
        print(len(self.agents))

    def crossover(self):
        offspring = []
        for i in range(int((self.population - len(self.agents))/2)):
            parent1 = random.choice(self.agents)
            parent2 = random.choice(self.agents)
            child1 = Agent(self.in_string_length)
            child2 = Agent(self.in_string_length)
            split = random.randint(0, self.in_string_length)
            child1.string = parent1.string[0:split] + parent2.string[split:self.in_string_length]
            child2.string = parent2.string[0:split] + parent1.string[split:self.in_string_length]
            offspring.append(child1)
            offspring.append(child2)

        self.agents.extend(offspring)

    def mutation(self):
        for agent in self.agents:
            for index, parameter in enumerate(agent.string):
                if random.uniform(0.0, 1.0) <= 0.05:
                    agent.string = agent.string[0:index] + random.choice(string.ascii_lowercase) + agent.string[index+1:self.in_string_length]





