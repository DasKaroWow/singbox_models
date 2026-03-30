from singbox_models.base import DialFields


class NTP(DialFields):
    enabled: bool | None = None
    server: str
    server_port: int | None = None
    interval: str | None = None
