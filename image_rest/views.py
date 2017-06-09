from rest_framework import generics, permissions
from image_rest.models import Image
from image_rest.serializers import ImageSerializer

class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(uploader=self.request.user)

