import pytest
from MySet import MySet

def test_add_element(empty_set):
    empty_set.add(1)
    assert empty_set.contains(1)

def test_remove_element(sample_set):
    sample_set.remove(2)
    assert not sample_set.contains(2)

def test_union(sample_set):
    other_set = MySet()
    other_set.add(2)
    other_set.add(3)
    other_set.add(4)
    
    result_set = sample_set.union(other_set)
    
    assert result_set.contains(1)
    assert result_set.contains(2)
    assert result_set.contains(3)
    assert result_set.contains(4)

def test_intersection(sample_set):
    other_set = MySet()
    other_set.add(2)
    other_set.add(3)
    other_set.add(4)

    result_set = sample_set.intersection(other_set)

    assert not result_set.contains(1)
    assert result_set.contains(2)
    assert result_set.contains(3)
    assert not result_set.contains(4)

def test_contains(sample_set):
    assert sample_set.contains(1)
    assert not sample_set.contains(4)

if __name__ == "__main__":
    pytest.main()
