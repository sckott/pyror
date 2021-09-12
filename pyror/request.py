import requests

base_url = "https://api.ror.org"


def ror_get(name, affiliation, filter, page):
    args = {"query": name, "affiliation": affiliation, "filter": filter, "page": page}
    r = requests.get(base_url + "/organizations", params=args)
    r.raise_for_status()
    return r.json()
