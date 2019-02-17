# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class CallSummaryList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the CallSummaryList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.insights.v1.summary.CallSummaryList
        :rtype: twilio.rest.insights.v1.summary.CallSummaryList
        """
        super(CallSummaryList, self).__init__(version)

        # Path Solution
        self._solution = {}

    def get(self, call_sid):
        """
        Constructs a CallSummaryContext

        :param call_sid: The call_sid

        :returns: twilio.rest.insights.v1.summary.CallSummaryContext
        :rtype: twilio.rest.insights.v1.summary.CallSummaryContext
        """
        return CallSummaryContext(self._version, call_sid=call_sid, )

    def __call__(self, call_sid):
        """
        Constructs a CallSummaryContext

        :param call_sid: The call_sid

        :returns: twilio.rest.insights.v1.summary.CallSummaryContext
        :rtype: twilio.rest.insights.v1.summary.CallSummaryContext
        """
        return CallSummaryContext(self._version, call_sid=call_sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Insights.V1.CallSummaryList>'


class CallSummaryPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the CallSummaryPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.insights.v1.summary.CallSummaryPage
        :rtype: twilio.rest.insights.v1.summary.CallSummaryPage
        """
        super(CallSummaryPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CallSummaryInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.insights.v1.summary.CallSummaryInstance
        :rtype: twilio.rest.insights.v1.summary.CallSummaryInstance
        """
        return CallSummaryInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Insights.V1.CallSummaryPage>'


class CallSummaryContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, call_sid):
        """
        Initialize the CallSummaryContext

        :param Version version: Version that contains the resource
        :param call_sid: The call_sid

        :returns: twilio.rest.insights.v1.summary.CallSummaryContext
        :rtype: twilio.rest.insights.v1.summary.CallSummaryContext
        """
        super(CallSummaryContext, self).__init__(version)

        # Path Solution
        self._solution = {'call_sid': call_sid, }
        self._uri = '/Voice/{call_sid}/Summary'.format(**self._solution)

    def fetch(self):
        """
        Fetch a CallSummaryInstance

        :returns: Fetched CallSummaryInstance
        :rtype: twilio.rest.insights.v1.summary.CallSummaryInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return CallSummaryInstance(self._version, payload, call_sid=self._solution['call_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Insights.V1.CallSummaryContext {}>'.format(context)


class CallSummaryInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    class CallType(object):
        CARRIER = "carrier"
        SIP = "sip"
        TRUNKING = "trunking"
        CLIENT = "client"

    class CallState(object):
        RINGING = "ringing"
        COMPLETED = "completed"
        BUSY = "busy"
        FAIL = "fail"
        NOANSWER = "noanswer"
        CANCELED = "canceled"
        ANSWERED = "answered"
        UNDIALED = "undialed"

    class ProcessingState(object):
        COMPLETE = "complete"
        PARTIAL = "partial"

    class Direction(object):
        INBOUND = "inbound"
        OUTBOUND_API = "outbound_api"
        OUTBOUND_DIAL = "outbound_dial"
        TRUNKING_ORIGINATING = "trunking_originating"
        TRUNKING_TERMINATING = "trunking_terminating"

    class DisconnectedBy(object):
        CALLEE = "callee"
        CALLER = "caller"
        UNKNOWN = "unknown"

    def __init__(self, version, payload, call_sid=None):
        """
        Initialize the CallSummaryInstance

        :returns: twilio.rest.insights.v1.summary.CallSummaryInstance
        :rtype: twilio.rest.insights.v1.summary.CallSummaryInstance
        """
        super(CallSummaryInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'call_sid': payload['call_sid'],
            'call_type': payload['call_type'],
            'call_state': payload['call_state'],
            'processing_state': payload['processing_state'],
            'direction': payload['direction'],
            'disconnected_by': payload['disconnected_by'],
            'start_time': deserialize.iso8601_datetime(payload['start_time']),
            'end_time': deserialize.iso8601_datetime(payload['end_time']),
            'duration': deserialize.integer(payload['duration']),
            'connect_duration': deserialize.integer(payload['connect_duration']),
            'from_': payload['from'],
            'to': payload['to'],
            'carrier_edge': payload['carrier_edge'],
            'client_edge': payload['client_edge'],
            'sip_edge': payload['sip_edge'],
            'tags': payload['tags'],
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {'call_sid': call_sid or self._properties['call_sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: CallSummaryContext for this CallSummaryInstance
        :rtype: twilio.rest.insights.v1.summary.CallSummaryContext
        """
        if self._context is None:
            self._context = CallSummaryContext(self._version, call_sid=self._solution['call_sid'], )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def call_sid(self):
        """
        :returns: The call_sid
        :rtype: unicode
        """
        return self._properties['call_sid']

    @property
    def call_type(self):
        """
        :returns: The call_type
        :rtype: CallSummaryInstance.CallType
        """
        return self._properties['call_type']

    @property
    def call_state(self):
        """
        :returns: The call_state
        :rtype: CallSummaryInstance.CallState
        """
        return self._properties['call_state']

    @property
    def processing_state(self):
        """
        :returns: The processing_state
        :rtype: CallSummaryInstance.ProcessingState
        """
        return self._properties['processing_state']

    @property
    def direction(self):
        """
        :returns: The direction
        :rtype: CallSummaryInstance.Direction
        """
        return self._properties['direction']

    @property
    def disconnected_by(self):
        """
        :returns: The disconnected_by
        :rtype: CallSummaryInstance.DisconnectedBy
        """
        return self._properties['disconnected_by']

    @property
    def start_time(self):
        """
        :returns: The start_time
        :rtype: datetime
        """
        return self._properties['start_time']

    @property
    def end_time(self):
        """
        :returns: The end_time
        :rtype: datetime
        """
        return self._properties['end_time']

    @property
    def duration(self):
        """
        :returns: The duration
        :rtype: unicode
        """
        return self._properties['duration']

    @property
    def connect_duration(self):
        """
        :returns: The connect_duration
        :rtype: unicode
        """
        return self._properties['connect_duration']

    @property
    def from_(self):
        """
        :returns: The from
        :rtype: dict
        """
        return self._properties['from_']

    @property
    def to(self):
        """
        :returns: The to
        :rtype: dict
        """
        return self._properties['to']

    @property
    def carrier_edge(self):
        """
        :returns: The carrier_edge
        :rtype: dict
        """
        return self._properties['carrier_edge']

    @property
    def client_edge(self):
        """
        :returns: The client_edge
        :rtype: dict
        """
        return self._properties['client_edge']

    @property
    def sip_edge(self):
        """
        :returns: The sip_edge
        :rtype: dict
        """
        return self._properties['sip_edge']

    @property
    def tags(self):
        """
        :returns: The tags
        :rtype: unicode
        """
        return self._properties['tags']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a CallSummaryInstance

        :returns: Fetched CallSummaryInstance
        :rtype: twilio.rest.insights.v1.summary.CallSummaryInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Insights.V1.CallSummaryInstance {}>'.format(context)
