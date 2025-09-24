import grpc
from rest_framework.generics import ListCreateAPIView

from something.models import Something
from something.serializers import SomethingSerializer
from something.grpc_gen import something_pb2, something_pb2_grpc


class SomethingListCreateAPIView(ListCreateAPIView):
    queryset = Something.objects.all()
    serializer_class = SomethingSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

        # Connect to Service B (running on localhost:50051)
        channel = grpc.insecure_channel("localhost:50051")
        stub = something_pb2_grpc.SomethingProcessorStub(channel)

        request = something_pb2.ProcessSomethingRequest(
            something=something_pb2.SomethingMessage(
                id=str(instance.id),
                title=instance.title,
                something_from_another_service=instance.something_from_another_service or "",
            )
        )

        response = stub.ProcessSomething(request)

        instance.something_from_another_service = response.something.something_from_another_service
        instance.save()
