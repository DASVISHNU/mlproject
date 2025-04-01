from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of package requirements.
    """
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Remove newlines
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)  # Remove "-e ." if present
    
    return requirements  # Ensure function always returns a list

setup(
    name="mlproject",
    version="0.0.1",
    author="Vishnu",
    author_email="vishnudinesh128@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements1.txt")  # ✅ Updated filename
)
