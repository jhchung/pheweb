
# run this with `python2 setup.py install` (in a virtualenv, probably)
# while developing, use `python2 setup.py develop` to just make a symlink from `sites-packages` to this folder.
# to upload to pypi, `python2 setup.py sdist bdist_wheel; twine upload dist/*`

from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='PheWeb',
    version='0.9',
    description="A tool for building PheWAS websites from association files",
    long_description=readme(),
    author="Peter VandeHaar",
    author_email="pjvh@umich.edu",
    url="https://github.com/statgen/pheweb",
    packages=['pheweb'],
    scripts=['bin/pheweb'],
    # TODO: use: entry_points={'console_scripts': ['pheweb=pheweb.command_line:main']},
    #       see <https://python-packaging.readthedocs.io/en/latest/everything.html>
    # TODO: add test_suite (ie, make a single file that runs tests, figure out how to access input_data, make a data_dir in /tmp)
    license="MIT",
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask>=0.11',
        'pysam~=0.9.0',
        'marisa-trie~=0.7',
        'flask-compress~=1.3',
        'contextlib2~=0.5',
        'intervaltree~=2.1',
        'more_itertools~=2.4',
        'tqdm~=4.10',
        'openpyxl~=2.4',
        'scipy~=0.17',
     ]
)
