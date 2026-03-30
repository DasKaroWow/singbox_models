from typing import Annotated, Literal

from pydantic import Field

from singbox_models.base import BaseModel


class RouteAction(BaseModel):
    action: Literal["route"] = "route"
    server: str
    strategy: Literal["prefer_ipv4", "prefer_ipv6", "ipv4_only", "ipv6_only"] | None = None
    disable_cache: bool | None = None
    rewrite_ttl: None = None
    client_subnet: None = None


class RouteOptionsAction(BaseModel):
    action: Literal["route-options"] = "route-options"
    disable_cache: bool | None = None
    rewrite_ttl: None = None
    client_subnet: None = None


class RejectAction(BaseModel):
    action: Literal["reject"] = "reject"
    method: Literal["default", "drop"] | None = None
    no_drop: bool | None = None


class PredefinedAction(BaseModel):
    action: Literal["predefined"] = "predefined"
    rcode: Literal["NOERROR", "FORMERR", "SERVFAIL", "NXDOMAIN", "NOTIMP", "REFUSED"] | None = None
    answer: list[str] | None = None
    ns: list[str] | None = None
    extra: list[str] | None = None


Action = Annotated[RouteAction | RouteOptionsAction | RejectAction | PredefinedAction, Field(discriminator="action")]


class DefaultRule(BaseModel):
    inbound: list[str] | None = None
    ip_version: Literal[4, 6] | None = None
    query_type: list[int | str] | None = None
    network: Literal["tcp", "udp"] | None = None
    auth_user: list[str] | None = None
    protocol: list[str] | None = None
    domain: list[str] | None = None
    domain_suffix: list[str] | None = None
    domain_keyword: list[str] | None = None
    domain_regex: list[str] | None = None
    source_ip_cidr: list[str] | None = None
    source_ip_is_private: bool | None = None
    ip_cidr: list[str] | None = None
    ip_is_private: bool | None = None
    ip_accept_any: bool | None = None
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
    rule_set: list[str] | None = None
    rule_set_ip_cidr_match_source: bool | None = None
    rule_set_ip_cidr_accept_empty: bool | None = None
    invert: bool | None = None
    action: Action


class LogicalRule(BaseModel):
    type: Literal["logical"] = "logical"
    mode: Literal["and", "or"] | None = None
    rules: list[DefaultRule] | None = None
    action: Action


Rule = LogicalRule | DefaultRule
