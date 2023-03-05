import pytest
from utils.logger import logger


def pytest_runtest_logreport(report):
    if report.failed:
        logger.error(report.longreprtext)
    elif report.when == 'call':
        logger.info(f'{report.nodeid} PASSED')


def pytest_addoption(parser):
    parser.addoption('--alluredir', action='store', default='allure-results')


@pytest.fixture(scope='session')
def allure_report(request):
    return request.config.getoption('--alluredir')
