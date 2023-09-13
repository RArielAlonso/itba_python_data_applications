from setuptools import setup

with open('requirements.txt') as f:
    install_requires=f.read().splitlines()

setup(
    name='pda',
    version='0.0.1',
    author='Ariel',
    install_requires=install_requires,
    packages=['pda']
)