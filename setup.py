import setuptools

setuptools.setup(
    name="flask-admin-tablefield",
    version="0.2.2022.3.7",
    author="hxh",
    author_email="cllenishxh@gmail.com",
    description="table field for flask-admin!",
    long_description="table field for flask-admin!",
    long_description_content_type="text/markdown",
    url="https://github.com/cllen/flask-admin-tablefield",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        "WTForms==2.2.1",
        "jinja2==3.0.3",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)