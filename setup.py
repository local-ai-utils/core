from setuptools import setup, find_packages

setup(
    name="local-ai-utils-core",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'pyyaml',
        'pytest'
    ],
)