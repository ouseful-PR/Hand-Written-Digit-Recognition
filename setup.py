from setuptools import setup


setup(
    name="nb-handwritten-digit",
    packages= ['nb_handwritten_digit'],
    version='0.0.1',
    include_package_data=True,
    install_requires=[
        'jupyter-server-proxy',
        'notebook'
    ],
    url="https://github.com/ouseful-PR/Hand-Written-Digit-Recognition",
    author="Benson Ruan",
    description="tony.hirst@gmail.com",
    entry_points={
        'jupyter_serverproxy_servers': [
            'nb_handwritten_digit = nb_handwritten_digit:setup_nb_handwritten_digit',
        ]
    }
)