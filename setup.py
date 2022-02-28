
  
import os

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='BLAST_REST',
    version='1.0.0',
    packages=['blast_rest'],
    include_package_data=True,
    license='MIT License',
    description='A simple Django restfull app to conduct web-based blast+ local alignment search.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/fbluewhale/blast_rest',
    author='fbluewhale',
    author_email='bluewhale.f@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django :: 4.0.1',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
)