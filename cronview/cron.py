from datetime import datetime
from typing import List


def is_valid_cron(expr: str) -> bool:
    parts = expr.split()
    return len(parts) == 5


def explain(expr: str) -> str:
    # Very rough explanation for MVP; not a full parser.
    if not is_valid_cron(expr):
        return "invalid cron expression"
    minute, hour, dom, month, dow = expr.split()
    return (
        f"minute={minute}, hour={hour}, day_of_month={dom}, "
        f"month={month}, day_of_week={dow}"
    )


def next_runs(expr: str, start: datetime, count: int = 3) -> List[datetime]:
    # Placeholder: naive next minute steps until count; not accurate.
    # Good enough for early visualization.
    if not is_valid_cron(expr):
        return []
    out = []
    current = start.replace(second=0, microsecond=0)
    while len(out) < count:
        current = current.replace(minute=(current.minute + 1) % 60)
        if current.minute == 0:
            current = current.replace(hour=(current.hour + 1) % 24)
        out.append(current)
    return out

