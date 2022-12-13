from setuptools import setup

'''To build + upload run python -m build then twine upload dist/*'''

setup(name='aurelii',
      version='0.1.2.2',
      description='Aurelii file format python package',
      long_description='Open source Aurelii file format python package by Xonize in OpenDTK',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='file format data serialization open source',
      url='http://github.com/xonize/opendtk/aurelii',
      author='Westsi',
      author_email='westsi@protonmail.com',
      license='GPL-3',
      packages=['aurelii'],
      install_requires=[
          'markdown',
      ],
      include_package_data=True,
      zip_safe=False)