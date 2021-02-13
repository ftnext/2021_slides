from setuptools import find_packages, setup

setup(
    name="deployslide",
    version="0.2.0",
    packages=find_packages(exclude=["tests.*", "tests"]),
    entry_points={"console_scripts": ["deployslide = deployslide:main"]},
)
