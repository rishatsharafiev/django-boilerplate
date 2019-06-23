import django_filters

from ..models import Log


class LogListFilter(django_filters.FilterSet):
    """Log List Filter"""

    class Meta:
        """Meta class"""

        model = Log
        fields = {
            'ip_address': ['icontains'],
            'created_at': ['lte', 'gte'],
            'method': ['icontains'],
            'uri': ['icontains'],
            'code': ['icontains'],
            'size': ['exact', 'lt', 'gt'],
        }
