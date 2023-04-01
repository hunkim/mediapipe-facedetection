# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/framework/stream_handler.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import mediapipe_options_pb2 as mediapipe_dot_framework_dot_mediapipe__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/framework/stream_handler.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=_b('\n\032com.google.mediapipe.protoB\022StreamHandlerProto'),
  serialized_pb=_b('\n(mediapipe/framework/stream_handler.proto\x12\tmediapipe\x1a+mediapipe/framework/mediapipe_options.proto\"\x81\x01\n\x18InputStreamHandlerConfig\x12\x37\n\x14input_stream_handler\x18\x01 \x01(\t:\x19\x44\x65\x66\x61ultInputStreamHandler\x12,\n\x07options\x18\x03 \x01(\x0b\x32\x1b.mediapipe.MediaPipeOptions\"\x9f\x01\n\x19OutputStreamHandlerConfig\x12\x39\n\x15output_stream_handler\x18\x01 \x01(\t:\x1aInOrderOutputStreamHandler\x12\x19\n\x11input_side_packet\x18\x02 \x03(\t\x12,\n\x07options\x18\x03 \x01(\x0b\x32\x1b.mediapipe.MediaPipeOptionsB0\n\x1a\x63om.google.mediapipe.protoB\x12StreamHandlerProto')
  ,
  dependencies=[mediapipe_dot_framework_dot_mediapipe__options__pb2.DESCRIPTOR,])




_INPUTSTREAMHANDLERCONFIG = _descriptor.Descriptor(
  name='InputStreamHandlerConfig',
  full_name='mediapipe.InputStreamHandlerConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input_stream_handler', full_name='mediapipe.InputStreamHandlerConfig.input_stream_handler', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("DefaultInputStreamHandler").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='mediapipe.InputStreamHandlerConfig.options', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=101,
  serialized_end=230,
)


_OUTPUTSTREAMHANDLERCONFIG = _descriptor.Descriptor(
  name='OutputStreamHandlerConfig',
  full_name='mediapipe.OutputStreamHandlerConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='output_stream_handler', full_name='mediapipe.OutputStreamHandlerConfig.output_stream_handler', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("InOrderOutputStreamHandler").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input_side_packet', full_name='mediapipe.OutputStreamHandlerConfig.input_side_packet', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='mediapipe.OutputStreamHandlerConfig.options', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=233,
  serialized_end=392,
)

_INPUTSTREAMHANDLERCONFIG.fields_by_name['options'].message_type = mediapipe_dot_framework_dot_mediapipe__options__pb2._MEDIAPIPEOPTIONS
_OUTPUTSTREAMHANDLERCONFIG.fields_by_name['options'].message_type = mediapipe_dot_framework_dot_mediapipe__options__pb2._MEDIAPIPEOPTIONS
DESCRIPTOR.message_types_by_name['InputStreamHandlerConfig'] = _INPUTSTREAMHANDLERCONFIG
DESCRIPTOR.message_types_by_name['OutputStreamHandlerConfig'] = _OUTPUTSTREAMHANDLERCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InputStreamHandlerConfig = _reflection.GeneratedProtocolMessageType('InputStreamHandlerConfig', (_message.Message,), dict(
  DESCRIPTOR = _INPUTSTREAMHANDLERCONFIG,
  __module__ = 'mediapipe.framework.stream_handler_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.InputStreamHandlerConfig)
  ))
_sym_db.RegisterMessage(InputStreamHandlerConfig)

OutputStreamHandlerConfig = _reflection.GeneratedProtocolMessageType('OutputStreamHandlerConfig', (_message.Message,), dict(
  DESCRIPTOR = _OUTPUTSTREAMHANDLERCONFIG,
  __module__ = 'mediapipe.framework.stream_handler_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.OutputStreamHandlerConfig)
  ))
_sym_db.RegisterMessage(OutputStreamHandlerConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
