import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="lastplayer",
    version="0.0.2",
    author="Tudor Roman",
    author_email="tudurom@gmail.com",
    description="Simple program that keeps the order of the last used players",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/ricede/lastplayer",
    scripts=['lastplayer/lastplayer'],
    packages=['lastplayer'],
    python_requires='>=3.5',
    install_requires=[
        'PyGObject',
        'dbus-python',
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: POSIX",
        "Topic :: Desktop Environment",
    ),
)
