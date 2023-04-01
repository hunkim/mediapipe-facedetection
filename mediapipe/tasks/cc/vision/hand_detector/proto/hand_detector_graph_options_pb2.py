# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/vision/hand_detector/proto/hand_detector_graph_options.proto

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
  name='mediapipe/tasks/cc/vision/hand_detector/proto/hand_detector_graph_options.proto',
  package='mediapipe.tasks.vision.hand_detector.proto',
  syntax='proto2',
  serialized_options=_b('\n4com.google.mediapipe.tasks.vision.handdetector.protoB\035HandDetectorGraphOptionsProto'),
  serialized_pb=_b('\nOmediapipe/tasks/cc/vision/hand_detector/proto/hand_detector_graph_options.proto\x12*mediapipe.tasks.vision.hand_detector.proto\x1a$mediapipe/framework/calculator.proto\x1a,mediapipe/framework/calculator_options.proto\x1a\x30mediapipe/tasks/cc/core/proto/base_options.proto\"\x88\x02\n\x18HandDetectorGraphOptions\x12=\n\x0c\x62\x61se_options\x18\x01 \x01(\x0b\x32\'.mediapipe.tasks.core.proto.BaseOptions\x12%\n\x18min_detection_confidence\x18\x02 \x01(\x02:\x03\x30.5\x12\x11\n\tnum_hands\x18\x03 \x01(\x05\x32s\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xa0\x88\xd5\xdd\x01 \x01(\x0b\x32\x44.mediapipe.tasks.vision.hand_detector.proto.HandDetectorGraphOptionsBU\n4com.google.mediapipe.tasks.vision.handdetector.protoB\x1dHandDetectorGraphOptionsProto')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,mediapipe_dot_framework_dot_calculator__options__pb2.DESCRIPTOR,mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2.DESCRIPTOR,])




_HANDDETECTORGRAPHOPTIONS = _descriptor.Descriptor(
  name='HandDetectorGraphOptions',
  full_name='mediapipe.tasks.vision.hand_detector.proto.HandDetectorGraphOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_options', full_name='mediapipe.tasks.vision.hand_detector.proto.HandDetectorGraphOptions.base_options', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_detection_confidence', full_name='mediapipe.tasks.vision.hand_detector.proto.HandDetectorGraphOptions.min_detection_confidence', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.5),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_hands', full_name='mediapipe.tasks.vision.hand_detector.proto.HandDetectorGraphOptions.num_hands', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.tasks.vision.hand_detector.proto.HandDetectorGraphOptions.ext', index=0,
      number=464864288, type=11, cpp_type=10, label=1,
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
  serialized_start=262,
  serialized_end=526,
)

_HANDDETECTORGRAPHOPTIONS.fields_by_name['base_options'].message_type = mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2._BASEOPTIONS
DESCRIPTOR.message_types_by_name['HandDetectorGraphOptions'] = _HANDDETECTORGRAPHOPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HandDetectorGraphOptions = _reflection.GeneratedProtocolMessageType('HandDetectorGraphOptions', (_message.Message,), dict(
  DESCRIPTOR = _HANDDETECTORGRAPHOPTIONS,
  __module__ = 'mediapipe.tasks.cc.vision.hand_detector.proto.hand_detector_graph_options_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.tasks.vision.hand_detector.proto.HandDetectorGraphOptions)
  ))
_sym_db.RegisterMessage(HandDetectorGraphOptions)

_HANDDETECTORGRAPHOPTIONS.extensions_by_name['ext'].message_type = _HANDDETECTORGRAPHOPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_HANDDETECTORGRAPHOPTIONS.extensions_by_name['ext'])

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
