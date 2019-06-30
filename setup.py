from setuptools import setup

setup(
    name = 'echoer',
    version = '0.0.1',
    license = 'Creative Commons Attribution-Noncommercial-Share Alike license',
    install_requires = ['Flask', 'gunicorn'],
    extras_require={
        'dev': ['pytest', 'pip-tools']
    }
)
