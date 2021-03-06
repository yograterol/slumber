import os
import sys
from setuptools import setup

install_requires = ["aiohttp"]
tests_require = ["mock", "unittest2"]

base_dir = os.path.dirname(os.path.abspath(__file__))

version = "2017.7"

if sys.argv[-1] == 'publish':
    os.system("git tag -a %s -m 'v%s'" % (version, version))
    os.system("python setup.py sdist bdist_wheel upload -r pypi")
    print("Published version %s, do `git push --tags` to push new tag to remote" % version)
    sys.exit()

if sys.argv[-1] == 'syncci':
    os.system("panci --to=tox .travis.yml > tox.ini");
    sys.exit();

setup(
    name = "slumber",
    version = version,
    description = "A library that makes consuming a REST API easier and more convenient",
    long_description="\n\n".join([
        open(os.path.join(base_dir, "README.rst"), "r").read(),
        open(os.path.join(base_dir, "CHANGELOG.rst"), "r").read()
    ]),
    url="http://github.com/samgiles/slumber",
    author="Yohan Graterol",
    author_email="y@platzi.com",
    maintainer="Yohan Graterol",
    maintainer_email="y@platzi.com",
    classifiers=[
        # See: https://pypi.python.org/pypi?:action=list_classifiers
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        # List of python versions and their support status:
        # https://en.wikipedia.org/wiki/CPython#Version_history
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
    ],
    packages = ["slumber"],
    zip_safe = False,
    install_requires = install_requires,
    tests_require = tests_require,
    test_suite = "tests.get_tests",
)
