from setuptools import setup

setup(
    name="ft_package",
    version="0.0.1",
    description="Count the occurrences of a value in a list.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="driss",
    author_email="drhaouha@student.42.fr",
    license="MIT",
    url="https://github.com/drisshaou/ft_package",
    py_modules=["ft_package"],
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)