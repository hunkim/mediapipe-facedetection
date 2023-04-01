# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/image/feature_detector_calculator.proto

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
  name='mediapipe/calculators/image/feature_detector_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n=mediapipe/calculators/image/feature_detector_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xe4\x01\n FeatureDetectorCalculatorOptions\x12\x14\n\x0coutput_patch\x18\x01 \x01(\x08\x12\x19\n\x0cmax_features\x18\x02 \x01(\x05:\x03\x32\x30\x30\x12\x18\n\rpyramid_level\x18\x03 \x01(\x05:\x01\x34\x12\x19\n\x0cscale_factor\x18\x04 \x01(\x02:\x03\x31.22Z\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xb0\x85\xf5\x84\x01 \x01(\x0b\x32+.mediapipe.FeatureDetectorCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])




_FEATUREDETECTORCALCULATOROPTIONS = _descriptor.Descriptor(
  name='FeatureDetectorCalculatorOptions',
  full_name='mediapipe.FeatureDetectorCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='output_patch', full_name='mediapipe.FeatureDetectorCalculatorOptions.output_patch', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_features', full_name='mediapipe.FeatureDetectorCalculatorOptions.max_features', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=200,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pyramid_level', full_name='mediapipe.FeatureDetectorCalculatorOptions.pyramid_level', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=4,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scale_factor', full_name='mediapipe.FeatureDetectorCalculatorOptions.scale_factor', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1.2),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.FeatureDetectorCalculatorOptions.ext', index=0,
      number=278741680, type=11, cpp_type=10, label=1,
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
  serialized_start=115,
  serialized_end=343,
)

DESCRIPTOR.message_types_by_name['FeatureDetectorCalculatorOptions'] = _FEATUREDETECTORCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeatureDetectorCalculatorOptions = _reflection.GeneratedProtocolMessageType('FeatureDetectorCalculatorOptions', (_message.Message,), dict(
  DESCRIPTOR = _FEATUREDETECTORCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.image.feature_detector_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.FeatureDetectorCalculatorOptions)
  ))
_sym_db.RegisterMessage(FeatureDetectorCalculatorOptions)

_FEATUREDETECTORCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _FEATUREDETECTORCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_FEATUREDETECTORCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
