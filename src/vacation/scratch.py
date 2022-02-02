import random 
import scipy.stats as stats

from basic_env import SeasonForecast
from agent import Agent
from utils import Actions, Seasons

basic_env = SeasonForecast(periods=12,n_steps=24,occlusion_pct=0.4)
basic_env.generate_weather(12)
basic_env.get_season()
print(len(basic_env.forecast))

agent_1 = Agent()
agent_2 = Agent()

agent_1.get_random_actions()

actions = {agent_1: agent_1.get_random_actions(),
               agent_2: agent_2.get_random_actions()}

agents = [agent_1, agent_2]   

season = basic_env.the_season
desc = Seasons[season]

actions[agents[0]]

current_season = Seasons[season]

rew = basic_env.get_agent_rew(actions[agents[0]])


if current_season == 'rainy':
    print('ok')


basic_env.generate_weather
print(basic_env.forecast)

season = stats.mode(basic_env.forecast)[0][0]

x = basic_env.forecast

no_of_occlusions = int(0.65*(len(x)))


occlusions = random.sample(range(0,len(basic_env.forecast)),no_of_occlusions)

for index in occlusions:
    x[index] = -1

print(x)


agent_1 = Agent()
agent_2 = Agent()
basic_env = SeasonForecast(periods=12,n_steps=24,occlusion_pct=0.4)
basic_env.generate_weather(periods=2)
actions = {
        agent_1: {
            agent_1.get_random_actions()
        },
        agent_2: {
            agent_2.get_random_actions()
        }
    }

print(actions)

print(type(actions))

act = basic_env.step(actions)

_, _, _ = basic_env.step()

basic_env.step()

basic_env.old_step()


print(type(basic_env))


x = random.uniform(10.5, 75.5)

def get_rand():

    return random.uniform(10.5, 75.5)

res = [random.uniform(10.5, 75.5) for i in range(7)]



    agent_1 = Agent()
    agent_2 = Agent()

    basic_env = SeasonForecast(periods=12,n_steps=24,occlusion_pct=0.4)

    basic_env.generate_weather()

    actions = {
        agent_1: {
            agent_1.get_random_actions()
        },
        agent_2: {
            agent_2.get_random_actions()
        }
    }

    print(actions)

    basic_env.step(actions)