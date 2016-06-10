# -*- coding: utf-8 -*-
###
# (C) Copyright (2012-2016) Hewlett Packard Enterprise Development LP
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
###

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()

__title__ = 'ethernet-networks'
__version__ = '0.0.1'
__copyright__ = '(C) Copyright (2012-2016) Hewlett Packard Enterprise ' \
                ' Development LP'
__license__ = 'MIT'
__status__ = 'Development'

from hpOneView.resources.resource import ResourceClient


class EthernetNetworks(object):
    URI = '/rest/ethernet-networks'

    def __init__(self, con):
        self._connection = con
        self._client = ResourceClient(con, self.URI)
        self.__default_values = {
            "ethernetNetworkType": "Tagged",
            "type": "ethernet-networkV3"
        }

    def get_all(self, start=0, count=-1, filter='', sort=''):
        """
        Gets a paginated collection of Ethernet networks. The collection is based on optional sorting and filtering,
        and constrained by start and count parameters.

        Args:
            start:
                The first item to return, using 0-based indexing.
                If not specified, the default is 0 - start with the first available item.
            count:
                The number of resources to return. A count of -1 requests all the items.
                The actual number of items in the response may differ from the requested
                count if the sum of start and count exceed the total number of items, or
                if returning the requested number of items would take too long.
            filter:
                A general filter/query string to narrow the list of items returned. The
                default is no filter - all resources are returned.
            sort:
                The sort order of the returned data set. By default, the sort order is based
                on create time, with the oldest entry first.

        Returns: dict

        """
        return self._client.get_all(start, count, filter=filter, sort=sort)

    def delete(self, resource, force=False, blocking=True):
        """
        Deletes an Ethernet network.
        Any deployed connections that are using the network are placed in the 'Failed' state.

        Args:
            resource: dict object to delete
            force:
                 If set to true the operation completes despite any problems with
                 network connectivity or errors on the resource itself. The default is false.
            blocking:
                Wait task completion

        Returns: task

        """
        return self._client.delete(resource, force=force, blocking=blocking)

    def get(self, id):
        """
        Gets the Ethernet network with the specified ID
        Args:
            id: ID of Ethernet network

        Returns: dict
        """
        return self._client.get(id)

    def create(self, resource, blocking=True):
        """
        Creates an Ethernet network.

        Args:
            resource: dict object to create
            blocking:
                Wait task completion. Default is True.

        Returns: Created resource. When blocking=False, returns the task.

        """
        data = self.__default_values.copy()
        data.update(resource)
        return self._client.create(data, blocking)

    def update(self, resource, blocking=True):
        """
        Updates an Ethernet network.

        Args:
            resource: dict object to update
            blocking:
                Wait task completion. Default is True.

        Returns: Updated resource. When blocking=False, returns the task.

        """
        data = self.__default_values.copy()
        data.update(resource)
        return self._client.update(data, blocking=blocking)

    def get_by(self, field, value):
        """
        Get all Ethernet networks that matches the filter
        The search is case insensitive

        Args:
            field: field name to filter
            value: value to filter

        Returns: dict

        """
        return self._client.get_by(field, value)

    def get_associated_profiles(self, id):
        """
        Gets the URIs of profiles which are using an Ethernet network.

        Args:
            id: The Ethernet id

        Returns: dict of URIs

        """
        uri = "/rest/ethernet-networks/%s/associatedProfiles" % (id)
        return self._client.get(uri)

    def get_associated_uplink_groups(self, id):
        """
        Gets the uplink sets which are using an Ethernet network.

        Args:
            id: The Ethernet id

        Returns: dict of URIs

        """
        uri = "/rest/ethernet-networks/%s/associatedUplinkGroups" % (id)
        return self._client.get(uri)
