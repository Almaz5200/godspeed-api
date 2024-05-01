from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Attachment:
    id: str
    name: str
    todo_item_id: str
    created_at: datetime
    updated_at: Optional[datetime]
    file_type: str
    user_id: int
    todo_item_deleted_at: Optional[datetime]
    order_index: int
    file_size_in_bytes: int
