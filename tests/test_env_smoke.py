import pytest
from envs.macro_env import MacroEnv


def test_smoke_rollout():
    env = MacroEnv(config="configs/kazakh.yml")
    obs = env.reset()
    assert env.observation_space.contains(obs)
    for _ in range(10):
        a = env.action_space.sample()
        obs, r, done, _ = env.step(a)
        assert env.observation_space.contains(obs)
        assert isinstance(r, float)
    env.close()
