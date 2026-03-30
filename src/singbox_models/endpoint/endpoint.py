from typing import Annotated, Literal

from pydantic import Field

from singbox_models.base import BaseModel, DialFields, PosixResolvedPath


class BaseEndpoint(DialFields):
    tag: str | None = None


class WireGuard(BaseEndpoint, DialFields):
    class Peer(BaseModel):
        address: str | None = None
        port: int | None = None
        public_key: str
        pre_shared_key: str | None = None
        allowed_ips: list[str]
        persistent_keepalive_interval: int | None = None
        reserved: list[int] | None = None

    type: Literal["wireguard"] = "wireguard"
    system: bool | None = None
    name: str | None = None
    mtu: int | None = None
    address: list[str]
    private_key: str
    listen_port: int | None = None
    peers: list[Peer]
    udp_timeout: str | None = None
    workers: int | None = None


class Tailscale(BaseEndpoint, DialFields):
    type: Literal["tailscale"] = "tailscale"
    state_directory: PosixResolvedPath | None = None
    auth_key: str | None = None
    control_url: str | None = None
    ephemeral: bool | None = None
    hostname: str | None = None
    accept_routes: bool | None = None
    exit_node: str | None = None
    exit_node_allow_lan_access: bool | None = None
    advertise_routes: list[str] | None = None
    advertise_exit_node: bool | None = None
    advertise_tags: list[str] | None = None
    relay_server_port: int | None = None
    relay_server_static_endpoints: list[str] | None = None
    system_interface: bool | None = None
    system_interface_name: str | None = None
    system_interface_mtu: int | None = None
    udp_timeout: str | None = None


Endpoint = Annotated[WireGuard | Tailscale, Field(discriminator="type")]
