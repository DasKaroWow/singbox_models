from typing import Annotated, Any, Literal

from pydantic import Field

from singbox_models.base import BaseModel, DialFields, ListenFields, PosixResolvedPath
from singbox_models.base.tls import TLSInbound, TLSOutbound


class BaseService(ListenFields):
    tag: str | None = None


class DERP(BaseService):
    class VerifyClientURL(DialFields):
        url: str

    class MeshWith(DialFields):
        server: str
        server_port: int
        host: str | None = None
        tls: TLSOutbound | None = None

    class Stun(ListenFields):
        enabled: bool

    type: Literal["derp"] = "derp"
    tls: TLSInbound | None = None
    config_path: PosixResolvedPath
    verify_client_endpoint: list[str] | None = None
    verify_client_url: list[str | VerifyClientURL] | None = None
    home: str | None = None
    mesh_with: list[MeshWith] | None = None
    mesh_psk: str | None = None
    mesh_psk_file: PosixResolvedPath | None = None
    stun: int | Stun | None = None


class Resolved(BaseService):
    type: Literal["resolved"] = "resolved"


class SSMAPI(BaseService):
    type: Literal["ssm-api"] = "ssm-api"
    servers: dict[str, str]
    cache_path: PosixResolvedPath | None = None
    tls: TLSInbound | None = None


class CCM(BaseService):
    class User(BaseModel):
        name: str | None = None
        token: str | None = None

    type: Literal["ccm"] = "ccm"
    credential_path: PosixResolvedPath | None = None
    usages_path: PosixResolvedPath | None = None
    users: list[User] | None = None
    headers: dict[str, Any] | None = None
    detour: str | None = None
    tls: TLSInbound | None = None


class OCM(BaseService):
    class User(BaseModel):
        name: str | None = None
        token: str | None = None

    type: Literal["ocm"] = "ocm"
    credential_path: PosixResolvedPath | None = None
    usages_path: PosixResolvedPath | None = None
    users: list[User] | None = None
    headers: dict[str, Any] | None = None
    detour: str | None = None
    tls: TLSInbound | None = None


Service = Annotated[
    DERP | Resolved | SSMAPI | CCM | OCM,
    Field(discriminator="type"),
]
