import requests

base_url = "https://api.ror.org"


def ror_get(ror=None, name=None, affiliation=None, filter=None, page=None):
    args = {"query": name, "affiliation": affiliation, "filter": filter, "page": page}
    args = {k: v for k, v in args.items() if v is not None}
    url = base_url + "/organizations"
    if ror:
        url = url + "/" + ror
    r = requests.get(url, params=args)
    r.raise_for_status()
    return r.json()
