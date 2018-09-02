class PaginatorFactory(object):
    def __init__(self, http_client):
        self.http_client = http_client

    def make(self, uri, data=None, union_key=None):
        return Paginator(self.http_client, uri, data, union_key)


class Paginator(object):
    def __init__(self, http_client, uri, data=None, union_key=None):
        self.http_client = http_client
        self.union_key = union_key
        self.uri = uri
        # Copy dictionary, defaulting to empty.
        self.data = dict(data or {})

    def page(self, page=0):
        # Add page_index to the dictionary passed in request.
        data = dict(self.data)
        data['page_index'] = page - 1

        return self.http_client.request(self.uri, data)

    def all(self):
        if not self.union_key:
            raise ValueError("Union key parameter is missing")

        union_result = []

        data = dict(self.data)

        page_num = 1
        page_index = 0

        while page_index < page_num:
            data['page_index'] = page_index
            page_result = self.http_client.request(self.uri, data)
            page_num = page_result.get('page_num')
            if page_num is None:
                return page_result.get(self.union_key, [])
            page_index = page_result.get('page_index') + 1
            page_result = page_result.get(self.union_key, [])
            union_result.extend(page_result)

        return union_result

    def __iter__(self):
        if not self.union_key:
            raise ValueError("Union key parameter is missing")

        page_index = 0
        data = dict(self.data)

        while True:
            data['page_index'] = page_index
            whole_page_result = self.http_client.request(self.uri, data)
            interesting_data = whole_page_result.get(self.union_key, [])
            for entry in interesting_data:
                yield entry
            page_num = whole_page_result.get('page_num')

            # Check if that was the last page.
            if not page_num or page_index >= page_num - 1:
                break

            page_index += 1
