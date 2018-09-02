import datetime
from six import iteritems, string_types
DATE_FORMAT = '%Y-%m-%d'
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'


def round_to_day(date):
    return datetime.date(*date.timetuple()[:3])


def to_day(date_or_date_string, date_format=DATE_FORMAT):
    """Convert to a datetime.date instance, rounded down to day."""
    if isinstance(date_or_date_string, string_types):
        date = datetime.datetime.strptime(date_or_date_string, date_format)
    elif isinstance(date_or_date_string, datetime.datetime):
        date = date_or_date_string
    elif isinstance(date_or_date_string, datetime.date):
        date = datetime.datetime(
            year=date_or_date_string.year,
            month=date_or_date_string.month,
            day=date_or_date_string.day)
    else:
        raise ValueError('invalid argument: %r' % date_or_date_string)
    return round_to_day(date)


def collection_to_str(collection, joinstr='+'):
    if isinstance(collection, string_types):
        return collection
    return joinstr.join([str(item) for item in collection])


def format_request_data(**kwargs):
    data = {k: v for k, v in iteritems(kwargs) if v is not None}
    if data.get('date'):
        data['date'] = str(to_day(data['date']))
    if data.get('start_date'):
        data['start_date'] = str(to_day(data['start_date']))
    if data.get('end_date'):
        data['end_date'] = str(to_day(data['end_date']))
    if data.get('countries'):
        data['countries'] = collection_to_str(data['countries']).upper()
    if data.get('categories'):
        data['categories'] = collection_to_str(data['categories'])
    if data.get('category'):
        data['category'] = collection_to_str(data['category'])
    if data.get('device'):
        data['device'] = collection_to_str(data['device'])
    if data.get('types'):
        data['types'] = collection_to_str(data['types'])
    if data.get('keywords'):
        data['keywords'] = collection_to_str(data['keywords'], ',')
    return data
