# coding: utf-8

"""
    Snippets API

    Test description  # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@snippets.local
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from infodbclient.configuration import Configuration


class Resource(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'text': 'str',
        'human_description': 'str',
        'machine_description': 'str',
        'scheme': 'str',
        'host': 'str',
        'path': 'str',
        'supercollection': 'str',
        'collection': 'str',
        'subcollection': 'str',
        'is_source': 'bool',
        'edition': 'int'
    }

    attribute_map = {
        'id': 'id',
        'text': 'text',
        'human_description': 'human_description',
        'machine_description': 'machine_description',
        'scheme': 'scheme',
        'host': 'host',
        'path': 'path',
        'supercollection': 'supercollection',
        'collection': 'collection',
        'subcollection': 'subcollection',
        'is_source': 'is_source',
        'edition': 'edition'
    }

    def __init__(self, id=None, text=None, human_description=None, machine_description=None, scheme=None, host=None, path=None, supercollection=None, collection=None, subcollection=None, is_source=None, edition=None, _configuration=None):  # noqa: E501
        """Resource - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._text = None
        self._human_description = None
        self._machine_description = None
        self._scheme = None
        self._host = None
        self._path = None
        self._supercollection = None
        self._collection = None
        self._subcollection = None
        self._is_source = None
        self._edition = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.text = text
        if human_description is not None:
            self.human_description = human_description
        if machine_description is not None:
            self.machine_description = machine_description
        if scheme is not None:
            self.scheme = scheme
        if host is not None:
            self.host = host
        if path is not None:
            self.path = path
        if supercollection is not None:
            self.supercollection = supercollection
        if collection is not None:
            self.collection = collection
        if subcollection is not None:
            self.subcollection = subcollection
        if is_source is not None:
            self.is_source = is_source
        if edition is not None:
            self.edition = edition

    @property
    def id(self):
        """Gets the id of this Resource.  # noqa: E501


        :return: The id of this Resource.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Resource.


        :param id: The id of this Resource.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def text(self):
        """Gets the text of this Resource.  # noqa: E501


        :return: The text of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Resource.


        :param text: The text of this Resource.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                text is not None and len(text) < 1):
            raise ValueError("Invalid value for `text`, length must be greater than or equal to `1`")  # noqa: E501

        self._text = text

    @property
    def human_description(self):
        """Gets the human_description of this Resource.  # noqa: E501


        :return: The human_description of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._human_description

    @human_description.setter
    def human_description(self, human_description):
        """Sets the human_description of this Resource.


        :param human_description: The human_description of this Resource.  # noqa: E501
        :type: str
        """

        self._human_description = human_description

    @property
    def machine_description(self):
        """Gets the machine_description of this Resource.  # noqa: E501


        :return: The machine_description of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._machine_description

    @machine_description.setter
    def machine_description(self, machine_description):
        """Sets the machine_description of this Resource.


        :param machine_description: The machine_description of this Resource.  # noqa: E501
        :type: str
        """

        self._machine_description = machine_description

    @property
    def scheme(self):
        """Gets the scheme of this Resource.  # noqa: E501


        :return: The scheme of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """Sets the scheme of this Resource.


        :param scheme: The scheme of this Resource.  # noqa: E501
        :type: str
        """

        self._scheme = scheme

    @property
    def host(self):
        """Gets the host of this Resource.  # noqa: E501


        :return: The host of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this Resource.


        :param host: The host of this Resource.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def path(self):
        """Gets the path of this Resource.  # noqa: E501


        :return: The path of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Resource.


        :param path: The path of this Resource.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def supercollection(self):
        """Gets the supercollection of this Resource.  # noqa: E501


        :return: The supercollection of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._supercollection

    @supercollection.setter
    def supercollection(self, supercollection):
        """Sets the supercollection of this Resource.


        :param supercollection: The supercollection of this Resource.  # noqa: E501
        :type: str
        """

        self._supercollection = supercollection

    @property
    def collection(self):
        """Gets the collection of this Resource.  # noqa: E501


        :return: The collection of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._collection

    @collection.setter
    def collection(self, collection):
        """Sets the collection of this Resource.


        :param collection: The collection of this Resource.  # noqa: E501
        :type: str
        """

        self._collection = collection

    @property
    def subcollection(self):
        """Gets the subcollection of this Resource.  # noqa: E501


        :return: The subcollection of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._subcollection

    @subcollection.setter
    def subcollection(self, subcollection):
        """Sets the subcollection of this Resource.


        :param subcollection: The subcollection of this Resource.  # noqa: E501
        :type: str
        """

        self._subcollection = subcollection

    @property
    def is_source(self):
        """Gets the is_source of this Resource.  # noqa: E501


        :return: The is_source of this Resource.  # noqa: E501
        :rtype: bool
        """
        return self._is_source

    @is_source.setter
    def is_source(self, is_source):
        """Sets the is_source of this Resource.


        :param is_source: The is_source of this Resource.  # noqa: E501
        :type: bool
        """

        self._is_source = is_source

    @property
    def edition(self):
        """Gets the edition of this Resource.  # noqa: E501


        :return: The edition of this Resource.  # noqa: E501
        :rtype: int
        """
        return self._edition

    @edition.setter
    def edition(self, edition):
        """Sets the edition of this Resource.


        :param edition: The edition of this Resource.  # noqa: E501
        :type: int
        """

        self._edition = edition

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Resource, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Resource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Resource):
            return True

        return self.to_dict() != other.to_dict()
