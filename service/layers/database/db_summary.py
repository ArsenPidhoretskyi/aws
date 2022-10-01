from models import BaseEntity
from typing import Generic, TypeVar

TEntity = TypeVar("TEntity", bound=BaseEntity)


class ObjectSummary(Generic[TEntity]):
    def __init__(self, object: TEntity) -> None:
        self.id = object.id
        self.createdAt = object.createdAt.isoformat()
        self.updatedAt = object.updatedAt.isoformat()
