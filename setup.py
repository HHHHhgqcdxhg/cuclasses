import setuptools

with open("README.md", "r",encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cuclasses",
    version="0.0.3",
    author="HHHHhg",
    author_email="2894700792@qq.com",
    description="useful classes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HHHHhgqcdxhg/cuclasses",
    packages=setuptools.find_packages(),
    classifiers=[
        "Natural Language :: Chinese (Simplified)"
    ],
)
