from typing import Annotated, Any, Literal

from pydantic import Field

from singbox_models.base.base import BaseModel


class HTTPTransport(BaseModel):
    type: Literal["http"] = "http"
    host: list[str] | None = None
    path: str | None = None
    method: str | None = None
    headers: dict[str, Any] | None = None
    idle_timeout: str | None = None
    ping_timeout: str | None = None


class WebSocketTransport(BaseModel):
    type: Literal["ws"] = "ws"
    path: str | None = None
    headers: dict[str, Any] | None = None
    max_early_data: int | None = None
    early_data_header_name: str | None = None


class QUICTransport(BaseModel):
    type: Literal["quic"] = "quic"


class GRPCTransport(BaseModel):
    type: Literal["grpc"] = "grpc"
    service_name: str | None = None
    idle_timeout: str | None = None
    ping_timeout: str | None = None
    permit_without_stream: bool | None = None


class HTTPUpgradeTransport(BaseModel):
    type: Literal["httpupgrade"] = "httpupgrade"
    host: str | None = None
    path: str | None = None
    headers: dict[str, Any] | None = None


Transport = Annotated[
    HTTPTransport | WebSocketTransport | QUICTransport | GRPCTransport | HTTPUpgradeTransport,
    Field(discriminator="type"),
]
