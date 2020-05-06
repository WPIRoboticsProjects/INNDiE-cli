from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name="inndie",
    version="0.1.18",
    description="The INNDiE CLI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wpilibsuite/INNDiE-cli",
    packages=["inndie"],
    python_requires=">=3.6",
    install_requires=["click==7.0.0", "boto3==1.9.248"],
    entry_points={
        "console_scripts": ["inndie=inndie.client:cli"]
    },
    project_urls={
        "Bug Reports": "https://github.com/wpilibsuite/INNDiE-cli/issues",
        "Source": "https://github.com/wpilibsuite/INNDiE-cli"
    }
)
