from typing import Annotated, Any, Literal

from pydantic import Field

from singbox_models.base import TLS, BaseModel, DialFields, PosixResolvedPath


class BaseServer(BaseModel):
    tag: str | None = None


class Local(BaseServer, DialFields):
    type: Literal["local"] = "local"
    prefer_go: bool | None = None


class Hosts(BaseServer):
    type: Literal["hosts"] = "hosts"
    path: list[PosixResolvedPath] | None = None
    predefined: dict[str, list[str] | str]


class TCP(BaseServer, DialFields):
    type: Literal["tcp"] = "tcp"
    server: str
    server_port: int | None = None


class UDP(BaseServer, DialFields):
    type: Literal["udp"] = "udp"
    server: str
    server_port: int | None = None


class TLSServer(BaseServer, DialFields):
    type: Literal["tls"] = "tls"
    server: str
    server_port: int | None = None
    tls: TLS | None = None


class QUIC(BaseServer, DialFields):
    type: Literal["quic"] = "quic"
    server: str
    server_port: int | None = None
    tls: TLS | None = None


class HTTPS(BaseServer, DialFields):
    type: Literal["https"] = "https"
    server: str
    server_port: int | None = None
    path: str | None = None
    headers: dict[str, Any] | None = None
    tls: TLS | None = None


class HTTP3(BaseServer, DialFields):
    type: Literal["h3"] = "h3"
    server: str
    server_port: int | None = None
    path: str | None = None
    headers: dict[str, Any] | None = None
    tls: TLS | None = None


class DHCP(BaseServer, DialFields):
    type: Literal["dhcp"] = "dhcp"
    interface: str | None = None


class FakeIP(BaseServer):
    type: Literal["fakeip"] = "fakeip"
    inet4_range: str | None = None
    inet6_range: str | None = None


class Tailscale(BaseServer):
    type: Literal["tailscale"] = "tailscale"
    endpoint: str
    accept_default_resolvers: bool | None = None


class Resolved(BaseServer):
    type: Literal["resolved"] = "resolved"
    service: str
    accept_default_resolvers: bool | None = None


Server = Annotated[
    Local | Hosts | TCP | UDP | TLSServer | QUIC | HTTPS | HTTP3 | DHCP | FakeIP | Tailscale | Resolved,
    Field(discriminator="type"),
]
