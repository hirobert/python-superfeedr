from setuptools import setup, find_packages

setup(
    name='superfeedr',
    version='1.0.0',
    author='Robert Neshanian',
    author_email='robert@hirobert.com',
    url='http://www.hirobert.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'superfeedr = superfeedr:main'
        ]
    },
    classifiers=[
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
