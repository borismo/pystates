from setuptools import setup

setup(
    name='pystates',
    version='0.1',
    py_modules=['pystates'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pystates=pystates:cli
    ''',
)
