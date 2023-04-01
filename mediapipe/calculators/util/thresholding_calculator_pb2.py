# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/util/thresholding_calculator.proto

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
  name='mediapipe/calculators/util/thresholding_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n8mediapipe/calculators/util/thresholding_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\x8a\x01\n\x1dThresholdingCalculatorOptions\x12\x11\n\tthreshold\x18\x01 \x01(\x01\x32V\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xe2\xc7\xfc{ \x01(\x0b\x32(.mediapipe.ThresholdingCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])




_THRESHOLDINGCALCULATOROPTIONS = _descriptor.Descriptor(
  name='ThresholdingCalculatorOptions',
  full_name='mediapipe.ThresholdingCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='threshold', full_name='mediapipe.ThresholdingCalculatorOptions.threshold', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.ThresholdingCalculatorOptions.ext', index=0,
      number=259990498, type=11, cpp_type=10, label=1,
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
  serialized_start=110,
  serialized_end=248,
)

DESCRIPTOR.message_types_by_name['ThresholdingCalculatorOptions'] = _THRESHOLDINGCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ThresholdingCalculatorOptions = _reflection.GeneratedProtocolMessageType('ThresholdingCalculatorOptions', (_message.Message,), dict(
  DESCRIPTOR = _THRESHOLDINGCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.util.thresholding_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.ThresholdingCalculatorOptions)
  ))
_sym_db.RegisterMessage(ThresholdingCalculatorOptions)

_THRESHOLDINGCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _THRESHOLDINGCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_THRESHOLDINGCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
