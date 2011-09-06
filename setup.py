import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages

import multi_registry

setup(
    name = "multi-registry",
    version = multi_registry.__version__,
    description = 'A module that aggregates key-value attributes from multiple sources',
    packages = find_packages(),
    author = 'Evgeny.Fadeev',
    author_email = 'evgeny.fadeev@gmail.com',
    license = 'BSD',
    keywords = 'settings, registry',
    url = 'http://askbot.org',
    include_package_data = True,
    install_requires = ['import-utils',],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Communications :: Usenet News',
    ],
    long_description = multi_registry.MultiRegistry.__doc__
)
