import setuptools


NAME = 'readerpython'
VERSION = '0.0.1'
DESCRIPTION = 'For unloading online files into a docker volume'
AUTHOR = 'greyhypotheses'
URL = 'https://github.com/greyhypotheses/readerpython'
PYTHON_REQUIRES = '=3.7.10'

with open('README.md') as f:
    readme_text = f.read()

setuptools.setup()(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=readme_text,
    author=AUTHOR,
    url=URL,
    python_requires=PYTHON_REQUIRES,
    packages=setuptools.find_packages(exclude=['docs', 'tests'])
)
