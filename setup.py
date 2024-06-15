from setuptools import setup, find_packages

setup(
    name='fixed_width_file',
    version='0.1',
    packages=find_packages(),
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'fixed_width_cli=cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
