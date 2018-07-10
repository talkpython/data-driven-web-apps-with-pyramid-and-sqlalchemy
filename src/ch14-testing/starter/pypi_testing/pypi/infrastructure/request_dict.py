from typing import Any

from pyramid.request import Request


class RequestDictionary(dict):
    def __getattr__(self, key):
        return self.get(key)


def create(request: Request) -> RequestDictionary:
    data = {
        **request.GET,
        **request.headers,
        **request.POST,
        **request.matchdict,
    }

    return RequestDictionary(data)
