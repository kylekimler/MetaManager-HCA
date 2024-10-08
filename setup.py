from setuptools import setup, find_packages

setup(
    name='hca_metadata_manager',
    version='0.1',
    packages=find_packages(),
    package_data={
        'hca_metadata_manager': ['data/*.csv'],
        '': ['data/*.csv'],
    },
    include_package_data=True,
    install_requires=[
        'gspread',
        'oauth2client',
        'google-auth',
        'google-auth-oauthlib',
        'google-auth-httplib2',
        'google-api-python-client',
        'pandas',
        'numpy',
        'scanpy'
    ],
    entry_points={
        'console_scripts': [
            # Add any console scripts if necessary
        ],
    },
)