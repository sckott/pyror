import pytest
import vcr

# import warnings
from pyror import fetch_id

# from requests.exceptions import HTTPError


@vcr.use_cassette("test/vcr_cassettes/fetch_id.yml")
def test_fetch_id():
    "fetch_id"
    res = fetch_id(name="University of Greenwich")
    assert isinstance(res, str)


# # errors
# def test_content_negotiation_ids_missing():
#     with pytest.raises(TypeError):
#         cn.content_negotiation()

# def test_content_negotiation_ids_none():
#     with pytest.raises(TypeError):
#         cn.content_negotiation(ids=None)
