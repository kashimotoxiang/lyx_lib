# coding=utf-8
"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import find_packages, setup

setup(
    name='lyx',
    version='0.7.1',
    description=('python toolbox created by kashimotoxiang'),
    long_description=('python toolbox created by kashimotoxiang'),
    author='kashimotoxiang',
    author_email='kashimotoxiang@gmail.com',
    maintainer='kashimotoxiang',
    maintainer_email='kashimotoxiang@gmail.com',
    license='MIT',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/kashimotoxiang/lyx_lib',
    install_requires=[
        'joblib',
    ],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.7',
)
