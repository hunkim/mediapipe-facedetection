from setuptools import setup, find_packages
setup(
    name="mediapipe",
    version="0.1",
    url="https://github.com/hunkim/streamlit-google-oauth",
    author="Sung Kim",
    author_email="hunkim@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
    ]
)
