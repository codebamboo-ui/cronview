import yaml
from .model import Job, Schedule


def load_schedule(text: str) -> Schedule:
    data = yaml.safe_load(text) or {}
    jobs = []
    for item in data.get("jobs", []) or []:
        jobs.append(
            Job(
                name=item.get("name", "unnamed"),
                schedule=item.get("schedule", "* * * * *"),
                image=item.get("image"),
                command=item.get("command"),
                tags=item.get("tags") or [],
            )
        )
    return Schedule(jobs=jobs)

