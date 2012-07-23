from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='captionstransformer',
      version=version,
      description="",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='caption subtitle',
      author='JeanMichel FRANCOIS aka toutpt',
      author_email='toutpt@gmail.com',
      url='https://github.com/toutpt/captionstranformer',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'beautifulsoup4',
          # -*- Extra requirements: -*-
      ],
      extras_require = {'test': ['unittest2']},
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      captionstranformer = captionstransformer.script:main
      """,
      )
