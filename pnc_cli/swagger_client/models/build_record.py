# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from datetime import datetime
from pprint import pformat
from six import iteritems


class BuildRecord(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BuildRecord - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'latest_build_configuration': 'BuildConfiguration',
            'build_configuration_audited': 'BuildConfigurationAudited',
            'build_content_id': 'str',
            'submit_time': 'datetime',
            'start_time': 'datetime',
            'end_time': 'datetime',
            'user': 'User',
            'scm_repo_url': 'str',
            'scm_revision': 'str',
            'build_log': 'str',
            'status': 'str',
            'built_artifacts': 'list[Artifact]',
            'dependencies': 'list[Artifact]',
            'build_environment': 'BuildEnvironment',
            'product_milestone': 'ProductMilestone',
            'build_config_set_record': 'BuildConfigSetRecord',
            'attributes': 'dict(str, str)',
            'field_handler': 'FieldHandler'
        }

        self.attribute_map = {
            'id': 'id',
            'latest_build_configuration': 'latestBuildConfiguration',
            'build_configuration_audited': 'buildConfigurationAudited',
            'build_content_id': 'buildContentId',
            'submit_time': 'submitTime',
            'start_time': 'startTime',
            'end_time': 'endTime',
            'user': 'user',
            'scm_repo_url': 'scmRepoURL',
            'scm_revision': 'scmRevision',
            'build_log': 'buildLog',
            'status': 'status',
            'built_artifacts': 'builtArtifacts',
            'dependencies': 'dependencies',
            'build_environment': 'buildEnvironment',
            'product_milestone': 'productMilestone',
            'build_config_set_record': 'buildConfigSetRecord',
            'attributes': 'attributes',
            'field_handler': 'fieldHandler'
        }

        self._id = None
        self._latest_build_configuration = None
        self._build_configuration_audited = None
        self._build_content_id = None
        self._submit_time = None
        self._start_time = None
        self._end_time = None
        self._user = None
        self._scm_repo_url = None
        self._scm_revision = None
        self._build_log = None
        self._status = None
        self._built_artifacts = None
        self._dependencies = None
        self._build_environment = None
        self._product_milestone = None
        self._build_config_set_record = None
        self._attributes = None
        self._field_handler = None

    @property
    def id(self):
        """
        Gets the id of this BuildRecord.


        :return: The id of this BuildRecord.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BuildRecord.


        :param id: The id of this BuildRecord.
        :type: int
        """
        self._id = id

    @property
    def latest_build_configuration(self):
        """
        Gets the latest_build_configuration of this BuildRecord.


        :return: The latest_build_configuration of this BuildRecord.
        :rtype: BuildConfiguration
        """
        return self._latest_build_configuration

    @latest_build_configuration.setter
    def latest_build_configuration(self, latest_build_configuration):
        """
        Sets the latest_build_configuration of this BuildRecord.


        :param latest_build_configuration: The latest_build_configuration of this BuildRecord.
        :type: BuildConfiguration
        """
        self._latest_build_configuration = latest_build_configuration

    @property
    def build_configuration_audited(self):
        """
        Gets the build_configuration_audited of this BuildRecord.


        :return: The build_configuration_audited of this BuildRecord.
        :rtype: BuildConfigurationAudited
        """
        return self._build_configuration_audited

    @build_configuration_audited.setter
    def build_configuration_audited(self, build_configuration_audited):
        """
        Sets the build_configuration_audited of this BuildRecord.


        :param build_configuration_audited: The build_configuration_audited of this BuildRecord.
        :type: BuildConfigurationAudited
        """
        self._build_configuration_audited = build_configuration_audited

    @property
    def build_content_id(self):
        """
        Gets the build_content_id of this BuildRecord.


        :return: The build_content_id of this BuildRecord.
        :rtype: str
        """
        return self._build_content_id

    @build_content_id.setter
    def build_content_id(self, build_content_id):
        """
        Sets the build_content_id of this BuildRecord.


        :param build_content_id: The build_content_id of this BuildRecord.
        :type: str
        """
        self._build_content_id = build_content_id

    @property
    def submit_time(self):
        """
        Gets the submit_time of this BuildRecord.


        :return: The submit_time of this BuildRecord.
        :rtype: datetime
        """
        return self._submit_time

    @submit_time.setter
    def submit_time(self, submit_time):
        """
        Sets the submit_time of this BuildRecord.


        :param submit_time: The submit_time of this BuildRecord.
        :type: datetime
        """
        self._submit_time = submit_time

    @property
    def start_time(self):
        """
        Gets the start_time of this BuildRecord.


        :return: The start_time of this BuildRecord.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this BuildRecord.


        :param start_time: The start_time of this BuildRecord.
        :type: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """
        Gets the end_time of this BuildRecord.


        :return: The end_time of this BuildRecord.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this BuildRecord.


        :param end_time: The end_time of this BuildRecord.
        :type: datetime
        """
        self._end_time = end_time

    @property
    def user(self):
        """
        Gets the user of this BuildRecord.


        :return: The user of this BuildRecord.
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this BuildRecord.


        :param user: The user of this BuildRecord.
        :type: User
        """
        self._user = user

    @property
    def scm_repo_url(self):
        """
        Gets the scm_repo_url of this BuildRecord.


        :return: The scm_repo_url of this BuildRecord.
        :rtype: str
        """
        return self._scm_repo_url

    @scm_repo_url.setter
    def scm_repo_url(self, scm_repo_url):
        """
        Sets the scm_repo_url of this BuildRecord.


        :param scm_repo_url: The scm_repo_url of this BuildRecord.
        :type: str
        """
        self._scm_repo_url = scm_repo_url

    @property
    def scm_revision(self):
        """
        Gets the scm_revision of this BuildRecord.


        :return: The scm_revision of this BuildRecord.
        :rtype: str
        """
        return self._scm_revision

    @scm_revision.setter
    def scm_revision(self, scm_revision):
        """
        Sets the scm_revision of this BuildRecord.


        :param scm_revision: The scm_revision of this BuildRecord.
        :type: str
        """
        self._scm_revision = scm_revision

    @property
    def build_log(self):
        """
        Gets the build_log of this BuildRecord.


        :return: The build_log of this BuildRecord.
        :rtype: str
        """
        return self._build_log

    @build_log.setter
    def build_log(self, build_log):
        """
        Sets the build_log of this BuildRecord.


        :param build_log: The build_log of this BuildRecord.
        :type: str
        """
        self._build_log = build_log

    @property
    def status(self):
        """
        Gets the status of this BuildRecord.


        :return: The status of this BuildRecord.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this BuildRecord.


        :param status: The status of this BuildRecord.
        :type: str
        """
        allowed_values = ["SUCCESS", "FAILED", "UNSTABLE", "BUILDING", "REJECTED", "CANCELLED", "SYSTEM_ERROR", "UNKNOWN", "NONE"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status`, must be one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def built_artifacts(self):
        """
        Gets the built_artifacts of this BuildRecord.


        :return: The built_artifacts of this BuildRecord.
        :rtype: list[Artifact]
        """
        return self._built_artifacts

    @built_artifacts.setter
    def built_artifacts(self, built_artifacts):
        """
        Sets the built_artifacts of this BuildRecord.


        :param built_artifacts: The built_artifacts of this BuildRecord.
        :type: list[Artifact]
        """
        self._built_artifacts = built_artifacts

    @property
    def dependencies(self):
        """
        Gets the dependencies of this BuildRecord.


        :return: The dependencies of this BuildRecord.
        :rtype: list[Artifact]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """
        Sets the dependencies of this BuildRecord.


        :param dependencies: The dependencies of this BuildRecord.
        :type: list[Artifact]
        """
        self._dependencies = dependencies

    @property
    def build_environment(self):
        """
        Gets the build_environment of this BuildRecord.


        :return: The build_environment of this BuildRecord.
        :rtype: BuildEnvironment
        """
        return self._build_environment

    @build_environment.setter
    def build_environment(self, build_environment):
        """
        Sets the build_environment of this BuildRecord.


        :param build_environment: The build_environment of this BuildRecord.
        :type: BuildEnvironment
        """
        self._build_environment = build_environment

    @property
    def product_milestone(self):
        """
        Gets the product_milestone of this BuildRecord.


        :return: The product_milestone of this BuildRecord.
        :rtype: ProductMilestone
        """
        return self._product_milestone

    @product_milestone.setter
    def product_milestone(self, product_milestone):
        """
        Sets the product_milestone of this BuildRecord.


        :param product_milestone: The product_milestone of this BuildRecord.
        :type: ProductMilestone
        """
        self._product_milestone = product_milestone

    @property
    def build_config_set_record(self):
        """
        Gets the build_config_set_record of this BuildRecord.


        :return: The build_config_set_record of this BuildRecord.
        :rtype: BuildConfigSetRecord
        """
        return self._build_config_set_record

    @build_config_set_record.setter
    def build_config_set_record(self, build_config_set_record):
        """
        Sets the build_config_set_record of this BuildRecord.


        :param build_config_set_record: The build_config_set_record of this BuildRecord.
        :type: BuildConfigSetRecord
        """
        self._build_config_set_record = build_config_set_record

    @property
    def attributes(self):
        """
        Gets the attributes of this BuildRecord.


        :return: The attributes of this BuildRecord.
        :rtype: dict(str, str)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """
        Sets the attributes of this BuildRecord.


        :param attributes: The attributes of this BuildRecord.
        :type: dict(str, str)
        """
        self._attributes = attributes

    @property
    def field_handler(self):
        """
        Gets the field_handler of this BuildRecord.


        :return: The field_handler of this BuildRecord.
        :rtype: FieldHandler
        """
        return self._field_handler

    @field_handler.setter
    def field_handler(self, field_handler):
        """
        Sets the field_handler of this BuildRecord.


        :param field_handler: The field_handler of this BuildRecord.
        :type: FieldHandler
        """
        self._field_handler = field_handler

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
	    elif isinstance(value, datetime):
		result[attr] = str(value.date())
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()
