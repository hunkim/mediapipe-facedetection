from setuptools import setup
setup(
    name="mediapipe",
    version="0.1",
    url="https://github.com/hunkim/streamlit-google-oauth",
    author="Sung Kim",
    author_email="hunkim@gmail.com",
    packages=["mediapipe"],
    package_data={"mediapipe": ["*"]},
    install_requires=[
        "numpy",
    ]
)
