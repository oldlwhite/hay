import setuptools

with open("README.md", "rb") as fh:
    long_description = fh.read().decode("utf8")

setuptools.setup(
    name="hay",
    version="0.0.2",
    author='白旭东,储国庆',
    author_email='2216403312@qq.com',
    description='基于pyppeteer的chromenium操控库',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/oldlwhite/hay',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)


