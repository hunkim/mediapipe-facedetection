# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/framework/formats/affine_transform_data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/framework/formats/affine_transform_data.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n7mediapipe/framework/formats/affine_transform_data.proto\x12\tmediapipe\"#\n\x0bVector2Data\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\"\xa2\x01\n\x13\x41\x66\x66ineTransformData\x12+\n\x0btranslation\x18\x01 \x01(\x0b\x32\x16.mediapipe.Vector2Data\x12%\n\x05scale\x18\x02 \x01(\x0b\x32\x16.mediapipe.Vector2Data\x12%\n\x05shear\x18\x03 \x01(\x0b\x32\x16.mediapipe.Vector2Data\x12\x10\n\x08rotation\x18\x04 \x01(\x02')
)




_VECTOR2DATA = _descriptor.Descriptor(
  name='Vector2Data',
  full_name='mediapipe.Vector2Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='mediapipe.Vector2Data.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='mediapipe.Vector2Data.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=70,
  serialized_end=105,
)


_AFFINETRANSFORMDATA = _descriptor.Descriptor(
  name='AffineTransformData',
  full_name='mediapipe.AffineTransformData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='translation', full_name='mediapipe.AffineTransformData.translation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scale', full_name='mediapipe.AffineTransformData.scale', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shear', full_name='mediapipe.AffineTransformData.shear', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rotation', full_name='mediapipe.AffineTransformData.rotation', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=108,
  serialized_end=270,
)

_AFFINETRANSFORMDATA.fields_by_name['translation'].message_type = _VECTOR2DATA
_AFFINETRANSFORMDATA.fields_by_name['scale'].message_type = _VECTOR2DATA
_AFFINETRANSFORMDATA.fields_by_name['shear'].message_type = _VECTOR2DATA
DESCRIPTOR.message_types_by_name['Vector2Data'] = _VECTOR2DATA
DESCRIPTOR.message_types_by_name['AffineTransformData'] = _AFFINETRANSFORMDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Vector2Data = _reflection.GeneratedProtocolMessageType('Vector2Data', (_message.Message,), dict(
  DESCRIPTOR = _VECTOR2DATA,
  __module__ = 'mediapipe.framework.formats.affine_transform_data_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.Vector2Data)
  ))
_sym_db.RegisterMessage(Vector2Data)

AffineTransformData = _reflection.GeneratedProtocolMessageType('AffineTransformData', (_message.Message,), dict(
  DESCRIPTOR = _AFFINETRANSFORMDATA,
  __module__ = 'mediapipe.framework.formats.affine_transform_data_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.AffineTransformData)
  ))
_sym_db.RegisterMessage(AffineTransformData)


# @@protoc_insertion_point(module_scope)
