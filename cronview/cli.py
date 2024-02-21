from pathlib import Path
from datetime import datetime
from .parser import load_schedule
from .cron import explain, next_runs


def main():
    import argparse

    ap = argparse.ArgumentParser(description="DockerDesk cron viewer")
    ap.add_argument("file", type=str, help="YAML schedule file")
    args = ap.parse_args()

    text = Path(args.file).read_text(encoding="utf-8")
    sched = load_schedule(text)
    now = datetime.now()

    for job in sched.jobs:
        print(f"- {job.name}")
        print(f"  schedule: {job.schedule} -> {explain(job.schedule)}")
        runs = next_runs(job.schedule, now, 3)
        if runs:
            print("  next:")
            for r in runs:
                print(f"    - {r}")
        if job.image:
            print(f"  image: {job.image}")
        if job.command:
            print(f"  command: {job.command}")

