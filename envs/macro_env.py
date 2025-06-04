import gym
from gym import spaces
import numpy as np

from .shocks.demand import DemandShock
from .observation import build_observation
from .actions import decode_action
from .reward import compute_reward

class MacroEnv(gym.Env):
    metadata = {"render.modes": []}

    def __init__(self, config=None):
        super().__init__()
        self.action_space = spaces.Box(low=-1.0, high=1.0, shape=(5,), dtype=np.float32)
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(17,), dtype=np.float32)
        self.state = np.zeros(17, dtype=np.float32)
        self.shock = DemandShock(sigma=1.0)
        self.step_count = 0

    def step(self, action):
        policy = decode_action(action)
        shock = self.shock.sample()
        self.state += shock
        obs = build_observation(self.state)
        reward = compute_reward({'inflation': 2.0, 'output_gap': 0.0, 'FSI': 0.0, 'dr': 0.0}, 0.5, 0.3, 0.05)
        self.step_count += 1
        done = self.step_count >= 50
        return obs, reward, done, {}

    def reset(self):
        self.state = np.zeros(17, dtype=np.float32)
        self.step_count = 0
        return build_observation(self.state)

    def render(self, mode="human"):
        pass

    def close(self):
        pass
