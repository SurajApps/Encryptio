import setuptools

__project__ = "Encryptio-GUI-pkg-SurajApps"
__version__ = "1.0"
__description__ = "A python module to find encrypt and decrypt files using Fernet encryption"
__packages__ = ["Encryptio_GUI"]
__author__ = "Suraj Apps"
__url__ = "https://surajapps.github.io"
__classifiers__ = [
    "Development Status :: 3 - Alpha",
    "Environment :: MacOS X",
    "Environment :: Win32 (MS Windows)"
    "Intended Audience :: System Administrators",
    "Intended Audience :: End Users/Desktop",
    "Intended Audience :: Education",
    "Programming Language :: Python :: 3",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Topic :: Security :: Cryptography",
    "Topic :: Security"

]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=__project__,
    version=__version__,
    author=__author__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=__url__,
    packages=__packages__,
    classifiers=__classifiers__,
    python_requires='>=3.7',
    entry_points=
    {
        "console_scripts":
        [
            "encryptio_gui = Encryptio_GUI.Menu:MainMenu"
        ]
    }
)