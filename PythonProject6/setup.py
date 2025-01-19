from setuptools import setup, find_packages

setup(
    name='Topsis-Ojasvi-102203960',
    version='0.1',
    author='Ojasvi',
    author_email='ojasvipathania23@gmail.com',
    description='A Python package implementing the TOPSIS method for multi-criteria decision making.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ojasvi-23/Topsis-Ojasvi-102203960',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy',
        # Add any other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'topsis = topsis.cli:main',  # Assuming you have a cli.py file with a main function
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
