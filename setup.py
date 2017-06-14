from setuptools import find_packages
from setuptools import setup


setup(
    name='pre_commit_pylint',
    description='Pylint wrapper hooks for pre-commit.',
    url='https://github.com/coldnight/pre-commit-pylint',
    version='0.0.1',

    author='Gray King',
    author_email='grayking.w@gmail.com',

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],

    packages=find_packages(exclude=('tests*', 'testing*')),
    install_requires=[
        'pylint',
    ],
    entry_points={
        'console_scripts': [
            'pylint-score-limit = pre_commit_pylint.pylint_wrapper:check_score',
            'pylint-py3k = pre_commit_pylint.pylint_wrapper:check_py3k',
        ],
    },
)
