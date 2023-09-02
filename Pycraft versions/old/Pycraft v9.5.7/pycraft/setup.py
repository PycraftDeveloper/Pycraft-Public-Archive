import os
import setuptools

base = os.path.dirname(__file__)

with open(os.path.join(base, "README.md"), "r") as file:
    long_description = file.read()
    
with open("requirements.txt", "r") as file:
    requirements = [line.strip() for line in file]

setuptools.setup(
    name="python-pycraft",
    version="0.9.5-1",
    author="PycraftDev",
    author_email="thomasjebbo@gmail.com",
    description="The open-world, OpenGL video game made in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url="https://github.com/PycraftDeveloper/Pycraft",
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent"],
    python_requires=">=3.7",
    install_requires=requirements)
