# Gym Rendering for Colab

[![PyPI download month](https://img.shields.io/pypi/dm/colabgymrender.svg)](https://pypi.python.org/pypi/colabgymrender/)
![PyPI - Status](https://img.shields.io/pypi/status/colabgymrender)
![PyPI](https://img.shields.io/pypi/v/colabgymrender)
![GitHub](https://img.shields.io/github/license/Ryan-Rudes/colabgymrender)

## Installation
```bash
apt-get install -y xvfb python-opengl ffmpeg > /dev/null 2>&1
pip install -U colabgymrender
```

## Usage
```python
import gym
from colabgymrender.recorder import Recorder

env = gym.make("Breakout-v0")
directory = './video'
env = Recorder(env, directory)

observation = env.reset()
terminal = False
while not terminal:
  action = env.action_space.sample()
  observation, reward, terminal, info = env.step(action)

env.play()
```

## Demo
https://user-images.githubusercontent.com/18452581/116127430-d2afb300-a695-11eb-991a-99d13c015006.mp4

* [Watch it on YouTube](https://youtu.be/nv2dU_9oZJ0)
