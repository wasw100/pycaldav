# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages

version = '0.0.1'

if __name__ == '__main__':
    setup(
        name='pycaldav',
        version=version,
        description="CalDAV (RFC4791) client library",
        classifiers=["Development Status :: 4 - Beta",
                     "Intended Audience :: Developers",
                     "License :: OSI Approved :: GNU General "
                     "Public License (GPL)",
                     "License :: OSI Approved :: Apache Software License",
                     "Operating System :: OS Independent",
                     "Programming Language :: Python",
                     "Topic :: Office/Business :: Scheduling",
                     "Topic :: Software Development :: Libraries "
                     ":: Python Modules"],
        keywords='',
        author='wasw100',
        author_email='wasw100@gmail.com',
        url='https://github.com/wasw100/pycaldav',
        license='GPL',
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
        install_requires=['vobject', 'lxml', 'nose', 'coverage', 'sphinx', 'requests'],
    )
