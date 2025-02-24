import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cabrillo",
    version="0.1.1",
    author="thxo",
    author_email="thx@uw.edu",
    description="A Python library to parse Cabrillo-format amateur radio "
                "contest logs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thxo/cabrillo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Communications :: Ham Radio"
    ],
)
