#!/usr/bin/env python
import sys
import warnings

from .crew import FastapiCrew
from dotenv import load_dotenv

load_dotenv()

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run(site):
    """
    Run the crew.
    """
    inputs = {
        'site': site
    }
    FastapiCrew().crew().kickoff(inputs=inputs)