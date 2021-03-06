from django.utils import timezone

from tazboard.api.queries.common import get_interval_filter_exclude_bots, get_ranges


def get_total_query(min_date, max_date=timezone.now()):
    min_date_previous_interval = min_date - (max_date - min_date)
    query = {
        "aggs": {
            **get_ranges(
                min_date_previous_interval, min_date, max_date
            ),
        },
        "query": get_interval_filter_exclude_bots(min_date_previous_interval, max_date)
    }
    return query
