from django_keycloak.keycloak.aio.mixins import WellKnownMixin
from django_keycloak.keycloak.openid_connect import (
    KeycloakOpenidConnect as SyncKeycloakOpenidConnect,
    PATH_WELL_KNOWN,
)

__all__ = (
    'KeycloakOpenidConnect',
)


class KeycloakOpenidConnect(WellKnownMixin, SyncKeycloakOpenidConnect):
    def get_path_well_known(self):
        return PATH_WELL_KNOWN
