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
parser.add_commands([uc.login])

parser.add_commands([brewpush.push_build,
                     brewpush.push_build_set,
                     brewpush.push_build_status],
                    namespace="brew-push", namespace_kwargs=brewpush.namespace_kwargs)
parser.add_commands([buildconfigurations.add_dependency,
                     buildconfigurations.build,
                     buildconfigurations.create_build_configuration,
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
                    namespace="build-config", namespace_kwargs=buildconfigurations.namespace_kwargs)
parser.add_commands([buildrecords.get_build_record,
                     runningbuilds.get_running_build,
                     buildrecords.get_audited_configuration_for_record,
                     buildrecords.get_log_for_record,
                     buildrecords.list_build_records,
                     runningbuilds.list_running_builds,
                     buildrecords.list_attributes,
                     buildrecords.list_artifacts,
                     buildrecords.list_built_artifacts,
                     buildrecords.list_dependency_artifacts,
                     buildrecords.query_by_attribute,
                     buildrecords.list_records_for_build_configuration,
                     buildrecords.list_records_for_project,
                     buildrecords.put_attribute,
                     buildrecords.remove_attribute],
                    namespace="build", namespace_kwargs=buildrecords.namespace_kwargs)
parser.add_commands([environments.create_environment,
                     environments.delete_environment,
                     environments.get_environment,
                     environments.list_environments,
                     environments.update_environment],
                    namespace="environment", namespace_kwargs=environments.namespace_kwargs)
parser.add_commands([buildconfigsetrecords.get_build_configuration_set_record,
                     buildconfigsetrecords.list_build_configuration_set_records,
                     buildconfigsetrecords.list_records_for_build_config_set],
                    namespace="group-build", namespace_kwargs=buildconfigsetrecords.namespace_kwargs)
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
parser.add_commands([productmilestones.create_milestone,
                     productmilestones.close_milestone,
                     productmilestones.get_milestone,
                     productmilestones.list_distributed_artifacts,
                     productmilestones.list_distributed_builds,
                     productmilestones.list_milestones,
                     productmilestones.list_milestones_for_version,
                     productmilestones.update_milestone],
                    namespace="product-milestone", namespace_kwargs=productmilestones.namespace_kwargs)
parser.add_commands([productreleases.create_release,
                     productreleases.get_release,
                     productreleases.list_product_releases,
                     productreleases.list_releases_for_version,
                     productreleases.update_release],
                    namespace="product-release", namespace_kwargs=productreleases.namespace_kwargs)
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
parser.add_commands([repositoryconfigurations.get_repository_configuration,
                     repositoryconfigurations.update_repository_configuration,
                     repositoryconfigurations.create_repository_configuration,
                     repositoryconfigurations.list_repository_configurations,
                     repositoryconfigurations.match_repository_configuration,
                     repositoryconfigurations.search_repository_configuration],
                    namespace="repository", namespace_kwargs=repositoryconfigurations.namespace_kwargs)
tool_kwargs = {'title': 'Various tools that help with working with PNC.',
               'description': 'Various tools that help with working with PNC.'}
parser.add_commands([generate_repo.generate_repo_list,
                     archives.generate_sources_zip],
                    namespace="tool", namespace_kwargs=tool_kwargs)
parser.add_commands([makemead.make_mead])
parser.autocomplete()

replace_map = {'foo': ['bar', 'baz'],
               'add-dependency': ['build-config', 'add-dependency'],
               'build': ['build-config', 'build'],
               'create-build-configuration': ['build-config', 'create'],
               'create-build-configuration-process': ['build-config', 'create-process'],
               'delete-build-configuration': ['build-config', 'delete'],
               'get-build-configuration': ['build-config', 'get'],
               'get-revision-of-build-configuration': ['build-config', 'get-revision'],
               'list-build-configurations,': ['build-config', 'list'],
               'list-build-configurations-for-product': ['build-config', 'list-by-product'],
               'list-build-configurations-for-product-version': ['build-config', 'list-by-product-version'],
               'list-build-configurations-for-project': ['build-config', 'list-by-project'],
               'list-dependencies': ['build-config', 'list-dependencies'],
               'list-revisions-of-build-configuration': ['build-config', 'list-revisions'],
               'remove-dependency': ['build-config', 'remove'],
               'update-build-configuration': ['build-config', 'update'],
               'get-build-record': ['builds', 'get'],
               'get-running-build': ['builds', 'get-running'],
               'get-audited-configuration-for-record': ['builds', 'get-audited-configuration'],
               'get-log-for-record': ['builds', 'get-build-log'],
               'list-build-records': ['builds', 'list'],
               'list-running-builds': ['builds', 'list-running'],
               'list-artifacts': ['builds', 'list-artifacts'],
               'list-attributes': ['builds', 'list-attributes'],
               'list-built-artifacts': ['builds', 'list-built-artifacts'],
               'list-dependency-artifacts': ['builds', 'list-dependency-artifacts'],
               'list-records-for-build-configuration': ['builds', 'list-by-build-config'],
               'list-records-for-project': ['builds', 'list-by-project'],
               'put-attribute': ['builds', 'add-attribute'],
               'remove-attribute': ['builds', 'remove-attribute'],
               'query-by-attribute': ['builds', 'list-by-attribute'],
               'create-environment': ['environment', 'create'],
               'delete-environment': ['environment', 'delete'],
               'get-environment': ['environment', 'get'],
               'list-environments': ['environment', 'list'],
               'update-environment': ['environment', 'update'],
               'get-build-configuration-set-record': ['group-build', 'get'],
               'list-build-configuration-set-records': ['group-build', 'list'],
               'list-records-for-build-config-set': ['group-build', 'list-by-build-group-config'],
               'add-build-configuration-to-set': ['group-build-configs', 'add-build-config'],
               'build-set': ['group-build-configs', 'build'],
               'create-build-configuration-set': ['group-build-configs', 'create'],
               'delete-build-configuration-set': ['group-build-configs', 'delete'],
               'get-build-configuration-set': ['group-build-configs', 'get'],
               'list-build-configuration-sets': ['group-build-configs', 'list'],
               'list-build-configurations-for-set': ['group-build-configs', 'list-build-congis'],
               'list-build-records-for-set': ['group-build-configs', 'list-builds'],
               'list-build-set-records': ['group-build-configs', 'list-group-builds'],
               'latest-build-set-records-status': ['group-build-configs', 'status'],
               'remove-build-configuration-from-set': ['group-build-configs', 'remove-build-config'],
               'update-build-configuration-set': ['group-build-configs', 'update'],
               'create-product': ['product', 'create'],
               'get-product': ['product', 'get'],
               'list-products': ['product', 'list'],
               'list-versions-for-product': ['product', 'list-by-product'],
               'update-product': ['product', 'update'],
               'create-milestone': ['product-milestone', 'create'],
               'close-milestone': ['product-milestone', 'close'],
               'get-milestone': ['product-milestone', 'get'],
               'list-distributed-artifacts': ['product-milestone', 'list-distributed-artifacts'],
               'list-distributed-builds': ['product-milestone', 'list-distributed-builds'],
               'list-milestones': ['product-milestone', 'list'],
               'list-milestones-for-version': ['product-milestone', 'list-by-version'],
               'update-milestone': ['product-milestone', 'update'],
               'create-release': ['product-release', 'create'],
               'get-release': ['product-release', 'get'],
               'list-product-releases': ['product-release', 'list'],
               'list-releases-for-version': ['product-release', 'list-by-version'],
               'update-release': ['product-release', 'update'],
               'create-product-version': ['product-version', 'create'],
               'get-product-version': ['product-version', 'get'],
               'list-product-versions': ['product-version', 'list'],
               'update-product-version': ['product-version', 'update'],
               'create-project': ['project', 'create'],
               'delete-project': ['project', 'delete'],
               'get-project': ['project', 'get'],
               'list-projects': ['project', 'list'],
               'update-project': ['project', 'update'],
               'get-repository-configuration': ['repository', 'get'],
               'update-repository-configuration': ['repository', 'update'],
               'create-repository-configuration': ['repository', 'create'],
               'list-repository-configurations': ['repository', 'list'],
               'search-repository-configuration': ['repository', 'search-by-url'],
               'generate-repo-list': ['tools', 'generate-repo-list'],
               'generate-sources-zip': ['tools', 'generate-sources-zip']
                
                
                
                
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
