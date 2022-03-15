from setuptools import setup

setup(
    name='geopandas_installer',
    version='0.0.1',
    packages=['geopandas_installer'],
    install_requires=["beautifulsoup4","requests"],
    entry_points={
        'console_scripts': [
            'check_system_parameters=geopandas_installer:check_system_parameters',
            'temp_dir=geopandas_installer:temp_dir',
            'download_geopandas_dependencies=geopandas_installer:download_geopandas_dependencies',
            'install_wheels=geopandas_installer:install_wheels',
            'install_geopandas=geopandas_installer:install_geopandas',
            'delete_temporary_directory=geopandas_installer:delete_temporary_directory',
        ]
    }
)
