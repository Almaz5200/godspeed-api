from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

from Label import Label
from TaskList import TaskList
from Task import Task


@dataclass
class ListTasksResponse:
    success: bool
    labels: List[Label]
    lists: List[TaskList]
    tasks: List[Task]
