import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="demo_package", # Replace with your own username
    version="0.0.4",
    author="Dimitrios Tsapnidis",
    author_email="dimitrios.tsapndis@gmail.com",
    description="A demo package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dtsap/demo_package",
    project_urls={
        "Bug Tracker": "https://github.com/dtsap/demo_package/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)