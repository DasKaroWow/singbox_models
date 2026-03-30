from typing import Literal

from singbox_models.base import BaseModel, PosixResolvedPath


class Certificate(BaseModel):
    store: Literal["system", "mozilla", "chrome", ""] | None = None
    certificate: list[str] | None = None
    certificate_path: list[PosixResolvedPath] | None = None
    certificate_directory_path: list[PosixResolvedPath] | None = None
