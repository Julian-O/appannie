import requests
from six.moves.urllib.parse import urlencode

from .exception import (AppAnnieException, AppAnnieBadRequestException,
                        AppAnnieNotFoundException,
                        AppAnnieUnauthorizedException,
                        AppAnnieRateLimitException)
from .throttle import throttle

class HttpClient(object):
    ENDPOINT_PREFIX = 'https://api.appannie.com'
    DEFAULT_VERSION = '/v1.2'
    def __init__(self, api_key):
        self.api_key = api_key

    def get_url(self, uri, data=None):

        # Some of the older code assumes the API version number v1.2
        # will be inserted.
        # Some of the newer code explicitly provides the API version
        # number.
        # Detect which this is and adapt appropriately.
        version_shim = "" if uri.startswith("/v1") else self.DEFAULT_VERSION
        url = self.ENDPOINT_PREFIX + version_shim + uri
        if data:
            # urlencode parameters deterministically:
            sorted_values = sorted(data.items(), key=lambda val: val[0])
            url = url + '?' + urlencode(sorted_values)
        return url

    def _get_default_headers(self):
        return {
            'Authorization': 'Bearer ' + self.api_key,
            'Accept': 'application/json',
        }

    # Use throttle decorator to enforce the per-minute rate-limit to avoid
    # 429 responses.
    # Does not enforce daily and monthly limits, nor does it prevent several
    # clashes with other instances/programs running under the same credentials.
    @throttle(min_period=60, max_calls=30)
    def request(self, uri, data=None):
        url = self.get_url(uri, data)
        headers = self._get_default_headers()

        try:
            response = requests.get(url, headers=headers).json()
            if self.is_error(response):
                raise self.get_exception_from_response(response)
            return response
        except requests.exceptions.RequestException as e:
            raise AppAnnieException(str(e))
        except ValueError:
            raise AppAnnieException("Empty data returned by AppAnnie.")

    def is_error(self, response):
        return bool(response.get('error', False))

    def get_exception_from_response(self, response):
        code = response['code']
        message = response['error']
        if code == AppAnnieBadRequestException.ERROR_CODE:
            return AppAnnieBadRequestException(message)
        if code == AppAnnieUnauthorizedException.ERROR_CODE:
            return AppAnnieUnauthorizedException(message)
        if code in [AppAnnieNotFoundException.ERROR_CODE, 405, 403]:
            return AppAnnieNotFoundException(message)
        if code == AppAnnieRateLimitException.ERROR_CODE:
            return AppAnnieRateLimitException(message)
        return AppAnnieException(message)
