# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/vision/face_landmarker/proto/face_blendshapes_graph_options.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
try:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
except AttributeError:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe.framework.calculator_options_pb2
from mediapipe.framework import calculator_options_pb2 as mediapipe_dot_framework_dot_calculator__options__pb2
from mediapipe.tasks.cc.core.proto import base_options_pb2 as mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/tasks/cc/vision/face_landmarker/proto/face_blendshapes_graph_options.proto',
  package='mediapipe.tasks.vision.face_landmarker.proto',
  syntax='proto2',
  serialized_options=_b('\n6com.google.mediapipe.tasks.vision.facelandmarker.protoB FaceBlendshapesGraphOptionsProto'),
  serialized_pb=_b('\nTmediapipe/tasks/cc/vision/face_landmarker/proto/face_blendshapes_graph_options.proto\x12,mediapipe.tasks.vision.face_landmarker.proto\x1a$mediapipe/framework/calculator.proto\x1a,mediapipe/framework/calculator_options.proto\x1a\x30mediapipe/tasks/cc/core/proto/base_options.proto\"\xd6\x01\n\x1b\x46\x61\x63\x65\x42lendshapesGraphOptions\x12=\n\x0c\x62\x61se_options\x18\x01 \x01(\x0b\x32\'.mediapipe.tasks.core.proto.BaseOptions2x\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\x88\xe4\xd9\xf2\x01 \x01(\x0b\x32I.mediapipe.tasks.vision.face_landmarker.proto.FaceBlendshapesGraphOptionsBZ\n6com.google.mediapipe.tasks.vision.facelandmarker.protoB FaceBlendshapesGraphOptionsProto')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,mediapipe_dot_framework_dot_calculator__options__pb2.DESCRIPTOR,mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2.DESCRIPTOR,])




_FACEBLENDSHAPESGRAPHOPTIONS = _descriptor.Descriptor(
  name='FaceBlendshapesGraphOptions',
  full_name='mediapipe.tasks.vision.face_landmarker.proto.FaceBlendshapesGraphOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_options', full_name='mediapipe.tasks.vision.face_landmarker.proto.FaceBlendshapesGraphOptions.base_options', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.tasks.vision.face_landmarker.proto.FaceBlendshapesGraphOptions.ext', index=0,
      number=508981768, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=269,
  serialized_end=483,
)

_FACEBLENDSHAPESGRAPHOPTIONS.fields_by_name['base_options'].message_type = mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2._BASEOPTIONS
DESCRIPTOR.message_types_by_name['FaceBlendshapesGraphOptions'] = _FACEBLENDSHAPESGRAPHOPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FaceBlendshapesGraphOptions = _reflection.GeneratedProtocolMessageType('FaceBlendshapesGraphOptions', (_message.Message,), dict(
  DESCRIPTOR = _FACEBLENDSHAPESGRAPHOPTIONS,
  __module__ = 'mediapipe.tasks.cc.vision.face_landmarker.proto.face_blendshapes_graph_options_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.tasks.vision.face_landmarker.proto.FaceBlendshapesGraphOptions)
  ))
_sym_db.RegisterMessage(FaceBlendshapesGraphOptions)

_FACEBLENDSHAPESGRAPHOPTIONS.extensions_by_name['ext'].message_type = _FACEBLENDSHAPESGRAPHOPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_FACEBLENDSHAPESGRAPHOPTIONS.extensions_by_name['ext'])

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
