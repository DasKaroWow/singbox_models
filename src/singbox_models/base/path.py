from pathlib import Path
from typing import Annotated

from pydantic import PlainSerializer

PosixResolvedPath = Annotated[
    Path,
    PlainSerializer(lambda path: path.resolve().as_posix(), return_type=str),
]
