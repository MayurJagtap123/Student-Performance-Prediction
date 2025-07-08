from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function return list of requirement
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='Student Performance Prediction',
    version='0.0.1',
    author="Mayur Jagtap",
    author_email='mayurjagtap648@gmail.com',
    packages=find_packages(),
    install_require=get_requirements('requirement.txt')
)