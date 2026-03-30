from typing import Literal

from singbox_models.base import BaseModel, PosixResolvedPath


class Log(BaseModel):
    disabled: bool | None = None
    level: Literal["trace", "debug", "info", "warn", "error", "fatal", "panic"] | None = None
    output: PosixResolvedPath | None = None
    timestamp: bool | None = None
