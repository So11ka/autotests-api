import random
from pytest import mark

os = 'Windows'

@mark.flaky(reruns=3)
def test_reruns():
    assert random.choice([True, False])

@mark.flaky(reruns=3, reruns_delay=2)
class TestReruns:
    def test_reruns1(self):
        assert random.choice([True, False])

    def test_reruns2(self):
        assert random.choice([True, False])

@mark.flaky(reruns=2, condition=os == "Windows")
def test_reruns_with_condition():
    assert random.choice([True, False])