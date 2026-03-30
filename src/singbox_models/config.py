from singbox_models.base import BaseModel
from singbox_models.certificate import Certificate
from singbox_models.dns import DNS
from singbox_models.endpoint import Endpoint
from singbox_models.experimental import Experimental
from singbox_models.inbound import Inbound
from singbox_models.log import Log
from singbox_models.ntp import NTP
from singbox_models.outbound import Outbound
from singbox_models.route import Route
from singbox_models.service import Service


class Config(BaseModel):
    log: Log | None = None
    dns: DNS | None = None
    ntp: NTP | None = None
    certificate: Certificate | None = None
    endpoints: list[Endpoint] | None = None
    inbounds: list[Inbound]
    outbounds: list[Outbound]
    route: Route | None = None
    services: list[Service] | None = None
    experimental: Experimental | None = None
