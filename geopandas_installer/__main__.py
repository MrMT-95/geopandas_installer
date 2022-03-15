from . import *

if __name__ == "__main__":
    python_version, windows_bit_version = check_system_parameters()
    temp_dir = create_temp_folder()
    download_geopandas_dependencies(python_version, windows_bit_version, temp_dir)
    install_wheels(temp_dir)
    install_geopandas()
    delete_temporary_directory(temp_dir)