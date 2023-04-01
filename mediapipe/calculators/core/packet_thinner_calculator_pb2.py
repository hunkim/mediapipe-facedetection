# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/core/packet_thinner_calculator.proto

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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/calculators/core/packet_thinner_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n:mediapipe/calculators/core/packet_thinner_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xf3\x02\n\x1ePacketThinnerCalculatorOptions\x12R\n\x0cthinner_type\x18\x01 \x01(\x0e\x32\x35.mediapipe.PacketThinnerCalculatorOptions.ThinnerType:\x05\x41SYNC\x12\x11\n\x06period\x18\x02 \x01(\x03:\x01\x31\x12\x12\n\nstart_time\x18\x03 \x01(\x03\x12\x10\n\x08\x65nd_time\x18\x04 \x01(\x03\x12$\n\x16sync_output_timestamps\x18\x05 \x01(\x08:\x04true\x12 \n\x11update_frame_rate\x18\x06 \x01(\x08:\x05\x66\x61lse\"\"\n\x0bThinnerType\x12\t\n\x05\x41SYNC\x10\x01\x12\x08\n\x04SYNC\x10\x02\x32X\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\x84\xd8\xca\x89\x01 \x01(\x0b\x32).mediapipe.PacketThinnerCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])



_PACKETTHINNERCALCULATOROPTIONS_THINNERTYPE = _descriptor.EnumDescriptor(
  name='ThinnerType',
  full_name='mediapipe.PacketThinnerCalculatorOptions.ThinnerType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ASYNC', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYNC', index=1, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=359,
  serialized_end=393,
)
_sym_db.RegisterEnumDescriptor(_PACKETTHINNERCALCULATOROPTIONS_THINNERTYPE)


_PACKETTHINNERCALCULATOROPTIONS = _descriptor.Descriptor(
  name='PacketThinnerCalculatorOptions',
  full_name='mediapipe.PacketThinnerCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='thinner_type', full_name='mediapipe.PacketThinnerCalculatorOptions.thinner_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='period', full_name='mediapipe.PacketThinnerCalculatorOptions.period', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='mediapipe.PacketThinnerCalculatorOptions.start_time', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='mediapipe.PacketThinnerCalculatorOptions.end_time', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sync_output_timestamps', full_name='mediapipe.PacketThinnerCalculatorOptions.sync_output_timestamps', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_frame_rate', full_name='mediapipe.PacketThinnerCalculatorOptions.update_frame_rate', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.PacketThinnerCalculatorOptions.ext', index=0,
      number=288533508, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  nested_types=[],
  enum_types=[
    _PACKETTHINNERCALCULATOROPTIONS_THINNERTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=483,
)

_PACKETTHINNERCALCULATOROPTIONS.fields_by_name['thinner_type'].enum_type = _PACKETTHINNERCALCULATOROPTIONS_THINNERTYPE
_PACKETTHINNERCALCULATOROPTIONS_THINNERTYPE.containing_type = _PACKETTHINNERCALCULATOROPTIONS
DESCRIPTOR.message_types_by_name['PacketThinnerCalculatorOptions'] = _PACKETTHINNERCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PacketThinnerCalculatorOptions = _reflection.GeneratedProtocolMessageType('PacketThinnerCalculatorOptions', (_message.Message,), dict(
  DESCRIPTOR = _PACKETTHINNERCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.core.packet_thinner_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.PacketThinnerCalculatorOptions)
  ))
_sym_db.RegisterMessage(PacketThinnerCalculatorOptions)

_PACKETTHINNERCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _PACKETTHINNERCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_PACKETTHINNERCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
