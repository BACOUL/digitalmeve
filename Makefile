.PHONY: lint test fmt all
fmt:
\tblack .
lint:
\tflake8
test:
\tpytest -q
all: fmt lint test
.PHONY: test coverage
test:
	pytest -q

coverage:
	pytest -q --cov=digitalmeve --cov-report=term --cov-report=xml
	@echo "Coverage XML généré: coverage.xml"
