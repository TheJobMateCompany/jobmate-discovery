import grpc
from concurrent import futures
import sys
import os

# Ajout du chemin pour trouver les modules générés
sys.path.append(os.path.abspath("./proto/gen/python"))

# Import des modules générés (attention aux noms exacts générés par Buf)
from proto.discovery.v1 import service_pb2 as pb2
from proto.discovery.v1 import service_pb2_grpc as pb2_grpc
from proto.common.v1 import types_pb2


class DiscoveryService(pb2_grpc.DiscoveryServiceServicer):
    def AddJobUrl(self, request, context):
        print(f"Reçu demande d'ajout URL: {request.url}")
        # Dummy response
        return pb2.JobCard(
            id="job_123",
            title="Dev React",
            company="Tech Corp",
            source_url=request.url,
            is_approved=True,
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_DiscoveryServiceServicer_to_server(DiscoveryService(), server)
    server.add_insecure_port("[::]:50052")
    print("Discovery Service listening on :50052")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
