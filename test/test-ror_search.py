import pytest
import vcr

from pyror import ror_search

@pytest.mark.vcr
def test_ror_search():
    "ror_search"
    res = ror_search(name = 'University of Greenwich')
    assert isinstance(res, dict)

