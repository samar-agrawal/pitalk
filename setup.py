from setuptools import setup, find_packages

setup(
    name='pitalk',
    version='1.1',
    description='Python Bot to talk to raspberry pi through Telegram',
    author='Samar',
    author_email='samar@enstino.com',
    packages = find_packages(),
    license = 'MIT',
    package_dir = {'': '.'},
    install_requires=['telepot', 'aiml'],
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Communications :: Chat'
    ],
    zip_safe=True,
)
