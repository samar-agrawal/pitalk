from setuptools import setup, find_packages


setup(
    name='pitalk',
    version='1.0',
    author='Samar',
    author_email='samar@enstino.com',
    packages = find_packages(),
    package_dir = {'': '.'},
    install_requires=['telepot', 'aiml'],
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=True,
)
