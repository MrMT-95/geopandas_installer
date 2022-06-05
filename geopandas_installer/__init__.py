import os
import platform
import re
import sys
import tempfile
import shutil
from bs4 import BeautifulSoup
import requests


def check_system_parameters():
    python_version = sys.version.split(" ")[0].replace(".", "")[0:2]
    windows_bit_version = platform.architecture()[0].replace("bit", "")

    return python_version, windows_bit_version


def create_temp_folder():
    return tempfile.mkdtemp(dir=os.path.dirname(os.path.abspath(__file__)))


def delete_temporary_directory(temp_dir):
    shutil.rmtree(temp_dir)


def get_dependencies_links():
    url = 'https://www.lfd.uci.edu/~gohlke/pythonlibs/'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'}
    reqs = requests.get(url, headers=headers)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    whl_names = []
    for link in soup.findAll('a'):
        text = link.text
        if text != "" and ".whl" in text:
            whl_names.append(link.text)

    return whl_names


def download_geopandas_dependencies(python_version, windows_bit_version, temp_dir):
    website_url = 'https://download.lfd.uci.edu/pythonlibs/x6hvwk7i/'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'}

    whl_names = get_dependencies_links()
    dependencies_names = ["GDAL", "Fiona", "rasterio"]
    dependencies = []
    for dep_name in dependencies_names:
        for name in whl_names:
            regex = f"{dep_name}.*cp{python_version}.*{windows_bit_version}\\.whl"
            if re.search(regex, name):
                dependencies.append(name.replace("‑", "-"))
                break

    for file_name in dependencies:
        download_path = os.path.join(temp_dir, file_name)
        print("Downloading: " + file_name)
        file_url = website_url + file_name

        r = requests.get(file_url, headers=headers)
        open(download_path, 'wb').write(r.content)


def install_geopandas():
    os.system("python -m pip install geopandas")


def install_wheels(temp_dir):
    pip_install_table = []
    for file in os.listdir(temp_dir):
        pip_install_table.append("python -m pip install " + os.path.join(temp_dir, file))

    dependencies_names = ["GDAL", "pyproj", "Fiona", "Shapely"]
    for dependency in dependencies_names:
        for item in pip_install_table:
            if dependency in item:
                os.system(item)



