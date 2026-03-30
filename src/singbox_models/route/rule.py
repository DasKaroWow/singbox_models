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


class DefaultRule(BaseModel):
    inbound: list[str] | None = None
    ip_version: Literal[4, 6] | None = None
    auth_user: list[str] | None = None
    protocol: list[str] | None = None
    client: list[str] | None = None
    network: list[Literal["tcp", "udp", "icmp"]] | None = None
    domain: list[str] | None = None
    domain_suffix: list[str] | None = None
    domain_keyword: list[str] | None = None
    domain_regex: list[str] | None = None
    geosite: list[str] | None = None
    source_geoip: list[str] | None = None
    geoip: list[str] | None = None
    source_ip_cidr: list[str] | None = None
    ip_is_private: bool | None = None
    ip_cidr: list[str] | None = None
    source_ip_is_private: bool | None = None
    source_port: list[int] | None = None
    source_port_range: list[str] | None = None
    port: list[int] | None = None
    port_range: list[str] | None = None
    process_name: list[str] | None = None
    process_path: list[str] | None = None
    process_path_regex: list[str] | None = None
    package_name: list[str] | None = None
    user: list[str] | None = None
    user_id: list[int] | None = None
    clash_mode: str | None = None
    network_type: list[Literal["wifi", "cellular", "ethernet", "other"]] | None = None
    network_is_expensive: bool | None = None
    network_is_constrained: bool | None = None
    interface_address: dict[str, list[str]] | None = None
    network_interface_address: dict[str, list[str]] | None = None
    default_interface_address: list[str] | None = None
    wifi_ssid: list[str] | None = None
    wifi_bssid: list[str] | None = None
    preferred_by: list[str] | None = None
    rule_set: list[str] | None = None
    rule_set_ipcidr_match_source: bool | None = None
    rule_set_ip_cidr_match_source: bool | None = None
    invert: bool | None = None
    action: Action | None = None
    outbound: str | None = None


class LogicalRule(BaseModel):
    type: Literal["logical"] = "logical"
    mode: Literal["and", "or"] | None = None
    rules: list[DefaultRule] | None = None
    invert: bool | None = None
    action: Action | None = None
    outbound: str | None = None


Rule = DefaultRule | LogicalRule
