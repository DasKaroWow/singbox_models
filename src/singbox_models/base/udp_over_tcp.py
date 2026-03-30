from typing import Literal

from singbox_models.base.base import BaseModel


class UDPOverTCP(BaseModel):
    enabled: bool | None = None
    version: Literal[1, 2] | None = None
