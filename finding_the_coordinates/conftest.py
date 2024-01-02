import pytest


def pytest_addoption(parser):
    parser.addoption("--email", action="store")


def pytest_configure():
    pytest.test_results = {
        "FAIL": 0,
        "PASS": 0
    }


@pytest.hookimpl
def pytest_report_teststatus(report, config):
    if report.when == 'call':
        if report.outcome == "failed":
            pytest.test_results["FAIL"] += 1
            return "FAIL", "F", "FAILED"
        elif report.outcome == "passed":
            pytest.test_results["PASS"] += 1
            return "PASS", "P", "PASSED"


def pytest_sessionfinish(session, exitstatus):
    pass
