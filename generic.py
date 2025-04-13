
from typing import TypeVar, Generic

# NOTE: declare a generic type
T = TypeVar('T') 

#NOTE: 'Generic' tells this is a generic class which works with type 'T'
class Box(Generic[T]):
    def __init__(self, item: T) -> None:
        self._item = item

    def get(self) -> T:
        return self._item

    def set(self, item: T) -> None:
        self._item = item

    def __repr__(self) -> str:
        return f"Box({self._item!r})"



from typing import Optional

 
# NOTE: optional means it may or may not return something 
def find_item(index: int) -> Optional[str]:
    items = ["apple", "banana", "cherry"]
    if 0 <= index < len(items):
        return items[index]  # Returns a string, e.g., "apple"
    return None  # No item found, so return None

