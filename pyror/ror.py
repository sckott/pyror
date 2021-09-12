from .request import ror_get


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
    items = w["items"]
    if name in [x["name"] for x in items]:
        match = [x for x in items if name in x["name"]]
    return match[0]["id"].split("/")[-1]


def ror_id(name=None, affiliation=None, filter=None, page=None):
    """
    Search for a ROR ID using an institution name

    :param name: [String] An institution name
    :param affiliation: [String] An institution name
    :param filter: [String] An institution name
    :param page: [String] returns a max of 20 results/page, beginning at page 1.
        by dafault this parameter isn't passed

    :return: str, a ROR ID

    Usage::

            from pyror import ror_id
            ror_id(name = 'University of Greenwich')
    """
    w = ror_get(name=name, affiliation=affiliation, filter=filter, page=page)
    items = w["items"]
    if name in [x["name"] for x in items]:
        match = [x for x in items if name in x["name"]]
    return match[0]["id"].split("/")[-1]
