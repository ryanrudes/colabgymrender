from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install
from subprocess import check_call

setup(
  name = 'colabgymrender',
  packages = ['colabgymrender'],
  version = '1.1.0',
  license='MIT',
  description = 'A wrapper for rendering OpenAI Gym environments in Google Colab',
  author = 'Ryan Rudes',
  author_email = 'ryanrudes@gmail.com',
  url = 'https://github.com/Ryan-Rudes/colabgymrender',
  download_url = 'https://github.com/Ryan-Rudes/colabgymrender/archive/v1.1.0.tar.gz',
  keywords = ['colab', 'gym', 'render', 'openai'],
  install_requires=['moviepy'],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)
