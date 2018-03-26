#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
import argh
import sys

from pnc_cli import bpmbuildconfigurations
from pnc_cli import buildconfigsetrecords
from pnc_cli import buildconfigurations
from pnc_cli import buildconfigurationsets
from pnc_cli import buildrecords
from pnc_cli import brewpush
from pnc_cli import environments
from pnc_cli import licenses
from pnc_cli import productmilestones
from pnc_cli import productreleases
from pnc_cli import products
from pnc_cli import productversions
from pnc_cli import projects
from pnc_cli import repositoryconfigurations
from pnc_cli import runningbuilds
from pnc_cli import users
from pnc_cli import archives
import pnc_cli.user_config as uc
from pnc_cli import makemead
from pnc_cli import generate_repo
import argparse
import logging


class LoggerAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=0, **kwargs):
        super(LoggerAction, self).__init__(option_strings, dest, nargs=nargs, **kwargs)

    def __call__(self, parser, namespace, values, option_string):
        if option_string == "-v" or option_string == "--verbose":
            logging.getLogger().setLevel(logging.INFO)
        elif option_string == "--debug":
            logging.getLogger().setLevel(0)
        elif option_string == "-q" or option_string == "--quiet":
            logging.getLogger().setLevel(logging.ERROR)


parser = argh.ArghParser()
parser.add_argument("--debug", action=LoggerAction, help="Print debug messages.")
parser.add_argument("-v","--verbose", action=LoggerAction, help="Print info messages.")
parser.add_argument("-q","--quiet", action=LoggerAction, help="Print only error messages.")
parser.add_commands([uc.login,
                     licenses.create_license,
                     licenses.delete_license,
                     licenses.get_license,
                     licenses.list_licenses,
                     licenses.update_license,
                     buildconfigurations.add_dependency,
                     buildconfigurations.build,
                     environments.create_environment,
                     environments.delete_environment,
                     environments.get_environment,
                     environments.list_environments,
                     environments.update_environment,
                     runningbuilds.get_running_build,
                     runningbuilds.list_running_builds,
                     productreleases.create_release,
                     productreleases.get_release,
                     productreleases.list_product_releases,
                     productreleases.list_releases_for_version,
                     productreleases.update_release,
                     productmilestones.create_milestone,
                     productmilestones.close_milestone,
                     productmilestones.get_milestone,
                     productmilestones.list_distributed_artifacts,
                     productmilestones.list_distributed_builds,
                     productmilestones.list_milestones,
                     productmilestones.list_milestones_for_version,
                     productmilestones.update_milestone,
                     repositoryconfigurations.get_repository_configuration,
                     repositoryconfigurations.update_repository_configuration,
                     repositoryconfigurations.create_repository_configuration,
                     repositoryconfigurations.list_repository_configurations,
                     repositoryconfigurations.search_repository_configuration,
                     buildconfigsetrecords.get_build_configuration_set_record,
                     buildconfigsetrecords.list_build_configuration_set_records,
                     buildconfigsetrecords.list_records_for_build_config_set,
                     users.get_logged_user,
                     makemead.make_mead,
                     generate_repo.generate_repo_list,
                     archives.generate_sources_zip])

parser.add_commands([brewpush.push_build,
                     brewpush.push_build_set,
                     brewpush.push_build_status],
                     namespace="brew-push", namespace_kwargs=brewpush.namespace_kwargs)
parser.add_commands([buildconfigurations.create_build_configuration,
                     bpmbuildconfigurations.create_build_configuration_process,
                     buildconfigurations.delete_build_configuration,
                     buildconfigurations.get_build_configuration,
                     buildconfigurations.get_revision_of_build_configuration,
                     buildconfigurations.list_build_configurations,
                     buildconfigurations.list_build_configurations_for_product,
                     buildconfigurations.list_build_configurations_for_product_version,
                     buildconfigurations.list_build_configurations_for_project,
                     buildconfigurations.list_dependencies,
                     buildconfigurations.list_revisions_of_build_configuration,
                     buildconfigurations.remove_dependency,
                     buildconfigurations.update_build_configuration],
                     namespace="build-configs", namespace_kwargs=buildconfigurations.namespace_kwargs)
parser.add_commands([buildrecords.get_build_record,
                     buildrecords.get_audited_configuration_for_record,
                     buildrecords.get_log_for_record,
                     buildrecords.list_build_records,
                     buildrecords.list_attributes,
                     buildrecords.list_artifacts,
                     buildrecords.list_built_artifacts,
                     buildrecords.list_dependency_artifacts,
                     buildrecords.query_by_attribute,
                     buildrecords.list_records_for_build_configuration,
                     buildrecords.list_records_for_project,
                     buildrecords.put_attribute,
                     buildrecords.remove_attribute],
                     namespace="builds", namespace_kwargs=buildrecords.namespace_kwargs)
parser.add_commands([buildconfigurationsets.add_build_configuration_to_set,
                     buildconfigurationsets.build_set,
                     buildconfigurationsets.create_build_configuration_set,
                     buildconfigurationsets.delete_build_configuration_set,
                     buildconfigurationsets.get_build_configuration_set,
                     buildconfigurationsets.list_build_configuration_sets,
                     buildconfigurationsets.list_build_configurations_for_set,
                     buildconfigurationsets.list_build_records_for_set,
                     buildconfigurationsets.list_build_set_records,
                     buildconfigurationsets.latest_build_set_records_status,
                     buildconfigurationsets.remove_build_configuration_from_set,
                     buildconfigurationsets.update_build_configuration_set],
                     namespace="group-build-configs", namespace_kwargs=buildconfigurationsets.namespace_kwargs)
parser.add_commands([products.create_product,
                     products.get_product,
                     products.list_products,
                     products.list_versions_for_product,
                     products.update_product],
                     namespace="product", namespace_kwargs=products.namespace_kwargs)
parser.add_commands([productversions.create_product_version,
                     productversions.get_product_version,
                     productversions.list_product_versions,
                     productversions.update_product_version,
                     productversions.list_product_versions_for_build_configuration],
                     namespace="product-version", namespace_kwargs=productversions.namespace_kwargs)
parser.add_commands([projects.create_project,
                     projects.delete_project,
                     projects.get_project,
                     projects.list_projects,
                     projects.update_project],
                     namespace="project", namespace_kwargs=projects.namespace_kwargs)
parser.autocomplete()

replace_map = { 'foo': ['bar', 'baz'],
                'get_build_record': ['builds', 'get'],
                'get_audited_configuration_for_record': ['builds', 'get-audited-configuration'],
                'get_log_for_record': ['builds', 'get-build-log'],
                'list_build_records': ['builds', 'list'],
                'list_artifacts': ['builds', 'list-artifacts'],
                'list_attributes': ['builds', 'list-attributes'],
                'list_built_artifacts': ['builds', 'list-built-artifacts'],
                'list_dependency_artifacts': ['builds', 'list-dependency-artifacts'],
                'list_records_for_build_configuration': ['builds', 'list-by-build-config'],
                'list_records_for_project': ['builds', 'list-by-project'],
                'put_attribute': ['builds', 'add-attribute'],
                'remove_attribute': ['builds', 'remove-attribue'],
                'query_by_attribute': ['builds', 'list-by-attribute'],
                'add_build_configuration_to_set': ['group-build-configs', 'add-build-config'],
                'build_set': ['group-build-configs', 'build'],
                'create_build_configuration_set': ['group-build-configs', 'create'],
                'delete_build_configuration_set': ['group-build-configs', 'delete'],
                'get_build_configuration_set': ['group-build-configs', 'get'],
                'list_build_configuration_sets': ['group-build-configs', 'list'],
                'list_build_configurations_for_set': ['group-build-configs', 'list-build-congis'],
                'list_build_records_for_set': ['group-build-configs', 'list-builds'],
                'list_build_set_records': ['group-build-configs', 'list-group-builds'],
                'latest_build_set_records_status': ['group-build-configs', 'status'],
                'remove_build_configuration_from_set': ['group-build-configs', 'remove-build-config'],
                'update_build_configuration_set': ['group-build-configs', 'update'],
                'create_product': ['product', 'create'],
                'get_product': ['product', 'get'],
                'list_products': ['product', 'list'],
                'list_versions_for_product': ['product', 'list-by-product'],
                'update_product': ['product', 'update'],
                'create_product_version': ['product-version', 'create'],
                'get_product_version': ['product-version', 'get'],
                'list_product_versions': ['product-version', 'list'],
                'update_product_version': ['product-version', 'update'],
                'create_project': ['project', 'create'],
                'delete_project': ['project', 'delete'],
                'get_project': ['project', 'get'],
                'list_projects': ['project', 'list'],
                'update_project': ['project', 'update'],
                'create_build_configuration': ['build-configuration', 'create'],
                'create_build_configuration_process': ['build-configuration', 'create-process'],
                'delete_build_configuration': ['build-configuration', 'delete'],
                'get_build_configuration': ['build-configuration', 'get'],
                'get_revision_of_build_configuration': ['build-configuration', 'get-revision'],
                'list_build_configurations,': ['build-configuration', 'list'],
                'list_build_configurations_for_product': ['build-configuration', 'list-by-product'],
                'list_build_configurations_for_product_version': ['build-configuration', 'list-by-product-version'],
                'list_build_configurations_for_project': ['build-configuration', 'list-by-project'],
                'list_dependencies': ['build-configuration', 'list-dependencies'],
                'list_revisions_of_build_configuration': ['build-configuration', 'list-revisions'],
                'remove_dependency': ['build-configuration', 'remove'],
                'update_build_configuration': ['build-configuration', 'update'],
                
                
                
                
                }

def spoof_argv():
    i=1
    while i < len(sys.argv) and sys.argv[i][0] == '-':
        i += 1
    if i < len(sys.argv):
        cmd = sys.argv[i]
        if cmd in replace_map:
            sys.argv[i] = replace_map[cmd][0]
            sys.argv.insert(i+1, replace_map[cmd][1])


def main():
    spoof_argv()
    parser.dispatch()


if __name__ == "__main__":
    main()
