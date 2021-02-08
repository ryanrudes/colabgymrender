from pyvirtualdisplay import Display
from moviepy.editor import *
import time
import gym
import cv2
import os

class Recorder:
  def __init__(self, env, directory, fps=None):
    display = Display()
    display.start()
    if not os.path.exists(directory):
      os.mkdir(directory)
    self.env = env
    self.directory = directory
    self.env.reset()
    self.width, self.height, _ = self.env.render(mode = 'rgb_array').shape
    self.fps = fps if not fps is None else self.env.metadata['video.frames_per_second'] if hasattr(self.env.metadata, 'video.frames_per_second') else 30
    self.writer = None
    self.paused = False
    self.display = Display(size = (self.width, self.height))
    self.display.start()

  def pause(self):
    self.paused = True

  def resume(self):
    self.paused = False
    
  def __getattr__(self, name):
    if name in ['env', 'path', 'directory', 'play', 'width', 'height', 'fps', 'writer', 'reset', 'step']:
      return self.__getattr__(name)
    else:
      return self.env.__getattr__(name)

  def reset(self):
    observation = self.env.reset()
    now = time.time()
    self.path = f'{self.directory}/{now}.mp4'
    self.writer = cv2.VideoWriter(self.path, cv2.VideoWriter_fourcc(*'MP4V'), self.fps, (self.height, self.width))
    if not self.paused:
      self.writer.write(cv2.cvtColor(self.env.render(mode = 'rgb_array'), cv2.COLOR_RGB2BGR))
    return observation

  def step(self, action):
    observation, reward, terminal, info = self.env.step(action)
    if not self.paused:
      self.writer.write(cv2.cvtColor(self.env.render(mode = 'rgb_array'), cv2.COLOR_RGB2BGR))
    if terminal:
      self.writer.release()
    return observation, reward, terminal, info

  def play(self):
    if not self.display.is_alive():
      self.display.start()

    with VideoFileClip(self.path) as video:
      return video.ipython_display(width = self.width, height = self.height)