from setuptools import setup
from typing import List


# Declaring variables for setup fuctions 
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Kashif khan"
DESCRIPTION="This is first fsds machine learning project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"



def get_requirements_list() ->List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file

    return This function is going to return a list which contain name of
    libraries mentioned in requirements.txt file
    
    """
    with open(REQUIREMENT_FILE_NAME) as requirements_file:
        return requirements_file.readlines()


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()

)
