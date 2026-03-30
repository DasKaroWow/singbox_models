from typing import Annotated, Any, Literal

from pydantic import Field

from singbox_models.base import BaseModel, DialFields, PosixResolvedPath, Transport, UDPOverTCP
from singbox_models.base.multiplex import MultiplexOutbound
from singbox_models.base.tls import TLSOutbound


class BaseOutbound(DialFields):
    tag: str | None = None


class Direct(BaseOutbound):
    type: Literal["direct"] = "direct"
    override_address: str | None = None
    override_port: int | None = None


class Block(BaseModel):
    type: Literal["block"] = "block"
    tag: str | None = None


class Socks(BaseOutbound):
    type: Literal["socks"] = "socks"
    server: str
    server_port: int
    version: Literal["4", "4a", "5"] | None = None
    username: str | None = None
    password: str | None = None
    network: Literal["tcp", "udp"] | None = None
    udp_over_tcp: bool | UDPOverTCP | None = None


class HTTP(BaseOutbound):
    type: Literal["http"] = "http"
    server: str
    server_port: int
    username: str | None = None
    password: str | None = None
    path: str | None = None
    headers: dict[str, Any] | None = None
    tls: TLSOutbound | None = None


class Shadowsocks(BaseOutbound):
    type: Literal["shadowsocks"] = "shadowsocks"
    server: str
    server_port: int
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
        "aes-128-ctr",
        "aes-192-ctr",
        "aes-256-ctr",
        "aes-128-cfb",
        "aes-192-cfb",
        "aes-256-cfb",
        "rc4-md5",
        "chacha20-ietf",
        "xchacha20",
    ]
    password: str
    plugin: Literal["obfs-local", "v2ray-plugin"] | None = None
    plugin_opts: str | None = None
    network: Literal["tcp", "udp"] | None = None
    udp_over_tcp: bool | UDPOverTCP | None = None
    multiplex: MultiplexOutbound | None = None


class VMess(BaseOutbound):
    type: Literal["vmess"] = "vmess"
    server: str
    server_port: int
    uuid: str
    security: (
        Literal[
            "auto",
            "none",
            "zero",
            "aes-128-gcm",
            "chacha20-poly1305",
            "aes-128-ctr",
        ]
        | None
    ) = None
    alter_id: int | None = None
    global_padding: bool | None = None
    authenticated_length: bool | None = None
    network: Literal["tcp", "udp"] | None = None
    tls: TLSOutbound | None = None
    packet_encoding: Literal["", "packetaddr", "xudp"] | None = None
    multiplex: MultiplexOutbound | None = None
    transport: Transport | None = None


class Trojan(BaseOutbound):
    type: Literal["trojan"] = "trojan"
    server: str
    server_port: int
    password: str
    network: Literal["tcp", "udp"] | None = None
    tls: TLSOutbound | None = None
    multiplex: MultiplexOutbound | None = None
    transport: Transport | None = None


class WireGuard(BaseOutbound):
    class Peer(BaseModel):
        server: str | None = None
        server_port: int | None = None
        public_key: str
        pre_shared_key: str | None = None
        allowed_ips: list[str] | None = None
        reserved: list[int] | None = None

    type: Literal["wireguard"] = "wireguard"
    server: str | None = None
    server_port: int | None = None
    system_interface: bool | None = None
    interface_name: str | None = None
    gso: bool | None = None
    local_address: list[str]
    private_key: str
    peers: list[Peer] | None = None
    peer_public_key: str | None = None
    pre_shared_key: str | None = None
    reserved: list[int] | None = None
    workers: int | None = None
    mtu: int | None = None
    network: Literal["tcp", "udp"] | None = None


class Hysteria(BaseOutbound):
    type: Literal["hysteria"] = "hysteria"
    server: str
    server_port: int
    server_ports: list[str] | None = None
    hop_interval: str | None = None
    up: str
    up_mbps: int
    down: str
    down_mbps: int
    obfs: str | None = None
    auth: str | None = None
    auth_str: str | None = None
    recv_window_conn: int | None = None
    recv_window: int | None = None
    disable_mtu_discovery: bool | None = None
    network: Literal["tcp", "udp"] | None = None
    tls: TLSOutbound


class ShadowTLS(BaseOutbound):
    type: Literal["shadowtls"] = "shadowtls"
    server: str
    server_port: int
    version: Literal[1, 2, 3] | None = None
    password: str | None = None
    tls: TLSOutbound


class VLESS(BaseOutbound):
    type: Literal["vless"] = "vless"
    server: str
    server_port: int
    uuid: str
    flow: Literal["xtls-rprx-vision"] | None = None
    network: Literal["tcp", "udp"] | None = None
    tls: TLSOutbound | None = None
    packet_encoding: Literal["", "packetaddr", "xudp"] | None = None
    multiplex: MultiplexOutbound | None = None
    transport: Transport | None = None


class TUIC(BaseOutbound):
    type: Literal["tuic"] = "tuic"
    server: str
    server_port: int
    uuid: str
    password: str | None = None
    congestion_control: Literal["cubic", "new_reno", "bbr"] | None = None
    udp_relay_mode: Literal["native", "quic"] | None = None
    udp_over_stream: bool | None = None
    zero_rtt_handshake: bool | None = None
    heartbeat: str | None = None
    network: Literal["tcp", "udp"] | None = None
    tls: TLSOutbound


class Hysteria2(BaseOutbound):
    class Obfs(BaseModel):
        type: Literal["salamander"] | None = None
        password: str | None = None

    type: Literal["hysteria2"] = "hysteria2"
    server: str
    server_port: int
    server_ports: list[str] | None = None
    hop_interval: str | None = None
    up_mbps: int | None = None
    down_mbps: int | None = None
    obfs: Obfs | None = None
    password: str | None = None
    network: Literal["tcp", "udp"] | None = None
    tls: TLSOutbound
    brutal_debug: bool | None = None


class AnyTLS(BaseOutbound):
    type: Literal["anytls"] = "anytls"
    server: str
    server_port: int
    password: str
    idle_session_check_interval: str | None = None
    idle_session_timeout: str | None = None
    min_idle_session: int | None = None
    tls: TLSOutbound


class Tor(BaseOutbound):
    type: Literal["tor"] = "tor"
    executable_path: PosixResolvedPath | None = None
    extra_args: list[str] | None = None
    data_directory: PosixResolvedPath | None = None
    torrc: dict[str, Any] | None = None


class SSH(BaseOutbound):
    type: Literal["ssh"] = "ssh"
    server: str
    server_port: int | None = None
    user: str | None = None
    password: str | None = None
    private_key: str | None = None
    private_key_path: PosixResolvedPath | None = None
    private_key_passphrase: str | None = None
    host_key: list[str] | None = None
    host_key_algorithms: list[str] | None = None
    client_version: str | None = None


class DNS(BaseModel):
    type: Literal["dns"] = "dns"
    tag: str | None = None


class Selector(BaseModel):
    type: Literal["selector"] = "selector"
    tag: str | None = None
    outbounds: list[str]
    default: str | None = None
    interrupt_exist_connections: bool | None = None


class URLTest(BaseModel):
    type: Literal["urltest"] = "urltest"
    tag: str | None = None
    outbounds: list[str]
    url: str | None = None
    interval: str | None = None
    tolerance: int | None = None
    idle_timeout: str | None = None
    interrupt_exist_connections: bool | None = None


class Naive(BaseOutbound):
    type: Literal["naive"] = "naive"
    server: str
    server_port: int
    username: str | None = None
    password: str | None = None
    insecure_concurrency: int | None = None
    extra_headers: dict[str, Any] | None = None
    udp_over_tcp: bool | UDPOverTCP | None = None
    quic: bool | None = None
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
    tls: TLSOutbound


Outbound = Annotated[
    Direct
    | Block
    | Socks
    | HTTP
    | Shadowsocks
    | VMess
    | Trojan
    | WireGuard
    | Hysteria
    | ShadowTLS
    | VLESS
    | TUIC
    | Hysteria2
    | AnyTLS
    | Tor
    | SSH
    | DNS
    | Selector
    | URLTest
    | Naive,
    Field(discriminator="type"),
]
