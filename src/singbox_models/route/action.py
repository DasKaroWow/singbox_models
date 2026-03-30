from typing import Annotated, Literal

from pydantic import Field

from singbox_models.base import BaseModel


class RouteOptions(BaseModel):
    override_address: str | None = None
    override_port: int | None = None
    network_strategy: Literal["default", "hybrid", "fallback"] | None = None
    network_type: list[Literal["wifi", "cellular", "ethernet", "other"]] | None = None
    fallback_network_type: list[Literal["wifi", "cellular", "ethernet"]] | None = None
    fallback_delay: str | None = None
    udp_disable_domain_unmapping: bool | None = None
    udp_connect: bool | None = None
    udp_timeout: str | None = None
    tls_fragment: bool | None = None
    tls_fragment_fallback_delay: str | None = None
    tls_record_fragment: bool | None = None


class RouteAction(RouteOptions):
    action: Literal["route"] = "route"
    outbound: str


class BypassAction(RouteOptions):
    action: Literal["bypass"] = "bypass"
    outbound: str | None = None


class RejectAction(BaseModel):
    action: Literal["reject"] = "reject"
    method: Literal["default", "drop", "reply"] | None = None
    no_drop: bool | None = None


class HijackDNSAction(BaseModel):
    action: Literal["hijack-dns"] = "hijack-dns"


class RouteOptionsAction(RouteOptions):
    action: Literal["route-options"] = "route-options"


class SniffAction(BaseModel):
    action: Literal["sniff"] = "sniff"
    sniffer: list[str] | None = None
    timeout: str | None = None


class ResolveAction(BaseModel):
    action: Literal["resolve"] = "resolve"
    server: str | None = None
    strategy: Literal["prefer_ipv4", "prefer_ipv6", "ipv4_only", "ipv6_only"] | None = None
    disable_cache: bool | None = None
    rewrite_ttl: None = None
    client_subnet: str | None = None


Action = Annotated[
    RouteAction | BypassAction | RejectAction | HijackDNSAction | RouteOptionsAction | SniffAction | ResolveAction,
    Field(discriminator="action"),
]
