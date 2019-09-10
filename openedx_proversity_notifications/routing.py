from channels.routing import route_class
from openedx_proversity_notifications.consumers import OpenEdxSubmitionsDemultiplexer

channel_routing = [
    route_class(OpenEdxSubmitionsDemultiplexer, path="^/submitions/"),
]
