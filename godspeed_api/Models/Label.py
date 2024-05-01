from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime


@dataclass
class Label:
    id: str
    name: str
    color_hex_string: str
    user_id: int
    deleted_at: Optional[datetime]
    created_at: datetime
    updated_at: Optional[datetime]
    associated_shared_list_id: Optional[str]
