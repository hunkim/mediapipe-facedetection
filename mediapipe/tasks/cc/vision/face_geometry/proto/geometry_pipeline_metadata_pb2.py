# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/vision/face_geometry/proto/geometry_pipeline_metadata.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.tasks.cc.vision.face_geometry.proto import mesh_3d_pb2 as mediapipe_dot_tasks_dot_cc_dot_vision_dot_face__geometry_dot_proto_dot_mesh__3d__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/tasks/cc/vision/face_geometry/proto/geometry_pipeline_metadata.proto',
  package='mediapipe.tasks.vision.face_geometry.proto',
  syntax='proto2',
  serialized_options=_b('\n4com.google.mediapipe.tasks.vision.facegeometry.protoB\035GeometryPipelineMetadataProto'),
  serialized_pb=_b('\nNmediapipe/tasks/cc/vision/face_geometry/proto/geometry_pipeline_metadata.proto\x12*mediapipe.tasks.vision.face_geometry.proto\x1a;mediapipe/tasks/cc/vision/face_geometry/proto/mesh_3d.proto\":\n\x13WeightedLandmarkRef\x12\x13\n\x0blandmark_id\x18\x01 \x01(\r\x12\x0e\n\x06weight\x18\x02 \x01(\x02\"\x99\x02\n\x18GeometryPipelineMetadata\x12M\n\x0cinput_source\x18\x03 \x01(\x0e\x32\x37.mediapipe.tasks.vision.face_geometry.proto.InputSource\x12J\n\x0e\x63\x61nonical_mesh\x18\x01 \x01(\x0b\x32\x32.mediapipe.tasks.vision.face_geometry.proto.Mesh3d\x12\x62\n\x19procrustes_landmark_basis\x18\x02 \x03(\x0b\x32?.mediapipe.tasks.vision.face_geometry.proto.WeightedLandmarkRef*S\n\x0bInputSource\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x1a\n\x16\x46\x41\x43\x45_LANDMARK_PIPELINE\x10\x01\x12\x1b\n\x17\x46\x41\x43\x45_DETECTION_PIPELINE\x10\x02\x42U\n4com.google.mediapipe.tasks.vision.facegeometry.protoB\x1dGeometryPipelineMetadataProto')
  ,
  dependencies=[mediapipe_dot_tasks_dot_cc_dot_vision_dot_face__geometry_dot_proto_dot_mesh__3d__pb2.DESCRIPTOR,])

_INPUTSOURCE = _descriptor.EnumDescriptor(
  name='InputSource',
  full_name='mediapipe.tasks.vision.face_geometry.proto.InputSource',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FACE_LANDMARK_PIPELINE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FACE_DETECTION_PIPELINE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=531,
  serialized_end=614,
)
_sym_db.RegisterEnumDescriptor(_INPUTSOURCE)

InputSource = enum_type_wrapper.EnumTypeWrapper(_INPUTSOURCE)
DEFAULT = 0
FACE_LANDMARK_PIPELINE = 1
FACE_DETECTION_PIPELINE = 2



_WEIGHTEDLANDMARKREF = _descriptor.Descriptor(
  name='WeightedLandmarkRef',
  full_name='mediapipe.tasks.vision.face_geometry.proto.WeightedLandmarkRef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='landmark_id', full_name='mediapipe.tasks.vision.face_geometry.proto.WeightedLandmarkRef.landmark_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='mediapipe.tasks.vision.face_geometry.proto.WeightedLandmarkRef.weight', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=187,
  serialized_end=245,
)


_GEOMETRYPIPELINEMETADATA = _descriptor.Descriptor(
  name='GeometryPipelineMetadata',
  full_name='mediapipe.tasks.vision.face_geometry.proto.GeometryPipelineMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input_source', full_name='mediapipe.tasks.vision.face_geometry.proto.GeometryPipelineMetadata.input_source', index=0,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='canonical_mesh', full_name='mediapipe.tasks.vision.face_geometry.proto.GeometryPipelineMetadata.canonical_mesh', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='procrustes_landmark_basis', full_name='mediapipe.tasks.vision.face_geometry.proto.GeometryPipelineMetadata.procrustes_landmark_basis', index=2,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=248,
  serialized_end=529,
)

_GEOMETRYPIPELINEMETADATA.fields_by_name['input_source'].enum_type = _INPUTSOURCE
_GEOMETRYPIPELINEMETADATA.fields_by_name['canonical_mesh'].message_type = mediapipe_dot_tasks_dot_cc_dot_vision_dot_face__geometry_dot_proto_dot_mesh__3d__pb2._MESH3D
_GEOMETRYPIPELINEMETADATA.fields_by_name['procrustes_landmark_basis'].message_type = _WEIGHTEDLANDMARKREF
DESCRIPTOR.message_types_by_name['WeightedLandmarkRef'] = _WEIGHTEDLANDMARKREF
DESCRIPTOR.message_types_by_name['GeometryPipelineMetadata'] = _GEOMETRYPIPELINEMETADATA
DESCRIPTOR.enum_types_by_name['InputSource'] = _INPUTSOURCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WeightedLandmarkRef = _reflection.GeneratedProtocolMessageType('WeightedLandmarkRef', (_message.Message,), dict(
  DESCRIPTOR = _WEIGHTEDLANDMARKREF,
  __module__ = 'mediapipe.tasks.cc.vision.face_geometry.proto.geometry_pipeline_metadata_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.tasks.vision.face_geometry.proto.WeightedLandmarkRef)
  ))
_sym_db.RegisterMessage(WeightedLandmarkRef)

GeometryPipelineMetadata = _reflection.GeneratedProtocolMessageType('GeometryPipelineMetadata', (_message.Message,), dict(
  DESCRIPTOR = _GEOMETRYPIPELINEMETADATA,
  __module__ = 'mediapipe.tasks.cc.vision.face_geometry.proto.geometry_pipeline_metadata_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.tasks.vision.face_geometry.proto.GeometryPipelineMetadata)
  ))
_sym_db.RegisterMessage(GeometryPipelineMetadata)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
