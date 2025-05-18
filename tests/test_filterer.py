# tests/test_filterer.py
import pytest
from hn_crawler.filterer import EntryFilterHandler

class Entry:
    def __init__(self, title, comments=0, points=0):
        self.title = title
        self.comments = comments
        self.points = points

@pytest.fixture
def sample_entries():
    return [
        Entry("This is a simple test", comments=10, points=5),
        Entry("Another title with more than five words here", comments=20, points=15),
        Entry("Short title", comments=5, points=25)
    ]

def test_count_words():
    # Assuming count_words splits on spaces and counts only words
    assert EntryFilterHandler.count_words("This is - a self-explained example") == 5
    assert EntryFilterHandler.count_words("Four words only") == 3  # "Four words only" is 3 words

def test_filter_more_than_five_words(sample_entries):
    ef = EntryFilterHandler()
    result = ef.filter_more_than_five_words(sample_entries)
    assert len(result) == 1
    assert result[0].title == "Another title with more than five words here"

def test_filter_five_or_fewer_words(sample_entries):
    ef = EntryFilterHandler()
    result = ef.filter_five_or_fewer_words(sample_entries)
    assert len(result) == 2
    titles = [e.title for e in result]
    assert "Short title" in titles
    assert "This is a simple test" in titles
