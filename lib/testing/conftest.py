#!/usr/bin/env python3
import pytest
from MySet import MySet

@pytest.fixture
def empty_set():
    return MySet()

@pytest.fixture
def sample_set():
    s = MySet()
    s.add(1)
    s.add(2)
    s.add(3)
    return s
