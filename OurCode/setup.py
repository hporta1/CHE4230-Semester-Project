from setuptools import setup, find_packages
with open("README.md", "r") as readme_file:

    readme = readme_file.read()

requirements = [
    "scikit-learn==1.0.2", 
    "scipy==1.8.0"
    "numpy==1.21.5"
]
setup(
    name="OurPackage",
    version="0.0.1",
    author="Luke Taylor",
    author_email="ltayl55@lsu.edu",
    descrpition="Supervised and Unsupervised learning code",
    long_description=readme, 
    long_description_content_type="text/markdown", 
    url="https://github.com/hporta1/CHE4230-Semester-Project.git",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
    "Programming Language :: Python :: 3.8",
    ],
)
