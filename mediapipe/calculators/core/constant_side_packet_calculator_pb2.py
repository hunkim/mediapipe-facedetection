# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/core/constant_side_packet_calculator.proto

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
from mediapipe.framework.formats import classification_pb2 as mediapipe_dot_framework_dot_formats_dot_classification__pb2
from mediapipe.framework.formats import landmark_pb2 as mediapipe_dot_framework_dot_formats_dot_landmark__pb2
from mediapipe.framework.formats import time_series_header_pb2 as mediapipe_dot_framework_dot_formats_dot_time__series__header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/calculators/core/constant_side_packet_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n@mediapipe/calculators/core/constant_side_packet_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\x1a\x30mediapipe/framework/formats/classification.proto\x1a*mediapipe/framework/formats/landmark.proto\x1a\x34mediapipe/framework/formats/time_series_header.proto\"\xbe\x04\n#ConstantSidePacketCalculatorOptions\x12Q\n\x06packet\x18\x01 \x03(\x0b\x32\x41.mediapipe.ConstantSidePacketCalculatorOptions.ConstantSidePacket\x1a\xe4\x02\n\x12\x43onstantSidePacket\x12\x13\n\tint_value\x18\x01 \x01(\x05H\x00\x12\x15\n\x0b\x66loat_value\x18\x02 \x01(\x02H\x00\x12\x14\n\nbool_value\x18\x03 \x01(\x08H\x00\x12\x16\n\x0cstring_value\x18\x04 \x01(\tH\x00\x12\x16\n\x0cuint64_value\x18\x05 \x01(\x04H\x00\x12\x42\n\x19\x63lassification_list_value\x18\x06 \x01(\x0b\x32\x1d.mediapipe.ClassificationListH\x00\x12\x36\n\x13landmark_list_value\x18\x07 \x01(\x0b\x32\x17.mediapipe.LandmarkListH\x00\x12\x16\n\x0c\x64ouble_value\x18\t \x01(\x01H\x00\x12?\n\x18time_series_header_value\x18\n \x01(\x0b\x32\x1b.mediapipe.TimeSeriesHeaderH\x00\x42\x07\n\x05value2]\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\x85\xaa\xee\x8a\x01 \x01(\x0b\x32..mediapipe.ConstantSidePacketCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,mediapipe_dot_framework_dot_formats_dot_classification__pb2.DESCRIPTOR,mediapipe_dot_framework_dot_formats_dot_landmark__pb2.DESCRIPTOR,mediapipe_dot_framework_dot_formats_dot_time__series__header__pb2.DESCRIPTOR,])




_CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET = _descriptor.Descriptor(
  name='ConstantSidePacket',
  full_name='mediapipe.ConstantSidePacketCalculatorOptions.ConstantSidePacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='int_value', full_name='mediapipe.ConstantSidePacketCalculatorOptions.ConstantSidePacket.int_value', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float_value', full_name='mediapipe.ConstantSidePacketCalculatorOptions.ConstantSidePacket.float_value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bool_value', full_name='mediapipe.ConstantSidePacketCalculatorOptions.ConstantSidePacket.bool_value', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='mediapipe.ConstantSidePacketCalculatorOptions.ConstantSidePacket.string_value', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uint64_value', full_name='mediapipe.ConstantSidePacketCalculatorOptions.ConstantSidePacket.uint64_value', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='classification_list_value', full_name='mediapipe.ConstantSidePacketCalculatorOptions.ConstantSidePacket.classification_list_value', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='landmark_list_value', full_name='mediapipe.ConstantSidePacketCalculatorOptions.ConstantSidePacket.landmark_list_value', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='double_value', full_name='mediapipe.ConstantSidePacketCalculatorOptions.ConstantSidePacket.double_value', index=7,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_series_header_value', full_name='mediapipe.ConstantSidePacketCalculatorOptions.ConstantSidePacket.time_series_header_value', index=8,
      number=10, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='value', full_name='mediapipe.ConstantSidePacketCalculatorOptions.ConstantSidePacket.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=389,
  serialized_end=745,
)

_CONSTANTSIDEPACKETCALCULATOROPTIONS = _descriptor.Descriptor(
  name='ConstantSidePacketCalculatorOptions',
  full_name='mediapipe.ConstantSidePacketCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packet', full_name='mediapipe.ConstantSidePacketCalculatorOptions.packet', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.ConstantSidePacketCalculatorOptions.ext', index=0,
      number=291214597, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  nested_types=[_CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=266,
  serialized_end=840,
)

_CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.fields_by_name['classification_list_value'].message_type = mediapipe_dot_framework_dot_formats_dot_classification__pb2._CLASSIFICATIONLIST
_CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.fields_by_name['landmark_list_value'].message_type = mediapipe_dot_framework_dot_formats_dot_landmark__pb2._LANDMARKLIST
_CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.fields_by_name['time_series_header_value'].message_type = mediapipe_dot_framework_dot_formats_dot_time__series__header__pb2._TIMESERIESHEADER
_CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.containing_type = _CONSTANTSIDEPACKETCALCULATOROPTIONS
_CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.oneofs_by_name['value'].fields.append(
  _CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.fields_by_name['int_value'])
_CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.fields_by_name['int_value'].containing_oneof = _CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.oneofs_by_name['value']
_CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.oneofs_by_name['value'].fields.append(
  _CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.fields_by_name['float_value'])
_CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.fields_by_name['float_value'].containing_oneof = _CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.oneofs_by_name['value']
_CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.oneofs_by_name['value'].fields.append(
  _CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.fields_by_name['bool_value'])
_CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.fields_by_name['bool_value'].containing_oneof = _CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.oneofs_by_name['value']
_CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.oneofs_by_name['value'].fields.append(
  _CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.fields_by_name['string_value'])
_CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.fields_by_name['string_value'].containing_oneof = _CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.oneofs_by_name['value']
_CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.oneofs_by_name['value'].fields.append(
  _CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.fields_by_name['uint64_value'])
_CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.fields_by_name['uint64_value'].containing_oneof = _CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.oneofs_by_name['value']
_CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.oneofs_by_name['value'].fields.append(
  _CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.fields_by_name['classification_list_value'])
_CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.fields_by_name['classification_list_value'].containing_oneof = _CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.oneofs_by_name['value']
_CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.oneofs_by_name['value'].fields.append(
  _CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.fields_by_name['landmark_list_value'])
_CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.fields_by_name['landmark_list_value'].containing_oneof = _CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.oneofs_by_name['value']
_CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.oneofs_by_name['value'].fields.append(
  _CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.fields_by_name['double_value'])
_CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.fields_by_name['double_value'].containing_oneof = _CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.oneofs_by_name['value']
_CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.oneofs_by_name['value'].fields.append(
  _CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.fields_by_name['time_series_header_value'])
_CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.fields_by_name['time_series_header_value'].containing_oneof = _CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET.oneofs_by_name['value']
_CONSTANTSIDEPACKETCALCULATOROPTIONS.fields_by_name['packet'].message_type = _CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET
DESCRIPTOR.message_types_by_name['ConstantSidePacketCalculatorOptions'] = _CONSTANTSIDEPACKETCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConstantSidePacketCalculatorOptions = _reflection.GeneratedProtocolMessageType('ConstantSidePacketCalculatorOptions', (_message.Message,), dict(

  ConstantSidePacket = _reflection.GeneratedProtocolMessageType('ConstantSidePacket', (_message.Message,), dict(
    DESCRIPTOR = _CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET,
    __module__ = 'mediapipe.calculators.core.constant_side_packet_calculator_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.ConstantSidePacketCalculatorOptions.ConstantSidePacket)
    ))
  ,
  DESCRIPTOR = _CONSTANTSIDEPACKETCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.core.constant_side_packet_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.ConstantSidePacketCalculatorOptions)
  ))
_sym_db.RegisterMessage(ConstantSidePacketCalculatorOptions)
_sym_db.RegisterMessage(ConstantSidePacketCalculatorOptions.ConstantSidePacket)

_CONSTANTSIDEPACKETCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _CONSTANTSIDEPACKETCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_CONSTANTSIDEPACKETCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
