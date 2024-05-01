from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

from .Attachment import Attachment


@dataclass
class Task:
    id: str
    title: str
    list_id: str
    user_id: int
    order_index: float
    indent_level: int
    completed_at: Optional[datetime]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    cleared_at: Optional[datetime]
    notified_at: Optional[datetime]
    repeat_value: Optional[int]
    repeat_unit: Optional[str]
    repeat_unit_metadata: Optional[dict]
    repeat_from: Optional[str]
    notes: str
    ordinal: str
    todo_item_attachments: List[Attachment]
    label_ids: List[str]
    due_at: Optional[datetime]
    snoozed_until: Optional[datetime]
    starts_at: Optional[datetime]
    snooze_count: int
    is_due_at_timeless: bool
    is_snoozed_until_timeless: bool
    is_starts_at_timeless: bool
