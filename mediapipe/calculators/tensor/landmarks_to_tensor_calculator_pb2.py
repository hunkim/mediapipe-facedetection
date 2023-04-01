# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/tensor/landmarks_to_tensor_calculator.proto

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
  name='mediapipe/calculators/tensor/landmarks_to_tensor_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\nAmediapipe/calculators/tensor/landmarks_to_tensor_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xa7\x02\n\"LandmarksToTensorCalculatorOptions\x12K\n\nattributes\x18\x01 \x03(\x0e\x32\x37.mediapipe.LandmarksToTensorCalculatorOptions.Attribute\x12\x16\n\x07\x66latten\x18\x02 \x01(\x08:\x05\x66\x61lse\">\n\tAttribute\x12\x05\n\x01X\x10\x00\x12\x05\n\x01Y\x10\x01\x12\x05\n\x01Z\x10\x02\x12\x0e\n\nVISIBILITY\x10\x03\x12\x0c\n\x08PRESENCE\x10\x04\x32\\\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xfb\xa6\xa1\xbc\x01 \x01(\x0b\x32-.mediapipe.LandmarksToTensorCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])



_LANDMARKSTOTENSORCALCULATOROPTIONS_ATTRIBUTE = _descriptor.EnumDescriptor(
  name='Attribute',
  full_name='mediapipe.LandmarksToTensorCalculatorOptions.Attribute',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='X', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Y', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Z', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VISIBILITY', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRESENCE', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=258,
  serialized_end=320,
)
_sym_db.RegisterEnumDescriptor(_LANDMARKSTOTENSORCALCULATOROPTIONS_ATTRIBUTE)


_LANDMARKSTOTENSORCALCULATOROPTIONS = _descriptor.Descriptor(
  name='LandmarksToTensorCalculatorOptions',
  full_name='mediapipe.LandmarksToTensorCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attributes', full_name='mediapipe.LandmarksToTensorCalculatorOptions.attributes', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flatten', full_name='mediapipe.LandmarksToTensorCalculatorOptions.flatten', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.LandmarksToTensorCalculatorOptions.ext', index=0,
      number=394810235, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  nested_types=[],
  enum_types=[
    _LANDMARKSTOTENSORCALCULATOROPTIONS_ATTRIBUTE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=414,
)

_LANDMARKSTOTENSORCALCULATOROPTIONS.fields_by_name['attributes'].enum_type = _LANDMARKSTOTENSORCALCULATOROPTIONS_ATTRIBUTE
_LANDMARKSTOTENSORCALCULATOROPTIONS_ATTRIBUTE.containing_type = _LANDMARKSTOTENSORCALCULATOROPTIONS
DESCRIPTOR.message_types_by_name['LandmarksToTensorCalculatorOptions'] = _LANDMARKSTOTENSORCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LandmarksToTensorCalculatorOptions = _reflection.GeneratedProtocolMessageType('LandmarksToTensorCalculatorOptions', (_message.Message,), dict(
  DESCRIPTOR = _LANDMARKSTOTENSORCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.tensor.landmarks_to_tensor_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.LandmarksToTensorCalculatorOptions)
  ))
_sym_db.RegisterMessage(LandmarksToTensorCalculatorOptions)

_LANDMARKSTOTENSORCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _LANDMARKSTOTENSORCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_LANDMARKSTOTENSORCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
