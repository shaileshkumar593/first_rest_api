from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from profile_rest_api import serializer
from profile_rest_api import models
from profile_rest_api import permissions

# Create your views here.


class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializer.HelloSerializer

    def get(self, request, format=None):
        """ Returns a list of APIViews features"""

        an_apiview = [
            'uses HTTP methods as functions(get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """create a hello message with our name """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API viewset"""
    serializer_class = serializer.HelloSerializer

    def list(self, request):
        """Return API viewSet """
        serializer_class = serializer.HelloSerializer
        a_viewset = [
            'uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionalityh with less code',
        ]

        return Response({'message': 'Hello! ', 'a_viewset': a_viewset})

    def create(self, request):
        """ Cretae a new hello message """
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'

            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """ Handle updating part of an object"""

        return  Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return  Response({'http_method':'delete'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle Creating,Creating and updating profiles"""

    serializer_class = serializer.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)