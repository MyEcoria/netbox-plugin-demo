from setuptools import find_packages, setup

setup(
    name='counter-plugin',
    version='0.3',
    description='An example NetBox plugin',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)