import pytest

from test import testutils
from pnc_cli.pnc_api import pnc_api


@pytest.fixture(scope='function', autouse=True)
def get_running_api():
    global running_api
    running_api = pnc_api.running_builds


@pytest.fixture(scope='function', autouse=True)
def get_configs_api():
    global configs_api
    configs_api = pnc_api.build_configs


@pytest.fixture(scope='function', autouse=True)
def get_sets_api():
    global sets_api
    sets_api = pnc_api.build_group_configs


def test_get_all(new_config):
    # start a build so that a build is running
    # need to run a legitimate build, create a buildconfiguration that will start running
    configs_api.trigger(id=new_config.id)
    running_builds = running_api.get_all(page_size=1000).content
    assert running_builds is not None


def test_get_specific_no_id():
    testutils.assert_raises_valueerror(running_api, 'get_specific', id=None)


def test_get_specific_invalid_param():
    testutils.assert_raises_typeerror(running_api, 'get_specific', id=1)


def test_get_specific(new_config):
    # same as above
    triggered_build = configs_api.trigger(id=new_config.id).content
    running_build = running_api.get_specific(id=triggered_build.id)
    assert running_build is not None


def test_get_all_for_bc_no_id():
    testutils.assert_raises_valueerror(running_api, 'get_all_for_bc', id=None)


def test_get_all_for_bc_invalid_param():
    testutils.assert_raises_typeerror(running_api, 'get_all_for_bc', id=1)


def test_get_all_for_bc(new_config):
    configs_api.trigger(id=new_config.id)
    response = running_api.get_all_for_bc(id=new_config.id)
    assert response is not None

