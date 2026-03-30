from typing import Literal

from singbox_models.base import BaseModel
from singbox_models.dns.rules import Rule
from singbox_models.dns.server import FakeIP, Server


class DNS(BaseModel):
    servers: list[Server] | None = None
    rules: list[Rule] | None = None
    fakeip: FakeIP | None = None
    final: str | None = None
    strategy: Literal["prefer_ipv4", "prefer_ipv6", "ipv4_only", "ipv6_only"] | None = None
    disable_cache: bool | None = None
    disable_expire: bool | None = None
    independent_cache: bool | None = None
    cache_capacity: int | None = None
    reverse_mapping: bool | None = None
    client_subnet: str | None = None
