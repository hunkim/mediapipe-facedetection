# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/core/concatenate_vector_calculator.proto

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
  name='mediapipe/calculators/core/concatenate_vector_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n>mediapipe/calculators/core/concatenate_vector_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xaa\x01\n\"ConcatenateVectorCalculatorOptions\x12\'\n\x18only_emit_if_all_present\x18\x01 \x01(\x08:\x05\x66\x61lse2[\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xcf\xb1\xd8{ \x01(\x0b\x32-.mediapipe.ConcatenateVectorCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])




_CONCATENATEVECTORCALCULATOROPTIONS = _descriptor.Descriptor(
  name='ConcatenateVectorCalculatorOptions',
  full_name='mediapipe.ConcatenateVectorCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='only_emit_if_all_present', full_name='mediapipe.ConcatenateVectorCalculatorOptions.only_emit_if_all_present', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.ConcatenateVectorCalculatorOptions.ext', index=0,
      number=259397839, type=11, cpp_type=10, label=1,
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
  serialized_start=116,
  serialized_end=286,
)

DESCRIPTOR.message_types_by_name['ConcatenateVectorCalculatorOptions'] = _CONCATENATEVECTORCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConcatenateVectorCalculatorOptions = _reflection.GeneratedProtocolMessageType('ConcatenateVectorCalculatorOptions', (_message.Message,), dict(
  DESCRIPTOR = _CONCATENATEVECTORCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.core.concatenate_vector_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.ConcatenateVectorCalculatorOptions)
  ))
_sym_db.RegisterMessage(ConcatenateVectorCalculatorOptions)

_CONCATENATEVECTORCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _CONCATENATEVECTORCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_CONCATENATEVECTORCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
