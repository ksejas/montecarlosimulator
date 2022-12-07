from setuptools import setup

setup(name='montecarlo',
      version='0.1',
      description='A package that lets you run Monte Carlo experiments. The user defines their "die", which can represent a variety of random variables, which the package utilizes for the random sampling to obtain statistics such as the the number of face counts per roll or the number of times a game results in all faces being identical or overall the number of times each unique combination of faces occurs in a given game (the size of the game is chosen by the user.).',
      url='https://github.com/ksejas/montecarlosimulator',
      author='Avid Gamer',
      author_email='gamer@example.com',
      license='MIT',
      packages=['montecarlo'])