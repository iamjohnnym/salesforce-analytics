from setuptools import setup

def readme():
    with open('README.md', 'w') as f:
        return f.read()


setup(name='salesforce-analytics',
      version='0.1.2',
      description="""Client to injest SalesForce Case information and generate
      analytics for trends and current statistics for evaluating on the
      fly""",
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Text Processing :: Linguistic',
          ],
      keywords='salesforce analytics libary',
      url='git@gitlab.eng.cleardata.com:operations/salesforce/salesforce-analytics.git',
      author='ClearDATA',
      author_email='john.martin@cleardata.com',
      license='MIT',
      packages=['salesforce_analytics'],
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose']
     )
