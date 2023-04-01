# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/tensor/tensors_to_audio_calculator.proto

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
  name='mediapipe/calculators/tensor/tensors_to_audio_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n>mediapipe/calculators/tensor/tensors_to_audio_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xbd\x03\n\x1fTensorsToAudioCalculatorOptions\x12\x10\n\x08\x66\x66t_size\x18\x01 \x01(\x03\x12\x13\n\x0bnum_samples\x18\x02 \x01(\x03\x12\"\n\x17num_overlapping_samples\x18\x03 \x01(\x03:\x01\x30\x12\x63\n\x11\x64\x66t_tensor_format\x18\x0b \x01(\x0e\x32:.mediapipe.TensorsToAudioCalculatorOptions.DftTensorFormat:\x0cWITH_NYQUIST\x12\x16\n\x0evolume_gain_db\x18\x0c \x01(\x01\"w\n\x0f\x44\x66tTensorFormat\x12\x1d\n\x19\x44\x46T_TENSOR_FORMAT_UNKNOWN\x10\x00\x12\x1a\n\x16WITHOUT_DC_AND_NYQUIST\x10\x01\x12\x10\n\x0cWITH_NYQUIST\x10\x02\x12\x17\n\x13WITH_DC_AND_NYQUIST\x10\x03\x32Y\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xb0\x93\xf7\xe6\x01 \x01(\x0b\x32*.mediapipe.TensorsToAudioCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])



_TENSORSTOAUDIOCALCULATOROPTIONS_DFTTENSORFORMAT = _descriptor.EnumDescriptor(
  name='DftTensorFormat',
  full_name='mediapipe.TensorsToAudioCalculatorOptions.DftTensorFormat',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DFT_TENSOR_FORMAT_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WITHOUT_DC_AND_NYQUIST', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WITH_NYQUIST', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WITH_DC_AND_NYQUIST', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=351,
  serialized_end=470,
)
_sym_db.RegisterEnumDescriptor(_TENSORSTOAUDIOCALCULATOROPTIONS_DFTTENSORFORMAT)


_TENSORSTOAUDIOCALCULATOROPTIONS = _descriptor.Descriptor(
  name='TensorsToAudioCalculatorOptions',
  full_name='mediapipe.TensorsToAudioCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fft_size', full_name='mediapipe.TensorsToAudioCalculatorOptions.fft_size', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_samples', full_name='mediapipe.TensorsToAudioCalculatorOptions.num_samples', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_overlapping_samples', full_name='mediapipe.TensorsToAudioCalculatorOptions.num_overlapping_samples', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dft_tensor_format', full_name='mediapipe.TensorsToAudioCalculatorOptions.dft_tensor_format', index=3,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volume_gain_db', full_name='mediapipe.TensorsToAudioCalculatorOptions.volume_gain_db', index=4,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.TensorsToAudioCalculatorOptions.ext', index=0,
      number=484297136, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  nested_types=[],
  enum_types=[
    _TENSORSTOAUDIOCALCULATOROPTIONS_DFTTENSORFORMAT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=561,
)

_TENSORSTOAUDIOCALCULATOROPTIONS.fields_by_name['dft_tensor_format'].enum_type = _TENSORSTOAUDIOCALCULATOROPTIONS_DFTTENSORFORMAT
_TENSORSTOAUDIOCALCULATOROPTIONS_DFTTENSORFORMAT.containing_type = _TENSORSTOAUDIOCALCULATOROPTIONS
DESCRIPTOR.message_types_by_name['TensorsToAudioCalculatorOptions'] = _TENSORSTOAUDIOCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TensorsToAudioCalculatorOptions = _reflection.GeneratedProtocolMessageType('TensorsToAudioCalculatorOptions', (_message.Message,), dict(
  DESCRIPTOR = _TENSORSTOAUDIOCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.tensor.tensors_to_audio_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.TensorsToAudioCalculatorOptions)
  ))
_sym_db.RegisterMessage(TensorsToAudioCalculatorOptions)

_TENSORSTOAUDIOCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _TENSORSTOAUDIOCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_TENSORSTOAUDIOCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
