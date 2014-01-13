from setuptools import setup, find_packages
import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


long_description = (
    read('README.md')
    + '\n' +
    read('CONTRIBUTORS.txt')
    + '\n' +
    read('CHANGES.txt'))


setup(name='kotti_versioning',
      version='0.1dev',
      description="""Add a versioning support to your Kotti site""",
      long_description=long_description,
      classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Framework :: Pylons',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'License :: Repoze Public License',
      ],
      keywords='kotti addon history versioning',
      author='Vanc Levstik',
      author_email='vanc.levstik@gmail.com',
      url='http://pypi.python.org/pypi/kotti_versioning',
      license='BSD-derived (http://www.repoze.org/LICENSE.txt)',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'Kotti>=0.8a1',
      ],
      tests_require=[],
      entry_points={
          'fanstatic.libraries': [
              'kotti_versioning = kotti_versioning.fanstatic:library',
          ],
      },
      extras_require={},
      message_extractors={'kotti_versioning': [
            ('**.py', 'lingua_python', None),
            ('**.zcml', 'lingua_xml', None),
            ('**.pt', 'lingua_xml', None),
            ]},
      )
