#!/usr/bin/env python
import sys
import warnings

from .crew import FastapiCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run(site: str):
    """
    Run the crew.
    """
    inputs = {
        'topic': site
    }
    FastapiCrew().crew().kickoff(inputs=inputs)