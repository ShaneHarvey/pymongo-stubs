from datetime import datetime
from typing import Any, Iterable, List, Mapping, Optional

from pymongo.client_session import ClientSession
from pymongo.collection import Collection
from pymongo.cursor import Cursor

EMPTY: bytes
NEWLN: bytes
DEFAULT_CHUNK_SIZE: int

class GridIn:
    def __init__(
        self, root_collection: Collection, session: Optional[ClientSession] = ..., disable_md5: bool = ..., **kwargs: Any
    ) -> None: ...
    def abort(self) -> None: ...
    @property
    def closed(self) -> bool: ...
    _id: Any = ...
    filename: Optional[str] = ...
    name: Optional[str] = ...
    content_type: Optional[str] = ...
    length: int = ...
    chunk_size: int = ...
    upload_date: datetime = ...
    md5: Optional[str] = ...
    def __getattr__(self, name: str) -> Any: ...
    def __setattr__(self, name: str, value: Any) -> None: ...
    def close(self) -> None: ...
    def read(self, size: int = ...) -> None: ...
    def readable(self) -> bool: ...
    def seekable(self) -> bool: ...
    def write(self, data: Any) -> None: ...
    def writelines(self, sequence: Iterable[Any]) -> None: ...
    def writeable(self) -> bool: ...
    def __enter__(self) -> GridIn: ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> bool: ...

class GridOut:
    def __init__(
        self,
        root_collection: Collection,
        file_id: Optional[Any] = ...,
        file_document: Optional[Any] = ...,
        session: Optional[ClientSession] = ...,
    ) -> None: ...
    _id: Any = ...
    filename: str = ...
    name: str = ...
    content_type: Optional[str] = ...
    length: int = ...
    chunk_size: int = ...
    upload_date: datetime = ...
    aliases: Optional[List[str]] = ...
    metadata: Optional[Mapping[str, Any]] = ...
    md5: Optional[str] = ...
    def __getattr__(self, name: str) -> Any: ...
    def readable(self) -> bool: ...
    def readchunk(self) -> bytes: ...
    def read(self, size: int = ...) -> bytes: ...
    def readline(self, size: int = ...) -> bytes: ...
    def tell(self) -> int: ...
    def seek(self, pos: int, whence: int = ...) -> None: ...
    def seekable(self) -> bool: ...
    def __iter__(self) -> GridOutIterator: ...
    def close(self) -> None: ...
    def write(self, value: Any) -> None: ...
    def __enter__(self) -> GridOut: ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> bool: ...

class GridOutIterator:
    def __init__(self, grid_out: GridOut, chunks: Collection, session: Optional[ClientSession]) -> None: ...
    def __iter__(self) -> GridOutIterator: ...
    def next(self) -> bytes: ...
    def __next__(self) -> bytes: ...

class GridOutCursor(Cursor):
    def __init__(
        self,
        collection: Collection,
        filter: Optional[Mapping[str, Any]] = ...,
        skip: int = ...,
        limit: int = ...,
        no_cursor_timeout: bool = ...,
        sort: Optional[Any] = ...,
        batch_size: int = ...,
        session: Optional[ClientSession] = ...,
    ) -> None: ...
    # error: Return type "GridOut" of "next" incompatible with return type "Dict[str, Any]" in supertype "Cursor"
    def next(self) -> GridOut: ...  # type: ignore[override]
    def __next__(self) -> GridOut: ...  # type: ignore[override]
    # TODO: error: Signature of "add_option" incompatible with supertype "Cursor"
    # Change pymongo to "mask: int"
    def add_option(self, *args: Any, **kwargs: Any) -> None: ...  # type: ignore[override]
    def remove_option(self, *args: Any, **kwargs: Any) -> None: ...  # type: ignore[override]
