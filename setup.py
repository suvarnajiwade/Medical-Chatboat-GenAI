from setuptools import find_packages, setup

setup(
    name="Generative AI Project",
    version="0.1.0",  # It's recommended to use semantic versioning
    author="Suvarna Jiwade",
    author_email="suvarnabjiwade@gmail.com",
    packages=find_packages(),
    install_requires=[
        'Flask>=3.1.0',  # Add your dependencies here
        'Django>=5.1.3'
    ]
)
