# Gym Rendering for Colab

> [PyPi](https://pypi.org/project/colabgymrender/)

## Installation
```bash
pip install gym pyvirtualdisplay > /dev/null 2>&1
apt-get install -y xvfb python-opengl ffmpeg > /dev/null 2>&1
pip install colabgymrender==1.0.2
```

## Usage
```python
import gym
from colabgymrender.recorder import Recorder

env = gym.make("Qbert-v0")
directory = './video'
env = Recorder(env, directory)

observation = env.reset()
terminal = False
while not terminal:
  action = env.action_space.sample()
  observation, reward, terminal, info = env.step(action)

env.play()
```

> <a href="https://youtu.be/R1uWOSvglAo"><img src="https://i.ibb.co/K55YtmM/ezgif-frame-001.jpg" border="0"></img></a>
