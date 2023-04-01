# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/modules/face_detection/face_detection.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.calculators.tensor import inference_calculator_pb2 as mediapipe_dot_calculators_dot_tensor_dot_inference__calculator__pb2
from mediapipe.framework import calculator_options_pb2 as mediapipe_dot_framework_dot_calculator__options__pb2
from mediapipe.gpu import gpu_origin_pb2 as mediapipe_dot_gpu_dot_gpu__origin__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/modules/face_detection/face_detection.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=_b('\n*com.google.mediapipe.modules.facedetectionB\027FaceDetectionFrontProto'),
  serialized_pb=_b('\n5mediapipe/modules/face_detection/face_detection.proto\x12\tmediapipe\x1a\x37mediapipe/calculators/tensor/inference_calculator.proto\x1a,mediapipe/framework/calculator_options.proto\x1a\x1emediapipe/gpu/gpu_origin.proto\"\xe6\x03\n\x14\x46\x61\x63\x65\x44\x65tectionOptions\x12\x12\n\nmodel_path\x18\x01 \x01(\t\x12-\n\ngpu_origin\x18\x0b \x01(\x0e\x32\x19.mediapipe.GpuOrigin.Mode\x12\x14\n\x0ctensor_width\x18\x15 \x01(\x05\x12\x15\n\rtensor_height\x18\x16 \x01(\x05\x12\x12\n\nnum_layers\x18\x17 \x01(\x05\x12\x0f\n\x07strides\x18\x18 \x03(\x05\x12*\n\x1finterpolated_scale_aspect_ratio\x18\x19 \x01(\x02:\x01\x31\x12\x11\n\tnum_boxes\x18\x1f \x01(\x05\x12\x12\n\x07x_scale\x18  \x01(\x02:\x01\x30\x12\x12\n\x07y_scale\x18! \x01(\x02:\x01\x30\x12\x12\n\x07w_scale\x18\" \x01(\x02:\x01\x30\x12\x12\n\x07h_scale\x18# \x01(\x02:\x01\x30\x12\x18\n\x10min_score_thresh\x18$ \x01(\x02\x12@\n\x08\x64\x65legate\x18\x06 \x01(\x0b\x32..mediapipe.InferenceCalculatorOptions.Delegate2N\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xee\xf3\xbc\xb2\x01 \x01(\x0b\x32\x1f.mediapipe.FaceDetectionOptionsBE\n*com.google.mediapipe.modules.facedetectionB\x17\x46\x61\x63\x65\x44\x65tectionFrontProto')
  ,
  dependencies=[mediapipe_dot_calculators_dot_tensor_dot_inference__calculator__pb2.DESCRIPTOR,mediapipe_dot_framework_dot_calculator__options__pb2.DESCRIPTOR,mediapipe_dot_gpu_dot_gpu__origin__pb2.DESCRIPTOR,])




_FACEDETECTIONOPTIONS = _descriptor.Descriptor(
  name='FaceDetectionOptions',
  full_name='mediapipe.FaceDetectionOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='model_path', full_name='mediapipe.FaceDetectionOptions.model_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gpu_origin', full_name='mediapipe.FaceDetectionOptions.gpu_origin', index=1,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tensor_width', full_name='mediapipe.FaceDetectionOptions.tensor_width', index=2,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tensor_height', full_name='mediapipe.FaceDetectionOptions.tensor_height', index=3,
      number=22, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_layers', full_name='mediapipe.FaceDetectionOptions.num_layers', index=4,
      number=23, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strides', full_name='mediapipe.FaceDetectionOptions.strides', index=5,
      number=24, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interpolated_scale_aspect_ratio', full_name='mediapipe.FaceDetectionOptions.interpolated_scale_aspect_ratio', index=6,
      number=25, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_boxes', full_name='mediapipe.FaceDetectionOptions.num_boxes', index=7,
      number=31, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='x_scale', full_name='mediapipe.FaceDetectionOptions.x_scale', index=8,
      number=32, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y_scale', full_name='mediapipe.FaceDetectionOptions.y_scale', index=9,
      number=33, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='w_scale', full_name='mediapipe.FaceDetectionOptions.w_scale', index=10,
      number=34, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='h_scale', full_name='mediapipe.FaceDetectionOptions.h_scale', index=11,
      number=35, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_score_thresh', full_name='mediapipe.FaceDetectionOptions.min_score_thresh', index=12,
      number=36, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delegate', full_name='mediapipe.FaceDetectionOptions.delegate', index=13,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.FaceDetectionOptions.ext', index=0,
      number=374290926, type=11, cpp_type=10, label=1,
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
  serialized_start=204,
  serialized_end=690,
)

_FACEDETECTIONOPTIONS.fields_by_name['gpu_origin'].enum_type = mediapipe_dot_gpu_dot_gpu__origin__pb2._GPUORIGIN_MODE
_FACEDETECTIONOPTIONS.fields_by_name['delegate'].message_type = mediapipe_dot_calculators_dot_tensor_dot_inference__calculator__pb2._INFERENCECALCULATOROPTIONS_DELEGATE
DESCRIPTOR.message_types_by_name['FaceDetectionOptions'] = _FACEDETECTIONOPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FaceDetectionOptions = _reflection.GeneratedProtocolMessageType('FaceDetectionOptions', (_message.Message,), dict(
  DESCRIPTOR = _FACEDETECTIONOPTIONS,
  __module__ = 'mediapipe.modules.face_detection.face_detection_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.FaceDetectionOptions)
  ))
_sym_db.RegisterMessage(FaceDetectionOptions)

_FACEDETECTIONOPTIONS.extensions_by_name['ext'].message_type = _FACEDETECTIONOPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_FACEDETECTIONOPTIONS.extensions_by_name['ext'])

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
