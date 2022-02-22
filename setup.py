from setuptools import setup

setup(
    name='flask-tutorial',
    version='0.0.1',
    install_requires=[
        'Flask',
        'rq',
        'flask-expects-json',
        'jsonschema',
        'redis',
        'Werkzeug',
        'pytest',
        'requests',
        'importlib; python_version == "3.7"',
    ],
)