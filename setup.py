"""
Install project requirements.
"""

from setuptools import setup, find_packages

setup(
    name="drinksapi",
    version="1.0.0",
    description='Drinks/Cocktails API',
    packages=find_packages(),  
    include_package_data=True,
    scripts=["manage.py"],
    install_requires=[
        "Django==3.2.2",
        "djangorestframework==3.12.4",
    ]
)