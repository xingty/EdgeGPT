from pathlib import Path

from setuptools import find_packages
from setuptools import setup

DOCS_PATH = Path(__file__).parents[0] / "docs/README.md"
PATH = Path("README.md")
if not PATH.exists():
    with Path.open(DOCS_PATH, encoding="utf-8") as f1:
        with Path.open(PATH, "w+", encoding="utf-8") as f2:
            f2.write(f1.read())

setup(
    name="EdgeGPT-fork",
    version="1.0.2",
    license="The Unlicense",
    author="Antonio Cheong,Bigbyto",
    author_email="acheong@student.dalat.org,bigbyto@gmail.com",
    description="Reverse engineered Edge Chat API",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/xingty/EdgeGPT",
    project_urls={"Bug Report": "https://github.com/xingty/EdgeGPT/issues/new"},
    entry_points={
        "console_scripts": [
            "edge-gpt = EdgeGPT.main:main",
            "edge-gpt-image = EdgeGPT.ImageGen:main",
        ],
    },
    install_requires=[
        "httpx[socks]>=0.24.0",
        "aiohttp",
        "websockets",
        "rich",
        "certifi",
        "prompt_toolkit",
        "requests",
        "BingImageCreator-fork>=0.7.6",
        "curl_cffi"
    ],
    long_description=Path.open(PATH, encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    py_modules=["EdgeGPT", "EdgeUtils", "ImageGen"],
    classifiers=[
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
