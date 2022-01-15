from setuptools import setup, find_packages

setup(
    name='transemon',
    version='1.0',
    author="BlueXIII",
    author_email="bluexiii@163.com",
    description="A Tool Pack For Excel Data Cleaning",
    url="https://www.bluexiii.com/",
    packages=['transemon', 'transemon.cleaner', 'transemon.config', 'transemon.pipeline', 'transemon.repository'],
    entry_points={
        'console_scripts': [
            'transemon = transemon.entry:entry'
        ]
    },
    install_requires=['xlutils', 'xlrd', 'jieba', 'faker'],
)
