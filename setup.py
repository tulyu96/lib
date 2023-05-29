from setuptools import find_packages, setup

setup(
    name="qrlib",
    packages=find_packages(
        include=["qrlib"],
    ),
    version="0.1.0",
    description="Python Library for Quantitative Trading & Investment Research",
    author="Tu",
    license="MIT",
    install_requires=[],  # limited to the package must need
    setup_requires=[],
    test_require=[],
    test_suite="tests",  # the directory name where all the tests are stored
)
