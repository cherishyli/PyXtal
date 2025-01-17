from distutils.core import setup
import setuptools  # noqa
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

exec(open('pyxtal/version.py').read())

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pyxtal",
    version=__version__,
    author="Scott Fredericks, Qiang Zhu",
    author_email="qiang.zhu@unlv.edu",
    description="Python code for generation of crystal structures based on symmetry constraints.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/qzhu2017/PyXtal",
    packages=['pyxtal', 
              'pyxtal.database', 
              'pyxtal.interface', 
              'pyxtal.optimize',
              'pyxtal.potentials',
              ],
    package_data={'pyxtal.database': ['*.csv', '*.json'],
                  'pyxtal.potentials': ['*'],
                 },

    scripts=['scripts/pyxtal', 'scripts/pyxtal_test'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'numpy>=1.13.3', 
        'scipy>=1.1.0', 
        'spglib>=1.10.4',
        'pymatgen<=2019.4.11'],
    python_requires='>=3.6.1',
    license='MIT',
)
