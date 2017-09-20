excludes = \*~ \*.pyc .cache/\* test_\* __pycache__/\*

.PHONY: clean
clean:
	find . -type f -name "*.pyc" -delete

.PHONY: test
test:
	nosetests --with-cov --cov salesforce_analytics

.PHONY: bandit
bandit:
	bandit -r salesforce_analytics/

.PHONY: coveralls
coveralls:
	coveralls

.PHONY: prospector
prospector:
	prospector