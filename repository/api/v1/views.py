"""
Views api for V1.
"""

from api import views
from . import serializers as v1_serializers


class NestedProgramViewSet(
    views.NestedProgramViewSet
):  # pylint: disable=too-many-ancestors
    """
    Nested program view set first version. Use NestedProgramSerializer V1.
    """

    serializer_class = v1_serializers.NestedProgramSerializer
