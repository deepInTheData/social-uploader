from os.path import dirname, join
from sys import version_info

import setuptools

if version_info < (3, 6, 0):
    raise SystemExit("Sorry! upgenius requires python 3.6.0 or later.")

with open(join(dirname(__file__), "upgenius/VERSION"), "rb") as fh:
    version = fh.read().decode("ascii").strip()

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

packages = setuptools.find_packages()
packages.extend(["upgenius"])


requires = [
    "playwright>=1.33.0",
    "better-exceptions>=0.2.2" "parsel>=1.5.2",
    "requests>=2.22.0",
    "selenium>=3.141.0",
    "bs4>=0.0.1",
    "bitarray>=1.5.3",
    "urllib3>=1.25.8",
    "loguru>=0.5.3",
    "webdriver-manager>=3.5.3",
    "terminal-layout>=2.1.3",
    "playwright_stealth #==1.0.5",
    "async_class #==0.5.0",
    "httpx",
    "numpy",
    "colorama==0.4.6",
    "undetected-playwright",
    "openpyxl",
]
setuptools.setup(
    name="upgenius",
    version=version,
    author="wanghaisheng",
    author_email="admin@tiktokastudio.com",
    description="using playwright and selenium to upload and schedule publish video on social media platform like youtube,tiktok,douyin etc.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/wanghaisheng/tiktoka-studio-uploader",
    download_url="https://github.com/wanghaisheng/tiktoka-studio-uploader/tarball/version",
    # packages=["upgenius", "upgenius.utils", "upgenius.tiktok", "upgenius.db", "upgenius.network"],
    packages=packages,
    # so we emit to hard code the package/sub-folder name
    include_package_data=True,
    # if not true, js folder wont included
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requires,
    python_requires=">=3.6",
)
