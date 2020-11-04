from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple, Union

class InsertOne:
    def __init__(self, document: Mapping[str, Any]) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

class DeleteOne:
    def __init__(self, filter: Mapping[str, Any], collation: Optional[Any] = ..., hint: Optional[Any] = ...) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

class DeleteMany:
    def __init__(self, filter: Mapping[str, Any], collation: Optional[Any] = ..., hint: Optional[Any] = ...) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

class ReplaceOne:
    def __init__(
        self,
        filter: Mapping[str, Any],
        replacement: Mapping[str, Any],
        upsert: bool = ...,
        collation: Optional[Any] = ...,
        hint: Optional[Any] = ...,
    ) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

class UpdateOne:
    def __init__(
        self,
        filter: Mapping[str, Any],
        update: Union[Mapping[str, Any], List[Mapping[str, Any]]],
        upsert: bool = ...,
        collation: Optional[Any] = ...,
        array_filters: Optional[List[Mapping[str, Any]]] = ...,
        hint: Optional[Any] = ...,
    ) -> None: ...

class UpdateMany:
    def __init__(
        self,
        filter: Mapping[str, Any],
        update: Union[Mapping[str, Any], List[Mapping[str, Any]]],
        upsert: bool = ...,
        collation: Optional[Any] = ...,
        array_filters: Optional[List[Mapping[str, Any]]] = ...,
        hint: Optional[Any] = ...,
    ) -> None: ...

class IndexModel:
    def __init__(self, keys: Union[str, Sequence[Tuple[str, Union[int, str, Mapping[str, Any]]]]], **kwargs: Any) -> None: ...
    @property
    def document(self) -> Dict[str, Any]: ...
