import os
from setuptools import setup, find_packages


setup(
    name='vcpkgpip',
    version='1.0.0',
    url='https://github.com/AlyShmahell/vcpkgpip',
    author='Aly Shmahell',
    author_email='',
    description='a python wrapper for vcpkg',
	long_description=(open('README.md', encoding='utf-8').read() if os.path.exists('README.md')
                        else ''),
    long_description_content_type='text/markdown',
    packages=['vcpkgpip'],    
    install_requires=[],
    entry_points = {
        "console_scripts": [
            "vcpkg = vcpkgpip.__main__:main",
            "vcpkg-bootstrap = vcpkgpip.__main__:bootstrap",
        ]
    }
)