from setuptools import setup, find_packages

setup(
    name="local_ai_utils_core",
    version="0.2.0",
    packages=['local_ai_utils_core'],
    package_dir={"local_ai_utils_core": "core"},
    install_requires=[
        'openai',
        'pyyaml',
        'pytest',
        'desktop-notifier'
    ],
)