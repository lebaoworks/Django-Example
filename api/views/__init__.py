from rest_framework.views import APIView
from rest_framework.response import Response

from api.views.sample import Sample

from django.urls import get_resolver
class ListAPIs(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
 
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        return Response(set(v[1] for k,v in get_resolver(None).reverse_dict.items()))