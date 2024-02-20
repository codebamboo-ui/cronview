from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Job:
    name: str
    schedule: str  # cron expression
    image: Optional[str] = None
    command: Optional[str] = None
    tags: List[str] = field(default_factory=list)


@dataclass
class Schedule:
    jobs: List[Job] = field(default_factory=list)

