import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TweetBot", 
    version="0.0.1",
    author="Abdullah Arif",
    author_email="abdullahmeo11@gmail.com",
    description="A bot that can take tweets from twitter and generate twitter that mimic the user",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Aarif123456/tweetGenerator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.8',
)