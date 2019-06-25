# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from facebookads.adobjects.abstractobject import AbstractObject
from facebookads.adobjects.abstractcrudobject import AbstractCrudObject
from facebookads.adobjects.objectparser import ObjectParser
from facebookads.api import FacebookRequest
from facebookads.typechecker import TypeChecker

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class EventSourceGroup(
  AbstractCrudObject,
):

  def __init__(self, fbid=None, parent_id=None, api=None):
    self._isEventSourceGroup = True
    super(EventSourceGroup, self).__init__(fbid, parent_id, api)

  class Field(AbstractObject.Field):
    business = 'business'
    event_sources = 'event_sources'
    id = 'id'
    name = 'name'

  # @deprecated get_endpoint function is deprecated
  @classmethod
  def get_endpoint(cls):
    return 'event_source_groups'

  def api_create(self, parent_id, fields=None, params=None, batch=None, pending=False):
    from facebookads.adobjects.business import Business
    return Business(api=self._api, fbid=parent_id).create_event_source_group(fields, params, batch, pending)

  def api_get(self, fields=None, params=None, batch=None, pending=False):
    param_types = {
    }
    enums = {
    }
    request = FacebookRequest(
      node_id=self['id'],
      method='GET',
      endpoint='/',
      api=self._api,
      param_checker=TypeChecker(param_types, enums),
      target_class=EventSourceGroup,
      api_type='NODE',
      response_parser=ObjectParser(reuse_object=self),
    )
    request.add_params(params)
    request.add_fields(fields)

    if batch is not None:
      request.add_to_batch(batch)
      return request
    elif pending:
      return request
    else:
      self.assure_call()
      return request.execute()

  def api_update(self, fields=None, params=None, batch=None, pending=False):
    param_types = {
      'event_sources': 'list<string>',
      'name': 'string',
    }
    enums = {
    }
    request = FacebookRequest(
      node_id=self['id'],
      method='POST',
      endpoint='/',
      api=self._api,
      param_checker=TypeChecker(param_types, enums),
      target_class=EventSourceGroup,
      api_type='NODE',
      response_parser=ObjectParser(reuse_object=self),
    )
    request.add_params(params)
    request.add_fields(fields)

    if batch is not None:
      request.add_to_batch(batch)
      return request
    elif pending:
      return request
    else:
      self.assure_call()
      return request.execute()

  def create_shared_account(self, fields=None, params=None, batch=None, pending=False):
    param_types = {
      'accounts': 'list<string>',
    }
    enums = {
    }
    request = FacebookRequest(
      node_id=self['id'],
      method='POST',
      endpoint='/shared_accounts',
      api=self._api,
      param_checker=TypeChecker(param_types, enums),
      target_class=EventSourceGroup,
      api_type='EDGE',
      response_parser=ObjectParser(target_class=EventSourceGroup, api=self._api),
    )
    request.add_params(params)
    request.add_fields(fields)

    if batch is not None:
      request.add_to_batch(batch)
      return request
    elif pending:
      return request
    else:
      self.assure_call()
      return request.execute()

  _field_types = {
    'business': 'Business',
    'event_sources': 'list<ExternalEventSource>',
    'id': 'string',
    'name': 'string',
  }

  @classmethod
  def _get_field_enum_info(cls):
    field_enum_info = {}
    return field_enum_info
