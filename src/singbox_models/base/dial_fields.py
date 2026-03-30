from typing import Literal

from .base import BaseModel


class DomainResolver(BaseModel):
    server: str
    strategy: Literal["prefer_ipv4", "prefer_ipv6", "ipv4_only", "ipv6_only"]
    disable_cache: bool | None = None
    rewrite_ttl: None = None
    client_subnet: None = None


class DialFields(BaseModel):
    detour: str | None = None
    inet4_bind_address: str | None = None
    inet6_bind_address: str | None = None
    bind_address_no_port: bool | None = None
    routing_mark: int | None = None
    reuse_addr: bool | None = None
    netns: str | None = None
    connect_timeout: str | None = None
    tcp_fast_open: bool | None = None
    tcp_multi_path: bool | None = None
    disable_tcp_keep_alive: bool | None = None
    tcp_keep_alive: str | None = None
    tcp_keep_alive_interval: str | None = None
    udp_fragment: bool | None = None

    domain_resolver: str | DomainResolver | None = None
    network_strategy: Literal["default", "hybrid", "fallback"] | None = None
    network_type: Literal["wifi", "cellular", "ethernet", "other"] | None = None
    fallback_network_type: Literal["wifi", "cellular", "ethernet"] | None = None
    fallback_delay: str | None = None
