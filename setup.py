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
        "python-decouple==3.4",
        "psycopg2-binary==2.8.6",
        "dj-database-url==0.5.0",
        "drf-yasg==1.20.0",
        "django-cors-middleware==1.5.0",
        "django-cors-headers==3.7.0",
        "whitenoise==5.2.0",
        "gunicorn==20.1.0",
        "pytest==6.2.4",
        "pytest-cov==2.11.1"
    ]
)
