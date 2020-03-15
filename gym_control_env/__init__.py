"""gym-control-env - Extension for OpenAI Gym environments and benchmarks"""

__version__ = '0.1.0'
__author__ = 'Or Dicker <or.dicker@gmail.com>'
__all__ = []

from gym.envs.registration import register

register(
    id='foo-v0',
    entry_point='gym_control_env.envs:MyPendulumEnv',
)
