# Gym Rendering for Colab

[![PyPI download month](https://img.shields.io/pypi/dm/colabgymrender.svg)](https://pypi.python.org/pypi/colabgymrender/)
[![PyPI - Status](https://img.shields.io/pypi/status/colabgymrender)](https://pypi.python.org/pypi/colabgymrender/)
[![PyPI](https://img.shields.io/pypi/v/colabgymrender)](https://pypi.python.org/pypi/colabgymrender/)
![GitHub](https://img.shields.io/github/license/Ryan-Rudes/colabgymrender)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ryan-Rudes/colabgymrender/blob/main/notebooks/demo.ipynb)

## Installation
```bash
apt-get install -y xvfb python-opengl ffmpeg > /dev/null 2>&1
pip install -U colabgymrender
pip install imageio==2.4.1
pip install --upgrade AutoROM
AutoROM --accept-license
pip install gym[atari,accept-rom-license]
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

[Watch it on YouTube](https://youtu.be/nv2dU_9oZJ0)

https://user-images.githubusercontent.com/18452581/116127430-d2afb300-a695-11eb-991a-99d13c015006.mp4

https://user-images.githubusercontent.com/18452581/116128757-48684e80-a697-11eb-9fbd-a716476b7c90.mp4

https://user-images.githubusercontent.com/18452581/116128782-4ef6c600-a697-11eb-80d2-fbf22ff7cf6f.mp4

https://user-images.githubusercontent.com/18452581/116128789-50c08980-a697-11eb-8ed3-6b4f645c3e1f.mp4
