from setuptools import setup,find_packages
from typing import List

HYPHEN_E_DOT = '-e .' # we need to remove this from requirements file in below function 

def get_requirements(file_path:str)->List[str]:
    '''this function returns list of requirements'''
    requirements = []
    with open(file_path) as file_obj: # opeining our file given as path
        requirements = file_obj.readlines() # it is reading \n as well
        requirements = [req.replace("\n",'') for req in requirements] # replacing with blank

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements



setup(
    name= 'mlproject',
    version='0.0.1',
    author="Abhishek",
    author_email="abhisheksapkota853@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt"),

)