from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime


@dataclass
class TaskList:
    id: str
    user_id: int
    name: str
    order_index: float
    created_at: datetime
    updated_at: Optional[datetime]
    list_type: str
    indent_level: int
    smart_list_query: Optional[str]
    persistent_sort_field: Optional[str]
    persistent_sort_order: Optional[str]
    ordinal: str
    collaborator_user_ids: List[int]
