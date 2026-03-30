from typing import Annotated, Any, Literal

from pydantic import Field

from singbox_models.base import BaseModel, DialFields, ListenFields, Transport
from singbox_models.base.multiplex import MultiplexInbound
from singbox_models.base.tls import TLSInbound


# Inbounds
class BaseInbound(ListenFields):
    tag: str | None = None


class Direct(BaseInbound):
    type: Literal["direct"] = "direct"
    network: Literal["tcp", "udp"] | None = None
    override_address: str | None = None
    override_port: int | None = None


class Mixed(BaseInbound):
    class User(BaseModel):
        username: str
        password: str

    type: Literal["mixed"] = "mixed"
    users: list[User] | None = None
    set_system_proxy: bool | None = None


class Socks(BaseInbound):
    class User(BaseModel):
        username: str
        password: str

    type: Literal["socks"] = "socks"
    users: list[User] | None = None


class HTTP(BaseInbound):
    class User(BaseModel):
        username: str
        password: str

    type: Literal["http"] = "http"
    users: list[User] | None = None
    tls: TLSInbound | None = None
    set_system_proxy: bool | None = None


class Shadowsocks(BaseInbound):
    class User(BaseModel):
        name: str
        password: str

    class Destination(BaseModel):
        name: str
        server: str
        server_port: int
        password: str

    type: Literal["shadowsocks"] = "shadowsocks"
    network: Literal["tcp", "udp"] | None = None
    method: Literal[
        "2022-blake3-aes-128-gcm",
        "2022-blake3-aes-256-gcm",
        "2022-blake3-chacha20-poly1305",
        "none",
        "aes-128-gcm",
        "aes-192-gcm",
        "aes-256-gcm",
        "chacha20-ietf-poly1305",
        "xchacha20-ietf-poly1305",
    ]
    password: str
    users: list[User] | None = None
    destinations: list[Destination] | None = None
    managed: bool | None = None
    multiplex: MultiplexInbound | None = None


class VMess(BaseInbound):
    class User(BaseModel):
        name: str
        uuid: str
        alterId: int  # noqa: N815

    type: Literal["vmess"] = "vmess"
    users: list[User]
    tls: TLSInbound | None = None
    multiplex: MultiplexInbound | None = None
    transport: Transport | None = None


class Trojan(BaseInbound):
    class User(BaseModel):
        name: str
        password: str

    class Fallback(BaseModel):
        server: str
        server_port: int

    type: Literal["trojan"] = "trojan"
    users: list[User]
    tls: TLSInbound | None = None
    fallback: Fallback | None = None
    fallback_for_alpn: dict[str, Fallback] | None = None
    multiplex: MultiplexInbound | None = None
    transport: Transport | None = None


class Naive(BaseInbound):
    class User(BaseModel):
        username: str
        password: str

    type: Literal["naive"] = "naive"
    network: Literal["tcp", "udp"] | None = None
    users: list[User]
    quic_congestion_control: (
        Literal[
            "bbr",
            "bbr_standard",
            "bbr2",
            "bbr2_variant",
            "cubic",
            "reno",
        ]
        | None
    ) = None
    tls: TLSInbound | None = None


class Hysteria(BaseInbound):
    class User(BaseModel):
        name: str | None = None
        auth: str | None = None
        auth_str: str | None = None

    type: Literal["hysteria"] = "hysteria"
    up: str
    up_mbps: int
    down: str
    down_mbps: int
    obfs: str | None = None
    users: list[User] | None = None
    recv_window_conn: int | None = None
    recv_window_client: int | None = None
    max_conn_client: int | None = None
    disable_mtu_discovery: bool | None = None
    tls: TLSInbound


class ShadowTLS(BaseInbound):
    class User(BaseModel):
        name: str | None = None
        password: str | None = None

    class Handshake(DialFields):
        server: str | None = None
        server_port: int | None = None

    type: Literal["shadowtls"] = "shadowtls"
    version: Literal[1, 2, 3] | None = None
    password: str | None = None
    users: list[User] | None = None
    handshake: Handshake
    handshake_for_server_name: dict[str, Handshake] | None = None
    strict_mode: bool | None = None
    wildcard_sni: Literal["off", "authed", "all"] | None = None


class TUIC(BaseInbound):
    class User(BaseModel):
        name: str | None = None
        uuid: str
        password: str | None = None

    type: Literal["tuic"] = "tuic"
    users: list[User]
    congestion_control: Literal["cubic", "new_reno", "bbr"] | None = None
    auth_timeout: str | None = None
    zero_rtt_handshake: bool | None = None
    heartbeat: str | None = None
    tls: TLSInbound


class Hysteria2(BaseInbound):
    class Obfs(BaseModel):
        type: Literal["salamander"] | None = None
        password: str | None = None

    class User(BaseModel):
        name: str | None = None
        password: str | None = None

    class MasqueradeFile(BaseModel):
        type: Literal["file"] = "file"
        directory: str | None = None

    class MasqueradeProxy(BaseModel):
        type: Literal["proxy"] = "proxy"
        url: str | None = None
        rewrite_host: bool | None = None

    class MasqueradeString(BaseModel):
        type: Literal["string"] = "string"
        status_code: int | None = None
        headers: dict[str, Any] | None = None
        content: str | None = None

    type: Literal["hysteria2"] = "hysteria2"
    up_mbps: int | None = None
    down_mbps: int | None = None
    obfs: Obfs | None = None
    users: list[User] | None = None
    ignore_client_bandwidth: bool | None = None
    tls: TLSInbound
    masquerade: str | MasqueradeFile | MasqueradeProxy | MasqueradeString | None = None
    brutal_debug: bool | None = None


class VLESS(BaseInbound):
    class User(BaseModel):
        name: str | None = None
        uuid: str
        flow: Literal["xtls-rprx-vision"] | None = None

    type: Literal["vless"] = "vless"
    users: list[User]
    tls: TLSInbound | None = None
    multiplex: MultiplexInbound | None = None
    transport: Transport | None = None


class AnyTLS(BaseInbound):
    class User(BaseModel):
        name: str | None = None
        password: str | None = None

    type: Literal["anytls"] = "anytls"
    users: list[User]
    padding_scheme: list[str] | None = None
    tls: TLSInbound | None = None


class Tun(BaseModel):
    class Platform(BaseModel):
        class HTTPProxy(BaseModel):
            enabled: bool | None = None
            server: str
            server_port: int
            bypass_domain: list[str] | None = None
            match_domain: list[str] | None = None

        http_proxy: HTTPProxy | None = None

    type: Literal["tun"] = "tun"
    tag: str | None = None
    interface_name: str | None = None
    address: list[str] | None = None
    inet4_address: list[str] | None = None
    inet6_address: list[str] | None = None
    mtu: int | None = None
    gso: bool | None = None
    auto_route: bool | None = None
    iproute2_table_index: int | None = None
    iproute2_rule_index: int | None = None
    auto_redirect: bool | None = None
    auto_redirect_input_mark: int | str | None = None
    auto_redirect_output_mark: int | str | None = None
    auto_redirect_reset_mark: int | str | None = None
    auto_redirect_nfqueue: int | None = None
    auto_redirect_iproute2_fallback_rule_index: int | None = None
    exclude_mptcp: bool | None = None
    loopback_address: list[str] | None = None
    strict_route: bool | None = None
    route_address: list[str] | None = None
    inet4_route_address: list[str] | None = None
    inet6_route_address: list[str] | None = None
    route_exclude_address: list[str] | None = None
    inet4_route_exclude_address: list[str] | None = None
    inet6_route_exclude_address: list[str] | None = None
    route_address_set: list[str] | None = None
    route_exclude_address_set: list[str] | None = None
    endpoint_independent_nat: bool | None = None
    udp_timeout: str | None = None
    stack: Literal["system", "gvisor", "mixed"] | None = None
    include_interface: list[str] | None = None
    exclude_interface: list[str] | None = None
    include_uid: list[int] | None = None
    include_uid_range: list[str] | None = None
    exclude_uid: list[int] | None = None
    exclude_uid_range: list[str] | None = None
    include_android_user: list[int] | None = None
    include_package: list[str] | None = None
    exclude_package: list[str] | None = None
    platform: Platform | None = None


class Redirect(BaseInbound):
    type: Literal["redirect"] = "redirect"


class TProxy(BaseInbound):
    type: Literal["tproxy"] = "tproxy"
    network: Literal["tcp", "udp"] | None = None


Inbound = Annotated[
    Direct
    | Mixed
    | Socks
    | HTTP
    | Shadowsocks
    | VMess
    | Trojan
    | Naive
    | Hysteria
    | ShadowTLS
    | VLESS
    | TUIC
    | Hysteria2
    | AnyTLS
    | Tun
    | Redirect
    | TProxy,
    Field(discriminator="type"),
]
