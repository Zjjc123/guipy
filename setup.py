from setuptools import find_packages, setup

setup(
    name='guipy',
    packages=find_packages(),
    version='0.1.0',
    description=['guipy', 'guipy.components'],
    author='Casey Culbertson, Jason Zhang',
    license='MIT',
    install_requires=['pygame'],
)
