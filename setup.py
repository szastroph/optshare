from setuptools import setup, find_packages

install_requires = ["pandas >=1.4.3", "requests"]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    # these rarely change
    name="optshare",
    description='Python package for option, index, and yield data',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='derivatives, finance',
    license='Free for non-commercial use',
    author='Yu Lu',
    author_email='luyudso@gmail.com',
    url='https://yulu0131.github.io/',
    # these may change frequently
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.10',
    install_requires=install_requires,
    package_data={'optshare': ['option/option_info.csv']},
)