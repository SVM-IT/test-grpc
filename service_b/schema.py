import dataclasses
from typing import Optional


@dataclasses.dataclass
class SomethingSchema:
    title: str
    something_from_another_service: Optional[str]
