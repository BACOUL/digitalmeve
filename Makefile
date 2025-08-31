.PHONY: lint test fmt all
fmt:
\tblack .
lint:
\tflake8
test:
\tpytest -q
all: fmt lint test
