from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

import os
import gym
import cv2
import time
from moviepy.editor import *
from pyvirtualdisplay import Display

display = Display(visible = 0, size = (800, 600))
display.start()

class Recorder(gym.Wrapper):
  def __init__(self, env, directory, auto_release=True, size=None, fps=None):
    super(Recorder, self).__init__(env)
    self.directory = directory
    self.auto_release = auto_release
    self.active = True

    if not os.path.exists(self.directory):
      os.mkdir(self.directory)

    if size is None:
      self.env.reset()
      self.size = self.env.render(mode = 'rgb_array').shape[:2][::-1]
    else:
      self.size = size

    if fps is None:
      if 'video.frames_per_second' in self.env.metadata:
        self.fps = self.env.metadata['video.frames_per_second']
      else:
        self.fps = 30
    else:
      self.fps = fps

  def pause(self):
    self.active = False

  def resume(self):
    self.active = True

  def _start(self):
    self.cliptime = time.time()
    self.path = f'{self.directory}/{self.cliptime}.mp4'
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    self._writer = cv2.VideoWriter(self.path, fourcc, self.fps, self.size)

  def _write(self):
    if self.active:
      frame = self.env.render(mode = 'rgb_array')
      frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
      self._writer.write(frame)

  def release(self):
    self._writer.release()

  def reset(self):
    observation = self.env.reset()
    self._start()
    self._write()
    return observation

  def step(self, action):
    data = self.env.step(action)
    self._write()

    if self.auto_release and data[2]:
      self.release()

    return data

  def play(self, **kwargs):
    kwargs.setdefault('autoplay', True)
    kwargs.setdefault('center', False)
    return VideoFileClip(self.path).ipython_display(**kwargs)
