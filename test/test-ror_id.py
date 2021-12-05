import pytest
import vcr

from pyror import ror_id

@pytest.mark.vcr
def test_ror_id():
    "ror_id"
    res = ror_id('026tem613')
    assert isinstance(res, dict)

