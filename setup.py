from os.path import join, dirname

from setuptools import setup, find_packages

here = dirname(__file__)

long_description = (open(join(here, "README.rst")).read() + "\n\n" +
                    open(join(here, "CHANGES.rst")).read() + "\n\n" +
                    open(join(here, "TODO.rst")).read())

dependency_links = [
    'git+git://github.com/mjumbewu/pymeta.git@master#egg=pymeta-0.5.0',
    'git+git://github.com/mjumbewu/pybars.git@master#egg=pybars-0.1.0',
]

def get_version():
    fh = open(join(here, "djangobars", "__init__.py"))
    try:
        for line in fh.readlines():
            if line.startswith("__version__ ="):
                return line.split("=")[1].strip().strip('"')
    finally:
        fh.close()

setup(
    name="djangobars",
    version=get_version(),
    description="An extension to allow Django to use Handlebars templates through the pybars port of Handlebars.js",
    long_description=long_description,
    author="Mjumbe Wawatu Ukweli",
    author_email="mjumbewu@gmail.com",
    url="https://github.com/mjumbewu/djangobars/",
    packages=find_packages(),
    dependency_links=dependency_links,
    install_requires=[
        "pymeta==0.5.0",
        "pybars==0.1.0"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Framework :: Django",
    ],
)
