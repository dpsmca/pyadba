"""Package configuration."""
from setuptools import find_packages, setup

VERSION = "0.1.0"

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='pyadba',
    version=VERSION,
    author='David S',
    author_email='DLRSTADBAGBS@mayo.edu',
    description='This python module allows to connect to and query a SQL Server database',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://mclm@dev.azure.com/mclm/GBS%20CAD/_git/NGS_ADBA',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        'wheel',
        'JayDeBeApi',
        'termcolor',
        'pytz',
        'pymssql',
        'pymssql-plus',
        'pymssql-utils',
        'pyodbc',
        'pyodbc-database-tools',
        'pyodbc-helpers',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Topic :: Database :: Database Engines/Servers',
        'Programming Language :: Python :: 3',
        'Programming Language :: SQL',
    ],
)
