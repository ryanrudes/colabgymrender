from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\\n" + fh.read()
    
setup(
  name = 'colabgymrender',
  packages = ['colabgymrender'],
  version = '{{VERSION_PLACEHOLDER}}',
  license = 'MIT',
  description = 'A wrapper for rendering OpenAI Gym environments in Google Colab',
  long_description_content_type = "text/markdown",
  long_description = long_description,
  author = 'Ryan Rudes',
  author_email = 'ryanrudes@gmail.com',
  url = 'https://github.com/ryanrudes/colabgymrender',
  keywords = ['colab', 'gym', 'render', 'openai'],
  packages = find_packages(),
  install_requires = ['moviepy', 'gym'],
  classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.9',
  ],
)
