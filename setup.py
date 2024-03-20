import setuptools

setuptools.setup(
    name='list-imports',
    version='2024.03.20',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
