"""
Return config on servers to start for nb_handwritten_digit
See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os
import pkg_resources

def setup_nb_handwritten_digit():
    fpath = pkg_resources.resource_filename('nb_handwritten_digit', 'static/')
    #fpath = "/home/jovyan/nb_handwritten_digit/static"
    return {
        'command': ["python", "-m", "http.server", "--directory", fpath, "{port}"],
        'environment': {},
        'launcher_entry': {
            'title': 'nb_handwritten_digit',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'nb_handwritten_digit.svg')
        }
    }