"""RadiusProvider API Views"""
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from authentik.core.api.providers import ProviderSerializer
from authentik.core.api.used_by import UsedByMixin
from authentik.providers.radius.models import RadiusProvider


class RadiusProviderSerializer(ProviderSerializer):
    """RadiusProvider Serializer"""

    class Meta:

        model = RadiusProvider
        fields = ProviderSerializer.Meta.fields + [
            "client_networks",
            "certificate",
        ]


class RadiusProviderViewSet(UsedByMixin, ModelViewSet):
    """RadiusProvider Viewset"""

    queryset = RadiusProvider.objects.all()
    serializer_class = RadiusProviderSerializer
    ordering = ["name"]


class RadiusOutpostConfigSerializer(ModelSerializer):
    """RadiusProvider Serializer"""

    application_slug = CharField(source="application.slug")
    auth_flow_slug = CharField(source="authorization_flow.slug")

    class Meta:

        model = RadiusProvider
        fields = [
            "pk",
            "name",
            "application_slug",
            "auth_flow_slug",
            "client_networks",
            "certificate",
        ]


class RadiusOutpostConfigViewSet(ReadOnlyModelViewSet):
    """RadiusProvider Viewset"""

    queryset = RadiusProvider.objects.filter(application__isnull=False)
    serializer_class = RadiusOutpostConfigSerializer
    ordering = ["name"]