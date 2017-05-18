# PentAI
CS 4701 Project, Spring 2017

# Dependencies
- Python 3.5+

# Getting Started
Clone the repository, and run ./main.py from the src/ directory.  To start a game with two human players, type `start`.  To start a game against an agent, type `start AGENTNAME`, where AGENTNAME is the name of the agent you wish to start.  There are two agents in this game: MinimaxAgent and LearningAgent.

# Teaching the LearningAgent
Included with the repository is a file called "heuristic.json" which is the result of training the learning agent.  If you wish to train the agent yourself, you can delete this file and run `start MinimaxAgent LearningAgent XX`, where XX is the number of games you wish to train it on.  Alternatively, you can also delete this file and simply play many games against the learning agent.

# Help
There are various commands available within the toplevel terminal.  To find out more information, type `help` in the terminal.
