from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_Requirements(file_path:str)->List[str]:
    """
    this function will return the list of requirements
    """
    requirements= []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace('\n', '') for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name='my_package',
    version='0.0.1',
    packages=find_packages(),
    author='Farhan',
    author_email='sheikhfarhan001.sf@gmail.com',
    install_requires=get_Requirements('requirements.txt'),
)