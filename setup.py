from setuptools import setup, find_packages
import textwrap
setup(
    name="dongsam",
    version="0.1",
    packages=find_packages(),
    scripts=[],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    # install_requires=[],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        # '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        # 'hello': ['*.msg'],
    },

    # metadata to display on PyPI
    author="Dongsam Byun",
    author_email="dongsamb@gmail.com",
    description="Python Utils Pacakage",
    license="Apache",
    keywords="dongsam",
    url="https://github.com/dongsam/dongsam",   # project home page, if any
    project_urls={
        # "Bug Tracker": "https://bugs.example.com/HelloWorld/",
        # "Documentation": "https://docs.example.com/HelloWorld/",
        "Source Code": "https://github.com/dongsam/dongsam",
    },
    classifiers = textwrap.dedent("""
        Development Status :: 5 - Production/Stable
        Intended Audience :: Developers
        License :: OSI Approved :: MIT License
        Operating System :: OS Independent
        Programming Language :: Python :: 2.7
        Programming Language :: Python :: 3.5
        Programming Language :: Python :: 3.6
        Programming Language :: Python :: 3.7
        Topic :: Software Development :: Libraries :: Python Modules
        Topic :: System :: Archiving :: Packaging
        Topic :: System :: Systems Administration
        Topic :: Utilities
        """).strip().splitlines(),
    python_requires = '>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',
    extras_require={
        'dotenv': ['python-dotenv'],
        'dev': [
            'pytest>=3',
            'coverage',
            'tox',
            'sphinx',
            'pallets-sphinx-themes',
            'sphinxcontrib-log-cabinet',
        ],
        'docs': [
            'sphinx',
            'pallets-sphinx-themes',
            'sphinxcontrib-log-cabinet',
        ]
    },
    zip_safe=False,
    # could also include long_description, download_url, classifiers, etc.
)