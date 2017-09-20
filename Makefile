excludes = \*~ \*.pyc .cache/\* test_\* __pycache__/\*

.PHONY: test
test:
	nosetests --with-cov --cov salesforce_analytics

.PHONY: bandit
bandit:
	bandit -r salesforce_analytics/
