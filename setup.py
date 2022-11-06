import setuptools
import os

readme = open(os.path.join(os.path.dirname(__file__), "README.md")).read()
with open(readme, encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="miskibin",
    version="1.0.6",
    author="Michał Skibiński",
    author_email="mskibinski109@gmail.com",
    description="My personal package for colored logs. Highly customizable.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/michalskibinski109/miskibin",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
