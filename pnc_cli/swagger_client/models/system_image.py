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


class SystemImage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SystemImage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'environment': 'Environment',
            'name': 'str',
            'description': 'str',
            'image_url': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'environment': 'environment',
            'name': 'name',
            'description': 'description',
            'image_url': 'imageUrl'
        }

        self._id = None
        self._environment = None
        self._name = None
        self._description = None
        self._image_url = None

    @property
    def id(self):
        """
        Gets the id of this SystemImage.


        :return: The id of this SystemImage.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SystemImage.


        :param id: The id of this SystemImage.
        :type: int
        """
        self._id = id

    @property
    def environment(self):
        """
        Gets the environment of this SystemImage.


        :return: The environment of this SystemImage.
        :rtype: Environment
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """
        Sets the environment of this SystemImage.


        :param environment: The environment of this SystemImage.
        :type: Environment
        """
        self._environment = environment

    @property
    def name(self):
        """
        Gets the name of this SystemImage.


        :return: The name of this SystemImage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SystemImage.


        :param name: The name of this SystemImage.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this SystemImage.


        :return: The description of this SystemImage.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SystemImage.


        :param description: The description of this SystemImage.
        :type: str
        """
        self._description = description

    @property
    def image_url(self):
        """
        Gets the image_url of this SystemImage.


        :return: The image_url of this SystemImage.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """
        Sets the image_url of this SystemImage.


        :param image_url: The image_url of this SystemImage.
        :type: str
        """
        self._image_url = image_url

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
		result[attr] = str(value)
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
