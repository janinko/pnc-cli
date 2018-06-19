__author__ = 'thauser'

import pytest

import pnc_cli.user_config as uc
from pnc_cli import environments
from pnc_cli import buildconfigurations
from pnc_cli import buildconfigurationsets
from pnc_cli import productmilestones
from pnc_cli import productreleases
from pnc_cli import products
from pnc_cli import productversions
from pnc_cli import projects
from pnc_cli import repositoryconfigurations
from test import testutils


@pytest.fixture(scope='module')
def new_product():
    randname = testutils.gen_random_name()
    product = products.create_product_raw(randname + "-product",
                                      randname,
                                      description="PNC CLI: test product")
    return product


@pytest.fixture(scope='module')
def new_project(request):
    project = projects.create_project_raw(name=testutils.gen_random_name() + '-project',
                                      description="PNC CLI: test project")

    def teardown():
        projects.delete_project_raw(id=project.id)

    request.addfinalizer(teardown)
    return project


@pytest.fixture(scope='function')
def new_set(request):
    set = buildconfigurationsets.create_build_configuration_set_raw(name=testutils.gen_random_name() + "-set",
                                                                product_version_id=1)

    def teardown():
        buildconfigurationsets.delete_build_configuration_set_raw(id=set.id)

    request.addfinalizer(teardown)
    return set


# helper function for checking BC creation
def contains_event_type(events, types):
    for event in events:
        if (event.event_type in types):
            return True
    return False

def new_repository(project_number):
    if (project_number == 2):
        ending = '-2'
    elif (project_number == 3):
        ending = '-3'
    else:
        ending = ''
    repo_url = 'git+ssh://code.stage.engineering.redhat.com/productization/github.com/pnc-simple-test-project'+ending+'.git'

    content = repositoryconfigurations.match_repository_configuration_raw(repo_url)
    if content:
        return content[0]
    return repositoryconfigurations.create_repository_configuration_raw(repo_url,prebuild_sync=False)

@pytest.fixture(scope='function')
def new_config(request, new_project, new_version):
    print("request: ", request)
    print("new_project: ", new_project)
    print("new_version: ", new_version)
    created_bc = create_config(request, new_project, new_version, 1)
    return created_bc


def create_config(request, new_project, new_version, project_number):
    rc = new_repository(project_number)

    # detect an appropriate environment
    available_environments = environments.list_environments_raw()

    for x in available_environments:
        # set the env_id to one of the environments. This allows us to set
        # env_id to an existing environment id even if no environment contains
        # "OpenJDK 1.8.0; Mvn 3.3.9" 
        env_id = x.id
        if "OpenJDK 1.8.0; Mvn 3.3.9" in x.name:
            env_id = x.id
            break

    bc_name = testutils.gen_random_name() + '-config'
    created_bc = buildconfigurations.create_build_configuration_raw(
        name=bc_name,
        project=new_project.id,
        environment=env_id,
        build_script='mvn deploy',
        product_version_id=new_version.id,
        repository_configuration=rc.id,
        scm_revision='master')
    print("created: ", created_bc)

    def teardown():
        buildconfigurations.delete_build_configuration_raw(id=created_bc.id)

    request.addfinalizer(teardown)
    return created_bc

@pytest.fixture(scope='module')
def new_version(new_product):
    version = productversions.create_product_version_raw(
        product_id=new_product.id,
        version=get_unique_version(new_product.id))
    return version


def get_unique_version(product_id):
    rand_version = testutils.gen_random_version()
    existing = products.list_versions_for_product_raw(id=product_id, page_size=100000)
    while existing is not None and rand_version in [x.version for x in existing]:
        rand_version = testutils.gen_random_version()
    return rand_version


@pytest.fixture(scope='module')
def new_milestone(new_version):
    starting = '2015-01-01'
    ending = '2016-01-01'
    milestone = productmilestones.create_milestone_raw(
        version='1.build3',
        starting_date=starting,
        planned_end_date=ending,
        download_url='localhost:8080/build3',
        product_version_id=new_version.id)
    return milestone


@pytest.fixture(scope='module')
def new_release(new_milestone):
    release_time = '2016-01-01'
    release = productreleases.create_release_raw(
        version="1.DR1",
        release_date=release_time,
        download_url="pnc-cli-test-url",
        product_version_id=new_milestone.product_version_id,
        product_milestone_id=new_milestone.id,
        support_level='EOL'
    )
    return release
