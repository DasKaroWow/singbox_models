from typing import Literal

from singbox_models.base.base import BaseModel


class Brutal(BaseModel):
    enabled: bool | None = None
    up_mbps: int | None = None
    down_mbps: int | None = None


class MultiplexInbound(BaseModel):
    enabled: bool | None = None
    padding: bool | None = None
    brutal: Brutal | None = None


class MultiplexOutbound(BaseModel):
    enabled: bool | None = None
    protocol: Literal["smux", "yamux", "h2mux"] | None = None
    max_connections: int | None = None
    min_streams: int | None = None
    max_streams: int | None = None
    padding: bool | None = None
    brutal: Brutal | None = None


Multiplex = MultiplexInbound | MultiplexOutbound
