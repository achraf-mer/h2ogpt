import os
import sys
import importlib.util


def pytest_itemcollected(item):
    item.name = item.name + os.getenv("PYTEST_TEST_NAME", "")


def pytest_sessionstart(session):
    if not os.getenv("BUILD_NUMBER", None):
        return
    try:
        for location in importlib.util.find_spec("h2ogpt").submodule_search_locations:
            sys.path.append(location)
    except AttributeError:
        pass
