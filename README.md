# Gym Rendering for Colab

[![PyPI download month](https://img.shields.io/pypi/dm/colabgymrender.svg)](https://pypi.python.org/pypi/colabgymrender/)
![PyPI - Status](https://img.shields.io/pypi/status/colabgymrender)
![PyPI](https://img.shields.io/pypi/v/colabgymrender)
![GitHub](https://img.shields.io/github/license/Ryan-Rudes/colabgymrender)

* [YouTube Demo](https://youtu.be/nv2dU_9oZJ0)

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

> <a href="https://youtu.be/ma4Oj775jo0"><img src="https://i.ibb.co/zJtGzZY/ezgif-frame-098.jpg" border="0"></img></a>
