from rest_framework.generics import ListCreateAPIView

from something.models import Something
from something.serializers import SomethingSerializer


class SomethingListCreateAPIView(ListCreateAPIView):
    queryset = Something.objects.all()
    serializer_class = SomethingSerializer
