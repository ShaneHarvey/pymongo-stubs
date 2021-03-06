from typing import Any, Dict, Iterable, Iterator, List, Mapping, Optional, Pattern, Tuple, Type, TypeVar, Union

RE_TYPE: Type[Pattern]
_Key = TypeVar("_Key")
_Value = TypeVar("_Value")
_T = TypeVar("_T")

class SON(Dict[_Key, _Value]):
    def __init__(
        self, data: Optional[Union[Mapping[_Key, _Value], Iterable[Tuple[_Key, _Value]]]] = ..., **kwargs: _Value
    ) -> None: ...
    def __new__(cls, *args: Any, **kwargs: Any) -> SON[_Key, _Value]: ...
    def __setitem__(self, key: _Key, value: _Value) -> None: ...
    def __delitem__(self, key: _Key) -> None: ...
    # TODO:  error: Return type "List[_Key]" of "keys" incompatible with return type "KeysView[_Key]" in supertype "dict"
    def keys(self) -> List[_Key]: ...  # type: ignore[override]
    def copy(self) -> SON[_Key, _Value]: ...
    def __iter__(self) -> Iterator[_Key]: ...
    def has_key(self, key: _Key) -> bool: ...
    def iteritems(self) -> Iterator[Tuple[_Key, _Value]]: ...
    def iterkeys(self) -> Iterator[_Key]: ...
    def itervalues(self) -> Iterator[_Value]: ...
    # TODO: error: Return type "List[_Value]" of "values" incompatible with return type "ValuesView[_Value]" in supertype "dict"
    def values(self) -> List[_Value]: ...  # type: ignore[override]
    # TODO: error: Return type "List[Tuple[_Key, _Value]]" of "items" incompatible with return type "ItemsView[_Key, _Value]"
    # in supertype "dict"
    def items(self) -> List[Tuple[_Key, _Value]]: ...  # type: ignore[override]
    def clear(self) -> None: ...
    def setdefault(self, key: _Key, default: Optional[Union[_Value, _T]] = ...) -> Union[_Value, _T]: ...
    def pop(self, key: _Key, *args: Union[_Value, _T]) -> Union[_Value, _T]: ...
    def popitem(self) -> Tuple[_Key, _Value]: ...
    # TODO: error: Signature of "update" incompatible with supertype "dict"
    def update(self, other: Optional[Any] = ..., **kwargs: _Value) -> None: ...  # type: ignore[override]
    def get(self, key: _Key, default: Optional[Union[_Value, _T]] = ...) -> Union[_Value, _T]: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __len__(self) -> int: ...
    def to_dict(self) -> Dict[_Key, _Value]: ...
    def __deepcopy__(self, memo: Any) -> SON[_Key, _Value]: ...
