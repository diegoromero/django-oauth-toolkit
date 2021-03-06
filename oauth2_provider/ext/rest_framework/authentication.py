from rest_framework.authentication import BaseAuthentication

from ...oauth2_backends import get_oauthlib_core

from mongoengine.django.auth import User


class OAuth2Authentication(BaseAuthentication):
    """
    OAuth 2 authentication backend using `django-oauth-toolkit`
    """
    www_authenticate_realm = 'api'

    def authenticate(self, request):
        """
        Returns two-tuple of (user, token) if authentication succeeds,
        or None otherwise.
        """
        oauthlib_core = get_oauthlib_core()
        valid, r = oauthlib_core.verify_request(request, scopes=[])
        if valid:
            user = User.objects.get(pk=r.user)
            return user, r.access_token
        else:
            return None

    def authenticate_header(self, request):
        """
        Bearer is the only finalized type currently
        """
        return 'Bearer realm="%s"' % self.www_authenticate_realm
