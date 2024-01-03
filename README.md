# jira-data-miner

# Overview
This is a simple tool used to parse the copied information from Jira's Burndown chart report and create a list of dates and story point information that can be used to create a burndown chart in Excel or other tools that can be used to generate a chart.

# Getting started
You will firstly require Python3 to be installed on your machine. This can be downloaded from [Python downloads](https://www.python.org/downloads/). This solution was developed using Python3.

Next, run the following command from the terminal or command line window depending on whether you are in a Linux or Windows environment.

> pip install -r requirements.txt

Once the installation has been completed, you will need to run the following command to start the application:

> python3 main.py

# Unit Testing
This solution includes a number of unit tests which check that the solution works as expected. To run these tests from the command line, use the following commands:

> python3 -m unittest discover . "*_test.py"