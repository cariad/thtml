from pathlib import Path

from setuptools import setup  # pyright: reportMissingTypeStubs=false

from thtml import get_version

readme_path = Path(__file__).parent / "README.md"

with open(readme_path, encoding="utf-8") as f:
    long_description = f.read()

classifiers = [
    "Environment :: Console",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Topic :: Utilities",
    "Typing :: Typed",
]

version = get_version()

if "a" in version:
    classifiers.append("Development Status :: 3 - Alpha")
elif "b" in version:
    classifiers.append("Development Status :: 4 - Beta")
else:
    classifiers.append("Development Status :: 5 - Production/Stable")

classifiers.sort()

setup(
    author="Cariad Eccleston",
    author_email="cariad@cariad.io",
    classifiers=classifiers,
    description="CLI tool for converting text to HTML",
    entry_points={
        "console_scripts": [
            "thtml=thtml.__main__:cli_entry",
        ],
    },
    include_package_data=True,
    install_requires=[
        "ansiscape>=1.0.0",
        "naughtty>=1.0.0",
        "pyyaml",
    ],
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="thtml",
    packages=[
        "thtml",
        "thtml.scopes",
        "thtml.themes",
        "thtml.theming",
        "thtml.version",
    ],
    package_data={
        "thtml": ["py.typed"],
        "thtml.scopes": ["py.typed"],
        "thtml.themes": ["py.typed"],
        "thtml.theming": ["py.typed"],
        "thtml.version": ["py.typed"],
    },
    python_requires=">=3.8",
    url="https://github.com/cariad/thtml",
    version=version,
)
