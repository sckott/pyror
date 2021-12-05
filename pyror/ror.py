from .request import ror_get
from .utils import parse_ids


def ror_id(ror):
    """
    Get data by ROR ID

    :param ror: [String] A ROR ID

    :return: a dictionary

    Usage::

            from pyror import ror_id
            ror_id('026tem613')
    """
    w = ror_get(ror=ror)
    return w


def ror_search(name=None, affiliation=None, filter=None, page=None):
    """
    Search ROR

    :param name: [String] An institution name
    :param affiliation: [String] An affiliation name
    :param filter: [String] filter by: type, country code or country name.
        types: 'Education', 'Healthcare', 'Company', 'Archive', 'Nonprofit',
        'Government', 'Facility', 'Other'. country codes are those in the ISO 3166 alpha-2 list
    :param page: [String] returns a max of 20 results/page, beginning at page 1.
        by dafault this parameter isn't passed

    :return: a dictionary

    Usage::

            from pyror import ror_search
            ror_search(name = 'University of Greenwich')
    """
    w = ror_get(name=name, affiliation=affiliation, filter=filter, page=page)
    return w


def ror_match(name=None, affiliation=None, filter=None, page=None):
    """
    Search for a ROR ID, and try to extract an exact match

    :param name: [String] An institution name
    :param affiliation: [String] An institution name
    :param filter: [String] An institution name
    :param page: [String] returns a max of 20 results/page, beginning at page 1.
        by dafault this parameter isn't passed

    :return: dict or list of dicts with a subset of fields
        (id, name, links, grid_id)

    Usage::

            from pyror import ror_match
            ror_match(name = 'University of Greenwich')
            ror_match(name = 'University of Green')
    """
    x = ror_search(name=name, affiliation=affiliation, filter=filter, page=page)
    items = x["items"]
    z = [parse_ids(w) for w in items]
    if name in [w["name"] for w in z]:
        match = [x for x in z if name in x["name"]]
        return match[0]
    else:
        # print("no exact match, returning dict of all results")
        return z
