import grpc
from concurrent import futures

from grpc_gen import something_pb2, something_pb2_grpc
from something_generator import process_somethings


class SomethingProcessorServicer(something_pb2_grpc.SomethingProcessorServicer):
    def ProcessSomething(self, request, context):
        something = request.something

        updated = process_somethings(something)

        print(updated)

        return something_pb2.ProcessSomethingResponse(something=updated)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    something_pb2_grpc.add_SomethingProcessorServicer_to_server(SomethingProcessorServicer(), server)
    server.add_insecure_port("[::]:50051")
    print("✅ Service B running on port 50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
