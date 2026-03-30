from singbox_models.base.base import BaseModel


class ListenFields(BaseModel):
    listen: str
    listen_port: int | None = None
    bind_interface: str | None = None
    routing_mark: int | str | None = None
    reuse_addr: bool | None = None
    netns: str | None = None
    tcp_fast_open: bool | None = None
    tcp_multi_path: bool | None = None
    disable_tcp_keep_alive: bool | None = None
    tcp_keep_alive: str | None = None
    tcp_keep_alive_interval: str | None = None
    udp_fragment: bool | None = None
    udp_timeout: str | None = None
    detour: str | None = None
