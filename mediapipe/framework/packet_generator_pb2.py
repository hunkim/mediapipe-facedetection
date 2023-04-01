# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/framework/packet_generator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/framework/packet_generator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=_b('\n\032com.google.mediapipe.protoB\024PacketGeneratorProto'),
  serialized_pb=_b('\n*mediapipe/framework/packet_generator.proto\x12\tmediapipe\"@\n\x16PacketGeneratorOptions\x12\x1a\n\x0cmerge_fields\x18\x01 \x01(\x08:\x04true*\n\x08\xa0\x9c\x01\x10\x80\x80\x80\x80\x02\"\xcf\x01\n\x15PacketGeneratorConfig\x12\x18\n\x10packet_generator\x18\x01 \x01(\t\x12\x19\n\x11input_side_packet\x18\x02 \x03(\t\x12\x17\n\x0e\x65xternal_input\x18\xea\x07 \x03(\t\x12\x1a\n\x12output_side_packet\x18\x03 \x03(\t\x12\x18\n\x0f\x65xternal_output\x18\xeb\x07 \x03(\t\x12\x32\n\x07options\x18\x04 \x01(\x0b\x32!.mediapipe.PacketGeneratorOptionsB2\n\x1a\x63om.google.mediapipe.protoB\x14PacketGeneratorProto')
)




_PACKETGENERATOROPTIONS = _descriptor.Descriptor(
  name='PacketGeneratorOptions',
  full_name='mediapipe.PacketGeneratorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='merge_fields', full_name='mediapipe.PacketGeneratorOptions.merge_fields', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
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
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(20000, 536870912), ],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=121,
)


_PACKETGENERATORCONFIG = _descriptor.Descriptor(
  name='PacketGeneratorConfig',
  full_name='mediapipe.PacketGeneratorConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packet_generator', full_name='mediapipe.PacketGeneratorConfig.packet_generator', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input_side_packet', full_name='mediapipe.PacketGeneratorConfig.input_side_packet', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='external_input', full_name='mediapipe.PacketGeneratorConfig.external_input', index=2,
      number=1002, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_side_packet', full_name='mediapipe.PacketGeneratorConfig.output_side_packet', index=3,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='external_output', full_name='mediapipe.PacketGeneratorConfig.external_output', index=4,
      number=1003, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='mediapipe.PacketGeneratorConfig.options', index=5,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=124,
  serialized_end=331,
)

_PACKETGENERATORCONFIG.fields_by_name['options'].message_type = _PACKETGENERATOROPTIONS
DESCRIPTOR.message_types_by_name['PacketGeneratorOptions'] = _PACKETGENERATOROPTIONS
DESCRIPTOR.message_types_by_name['PacketGeneratorConfig'] = _PACKETGENERATORCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PacketGeneratorOptions = _reflection.GeneratedProtocolMessageType('PacketGeneratorOptions', (_message.Message,), dict(
  DESCRIPTOR = _PACKETGENERATOROPTIONS,
  __module__ = 'mediapipe.framework.packet_generator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.PacketGeneratorOptions)
  ))
_sym_db.RegisterMessage(PacketGeneratorOptions)

PacketGeneratorConfig = _reflection.GeneratedProtocolMessageType('PacketGeneratorConfig', (_message.Message,), dict(
  DESCRIPTOR = _PACKETGENERATORCONFIG,
  __module__ = 'mediapipe.framework.packet_generator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.PacketGeneratorConfig)
  ))
_sym_db.RegisterMessage(PacketGeneratorConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
