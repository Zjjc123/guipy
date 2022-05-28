from setuptools import find_packages, setup

# python setup.py bdist_wheel

setup(
    name='guipylib',
    packages=find_packages(),
    version='0.1.0',
    description='User Interface Library for pygame',
    author='Casey Culbertson, Jason Zhang',
    license='MIT',
    install_requires=['pygame'],
)
