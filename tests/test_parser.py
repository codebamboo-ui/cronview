from cronview.parser import load_schedule


def test_load_minimal():
    sched = load_schedule("jobs: []\n")
    assert sched.jobs == []


def test_load_sample():
    text = """
jobs:
  - name: a
    schedule: "* * * * *"
    image: alpine
    command: echo hi
"""
    sched = load_schedule(text)
    assert len(sched.jobs) == 1
    assert sched.jobs[0].name == "a"

