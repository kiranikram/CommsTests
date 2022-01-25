import gym
from gym import spaces, logger
import numpy as np
import math
import torch
import torch.nn as nn
from torch.distributions.categorical import Categorical
from torch.optim import Adam

v_obs_space = spaces.Discrete(8)

v_act_space = spaces.Discrete(4)

obs_dim = v_obs_space.n
n_acts = v_act_space.n
hidden_sizes = [32]

def mlp(sizes, activation=nn.Tanh, output_activation=nn.Identity):
    # Build a feedforward neural network.
    layers = []
    for j in range(len(sizes)-1):
        act = activation if j < len(sizes)-2 else output_activation
        layers += [nn.Linear(sizes[j], sizes[j+1]), act()]
    return nn.Sequential(*layers)

# make core of policy network
logits_net = mlp(sizes=[obs_dim]+hidden_sizes+[n_acts])

y = [obs_dim]+hidden_sizes+[n_acts]

# make function to compute action distribution
def get_policy(obs):
    logits = logits_net(obs)
    return Categorical(logits=logits)

    # make action selection function (outputs int actions, sampled from policy)
def get_action(obs):
    return get_policy(obs).sample().item()

env = gym.make('CartPole-v0')

obs = env.reset()

test_obs = [1.0,2.0,1.0,2.0,1.0,1.0,1.0,1.0]
test_obs = np.array(test_obs)

x = get_action((torch.as_tensor(test_obs, dtype=torch.float32)))



############

env = gym.make('CartPole-v0')

obs = env.reset()

print(env.observation_space.shape[0])

def pi_net (obs_dim, hidden_size, act_dim):
    mlp = nn.Sequential(
              nn.Linear(obs_dim, 64),
              nn.Tanh(),
              nn.Linear(64, 64),
              nn.Tanh(),
              nn.Linear(64, act_dim)
            )

    return mlp 

def get_policy(obs):
    logits = logits_net(obs)
    return Categorical(logits = logits)

def get_action(obs):
    return get_policy(obs).sample().item()

test_obs = [1.0,2.0,1.0,2.0]
test_obs = np.array(test_obs)

print(type(obs))
print(type(test_obs))

obs_dim = obs.shape[0]

act_dim = 4
hidden_size = 32

logits_net = pi_net (obs_dim,hidden_size,act_dim)

act = get_action(obs)


#################

def mlp(sizes, activation=nn.Tanh, output_activation=nn.Identity):
    # Build a feedforward neural network.
    layers = []
    for j in range(len(sizes)-1):
        act = activation if j < len(sizes)-2 else output_activation
        layers += [nn.Linear(sizes[j], sizes[j+1]), act()]
    return nn.Sequential(*layers)


obs_dim = 1
hidden_sizes = [32]
n_acts = 4
logits_net = mlp(sizes=[obs_dim]+hidden_sizes+[n_acts])

def get_policy(obs):
    logits = logits_net(obs)
    return Categorical(logits=logits)

def get_action(obs):
    return get_policy(obs).sample().item()

obs = [1.0,2.0,1.0]
obs = np.array(obs)

obs_dim = obs.shape[0]

act_dim = 4

pi_net = nn.Sequential(
              nn.Linear(obs_dim, 64),
              nn.Tanh(),
              nn.Linear(64, 64),
              nn.Tanh(),
              nn.Linear(64, act_dim)
)

obs_tensor = torch.as_tensor(obs, dtype=torch.float32)

actions = pi_net(obs_tensor)

act = get_action(torch.as_tensor(obs, dtype=torch.float32))

#####

action_space = spaces.Discrete(2)
n_acts_c = action_space.n

theta_threshold_radians = 12 * 2 * math.pi / 360
x_threshold = 2.4

high = np.array(
            [
                x_threshold * 2,
                np.finfo(np.float32).max,
                theta_threshold_radians * 2,
                np.finfo(np.float32).max,
            ],
            dtype=np.float32,
        )

observation_space = spaces.Box(-high ,high, dtype=np.float32)

observation_space_c = spaces.Box(-high, high, dtype=np.float32)

obs_dim_c = observation_space.shape[0]

logits_net_c = mlp(sizes=[obs_dim_c]+hidden_sizes+[n_acts_c])

obs_c = np.random.uniform(low=-0.05, high=0.05, size=(4,))

print(type(obs_c))
print(type(obs))

act_c = get_action(torch.as_tensor(obs_c, dtype=torch.float32))



