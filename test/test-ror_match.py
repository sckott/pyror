import pytest
import vcr

from pyror import ror_match

@pytest.mark.vcr
def test_ror_match():
    "ror_match"
    res = ror_match(name = 'University of Greenwich')
    assert isinstance(res, dict)

    res2 = ror_match(name = 'University of Green')
    assert isinstance(res2, list)
    for x in res2:
        assert isinstance(x, dict)

