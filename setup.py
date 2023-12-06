from setuptools import setup, find_packages

setup(
    name='FileOrganizer',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        # List dependencies here
    ],
    entry_points={
        'console_scripts': [
            'file_organizer=FileOrganizer.organizer:organize_files',
        ],
    },
)
