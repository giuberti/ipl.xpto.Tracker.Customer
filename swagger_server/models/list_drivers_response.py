# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.get_driver_response import GetDriverResponse  # noqa: F401,E501
from swagger_server import util


class ListDriversResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, content: List[GetDriverResponse]=None, total_results: int=None):  # noqa: E501
        """ListDriversResponse - a model defined in Swagger

        :param content: The content of this ListDriversResponse.  # noqa: E501
        :type content: List[GetDriverResponse]
        :param total_results: The total_results of this ListDriversResponse.  # noqa: E501
        :type total_results: int
        """
        self.swagger_types = {
            'content': List[GetDriverResponse],
            'total_results': int
        }

        self.attribute_map = {
            'content': 'content',
            'total_results': 'totalResults'
        }
        self._content = content
        self._total_results = total_results

    @classmethod
    def from_dict(cls, dikt) -> 'ListDriversResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ListDriversResponse of this ListDriversResponse.  # noqa: E501
        :rtype: ListDriversResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def content(self) -> List[GetDriverResponse]:
        """Gets the content of this ListDriversResponse.

        list of paged items  # noqa: E501

        :return: The content of this ListDriversResponse.
        :rtype: List[GetDriverResponse]
        """
        return self._content

    @content.setter
    def content(self, content: List[GetDriverResponse]):
        """Sets the content of this ListDriversResponse.

        list of paged items  # noqa: E501

        :param content: The content of this ListDriversResponse.
        :type content: List[GetDriverResponse]
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def total_results(self) -> int:
        """Gets the total_results of this ListDriversResponse.

        total number of records  # noqa: E501

        :return: The total_results of this ListDriversResponse.
        :rtype: int
        """
        return self._total_results

    @total_results.setter
    def total_results(self, total_results: int):
        """Sets the total_results of this ListDriversResponse.

        total number of records  # noqa: E501

        :param total_results: The total_results of this ListDriversResponse.
        :type total_results: int
        """
        if total_results is None:
            raise ValueError("Invalid value for `total_results`, must not be `None`")  # noqa: E501

        self._total_results = total_results
