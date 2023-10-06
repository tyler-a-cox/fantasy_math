from setuptools import setup, find_packages

# Package metadata
NAME = 'fantasy_math'
VERSION = '0.1.0'
DESCRIPTION = 'A Python package for fantasy football match-ups.'
AUTHOR = 'Your Name'
AUTHOR_EMAIL = 'your.email@example.com'
URL = 'https://github.com/tyleracox/fantasy_math'

# Package dependencies
INSTALL_REQUIRES = [
    'numpy',
    'asyncio',
    'aiohttp',
    'pandas',
    'pymc',
    'scipy'
]

# Package classifiers (https://pypi.org/classifiers/)
CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
]

# Package entry points
ENTRY_POINTS = {
    'console_scripts': [
        'fantasy_math = fantasy_math.cli:main',
    ],
}

# Read the long description from README.md
with open('README.md', 'r', encoding='utf-8') as readme_file:
    long_description = readme_file.read()

# Setup configuration
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    classifiers=CLASSIFIERS,
    entry_points=ENTRY_POINTS,
)