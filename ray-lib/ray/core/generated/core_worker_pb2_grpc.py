# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import core_worker_pb2 as src_dot_ray_dot_protobuf_dot_core__worker__pb2


class CoreWorkerServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.PushTask = channel.unary_unary(
        '/ray.rpc.CoreWorkerService/PushTask',
        request_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.PushTaskRequest.SerializeToString,
        response_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.PushTaskReply.FromString,
        )
    self.DirectActorCallArgWaitComplete = channel.unary_unary(
        '/ray.rpc.CoreWorkerService/DirectActorCallArgWaitComplete',
        request_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.DirectActorCallArgWaitCompleteRequest.SerializeToString,
        response_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.DirectActorCallArgWaitCompleteReply.FromString,
        )
    self.GetObjectStatus = channel.unary_unary(
        '/ray.rpc.CoreWorkerService/GetObjectStatus',
        request_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.GetObjectStatusRequest.SerializeToString,
        response_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.GetObjectStatusReply.FromString,
        )
    self.WaitForActorOutOfScope = channel.unary_unary(
        '/ray.rpc.CoreWorkerService/WaitForActorOutOfScope',
        request_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.WaitForActorOutOfScopeRequest.SerializeToString,
        response_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.WaitForActorOutOfScopeReply.FromString,
        )
    self.WaitForObjectEviction = channel.unary_unary(
        '/ray.rpc.CoreWorkerService/WaitForObjectEviction',
        request_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.WaitForObjectEvictionRequest.SerializeToString,
        response_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.WaitForObjectEvictionReply.FromString,
        )
    self.AddObjectLocationOwner = channel.unary_unary(
        '/ray.rpc.CoreWorkerService/AddObjectLocationOwner',
        request_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.AddObjectLocationOwnerRequest.SerializeToString,
        response_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.AddObjectLocationOwnerReply.FromString,
        )
    self.RemoveObjectLocationOwner = channel.unary_unary(
        '/ray.rpc.CoreWorkerService/RemoveObjectLocationOwner',
        request_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.RemoveObjectLocationOwnerRequest.SerializeToString,
        response_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.RemoveObjectLocationOwnerReply.FromString,
        )
    self.GetObjectLocationsOwner = channel.unary_unary(
        '/ray.rpc.CoreWorkerService/GetObjectLocationsOwner',
        request_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.GetObjectLocationsOwnerRequest.SerializeToString,
        response_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.GetObjectLocationsOwnerReply.FromString,
        )
    self.KillActor = channel.unary_unary(
        '/ray.rpc.CoreWorkerService/KillActor',
        request_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.KillActorRequest.SerializeToString,
        response_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.KillActorReply.FromString,
        )
    self.CancelTask = channel.unary_unary(
        '/ray.rpc.CoreWorkerService/CancelTask',
        request_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.CancelTaskRequest.SerializeToString,
        response_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.CancelTaskReply.FromString,
        )
    self.RemoteCancelTask = channel.unary_unary(
        '/ray.rpc.CoreWorkerService/RemoteCancelTask',
        request_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.RemoteCancelTaskRequest.SerializeToString,
        response_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.RemoteCancelTaskReply.FromString,
        )
    self.GetCoreWorkerStats = channel.unary_unary(
        '/ray.rpc.CoreWorkerService/GetCoreWorkerStats',
        request_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.GetCoreWorkerStatsRequest.SerializeToString,
        response_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.GetCoreWorkerStatsReply.FromString,
        )
    self.WaitForRefRemoved = channel.unary_unary(
        '/ray.rpc.CoreWorkerService/WaitForRefRemoved',
        request_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.WaitForRefRemovedRequest.SerializeToString,
        response_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.WaitForRefRemovedReply.FromString,
        )
    self.LocalGC = channel.unary_unary(
        '/ray.rpc.CoreWorkerService/LocalGC',
        request_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.LocalGCRequest.SerializeToString,
        response_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.LocalGCReply.FromString,
        )
    self.SpillObjects = channel.unary_unary(
        '/ray.rpc.CoreWorkerService/SpillObjects',
        request_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.SpillObjectsRequest.SerializeToString,
        response_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.SpillObjectsReply.FromString,
        )
    self.RestoreSpilledObjects = channel.unary_unary(
        '/ray.rpc.CoreWorkerService/RestoreSpilledObjects',
        request_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.RestoreSpilledObjectsRequest.SerializeToString,
        response_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.RestoreSpilledObjectsReply.FromString,
        )
    self.DeleteSpilledObjects = channel.unary_unary(
        '/ray.rpc.CoreWorkerService/DeleteSpilledObjects',
        request_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.DeleteSpilledObjectsRequest.SerializeToString,
        response_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.DeleteSpilledObjectsReply.FromString,
        )
    self.PlasmaObjectReady = channel.unary_unary(
        '/ray.rpc.CoreWorkerService/PlasmaObjectReady',
        request_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.PlasmaObjectReadyRequest.SerializeToString,
        response_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.PlasmaObjectReadyReply.FromString,
        )
    self.Exit = channel.unary_unary(
        '/ray.rpc.CoreWorkerService/Exit',
        request_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.ExitRequest.SerializeToString,
        response_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.ExitReply.FromString,
        )


class CoreWorkerServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def PushTask(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DirectActorCallArgWaitComplete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetObjectStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WaitForActorOutOfScope(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WaitForObjectEviction(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddObjectLocationOwner(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveObjectLocationOwner(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetObjectLocationsOwner(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def KillActor(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CancelTask(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoteCancelTask(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetCoreWorkerStats(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WaitForRefRemoved(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def LocalGC(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SpillObjects(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RestoreSpilledObjects(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteSpilledObjects(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PlasmaObjectReady(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Exit(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CoreWorkerServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'PushTask': grpc.unary_unary_rpc_method_handler(
          servicer.PushTask,
          request_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.PushTaskRequest.FromString,
          response_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.PushTaskReply.SerializeToString,
      ),
      'DirectActorCallArgWaitComplete': grpc.unary_unary_rpc_method_handler(
          servicer.DirectActorCallArgWaitComplete,
          request_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.DirectActorCallArgWaitCompleteRequest.FromString,
          response_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.DirectActorCallArgWaitCompleteReply.SerializeToString,
      ),
      'GetObjectStatus': grpc.unary_unary_rpc_method_handler(
          servicer.GetObjectStatus,
          request_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.GetObjectStatusRequest.FromString,
          response_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.GetObjectStatusReply.SerializeToString,
      ),
      'WaitForActorOutOfScope': grpc.unary_unary_rpc_method_handler(
          servicer.WaitForActorOutOfScope,
          request_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.WaitForActorOutOfScopeRequest.FromString,
          response_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.WaitForActorOutOfScopeReply.SerializeToString,
      ),
      'WaitForObjectEviction': grpc.unary_unary_rpc_method_handler(
          servicer.WaitForObjectEviction,
          request_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.WaitForObjectEvictionRequest.FromString,
          response_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.WaitForObjectEvictionReply.SerializeToString,
      ),
      'AddObjectLocationOwner': grpc.unary_unary_rpc_method_handler(
          servicer.AddObjectLocationOwner,
          request_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.AddObjectLocationOwnerRequest.FromString,
          response_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.AddObjectLocationOwnerReply.SerializeToString,
      ),
      'RemoveObjectLocationOwner': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveObjectLocationOwner,
          request_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.RemoveObjectLocationOwnerRequest.FromString,
          response_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.RemoveObjectLocationOwnerReply.SerializeToString,
      ),
      'GetObjectLocationsOwner': grpc.unary_unary_rpc_method_handler(
          servicer.GetObjectLocationsOwner,
          request_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.GetObjectLocationsOwnerRequest.FromString,
          response_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.GetObjectLocationsOwnerReply.SerializeToString,
      ),
      'KillActor': grpc.unary_unary_rpc_method_handler(
          servicer.KillActor,
          request_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.KillActorRequest.FromString,
          response_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.KillActorReply.SerializeToString,
      ),
      'CancelTask': grpc.unary_unary_rpc_method_handler(
          servicer.CancelTask,
          request_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.CancelTaskRequest.FromString,
          response_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.CancelTaskReply.SerializeToString,
      ),
      'RemoteCancelTask': grpc.unary_unary_rpc_method_handler(
          servicer.RemoteCancelTask,
          request_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.RemoteCancelTaskRequest.FromString,
          response_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.RemoteCancelTaskReply.SerializeToString,
      ),
      'GetCoreWorkerStats': grpc.unary_unary_rpc_method_handler(
          servicer.GetCoreWorkerStats,
          request_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.GetCoreWorkerStatsRequest.FromString,
          response_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.GetCoreWorkerStatsReply.SerializeToString,
      ),
      'WaitForRefRemoved': grpc.unary_unary_rpc_method_handler(
          servicer.WaitForRefRemoved,
          request_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.WaitForRefRemovedRequest.FromString,
          response_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.WaitForRefRemovedReply.SerializeToString,
      ),
      'LocalGC': grpc.unary_unary_rpc_method_handler(
          servicer.LocalGC,
          request_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.LocalGCRequest.FromString,
          response_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.LocalGCReply.SerializeToString,
      ),
      'SpillObjects': grpc.unary_unary_rpc_method_handler(
          servicer.SpillObjects,
          request_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.SpillObjectsRequest.FromString,
          response_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.SpillObjectsReply.SerializeToString,
      ),
      'RestoreSpilledObjects': grpc.unary_unary_rpc_method_handler(
          servicer.RestoreSpilledObjects,
          request_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.RestoreSpilledObjectsRequest.FromString,
          response_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.RestoreSpilledObjectsReply.SerializeToString,
      ),
      'DeleteSpilledObjects': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteSpilledObjects,
          request_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.DeleteSpilledObjectsRequest.FromString,
          response_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.DeleteSpilledObjectsReply.SerializeToString,
      ),
      'PlasmaObjectReady': grpc.unary_unary_rpc_method_handler(
          servicer.PlasmaObjectReady,
          request_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.PlasmaObjectReadyRequest.FromString,
          response_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.PlasmaObjectReadyReply.SerializeToString,
      ),
      'Exit': grpc.unary_unary_rpc_method_handler(
          servicer.Exit,
          request_deserializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.ExitRequest.FromString,
          response_serializer=src_dot_ray_dot_protobuf_dot_core__worker__pb2.ExitReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ray.rpc.CoreWorkerService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
