from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup (
    name='tusic',
    version='1.0',
    packages=[''],
    scripts=["tusic.py"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bistcuite/tusic",
    install_requires=[
        'pygame'
    ],
    entry_points = {
        'console_scripts': ['tusic=tusic:main'],
    }
 )