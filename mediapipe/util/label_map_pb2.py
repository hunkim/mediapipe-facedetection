# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/util/label_map.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/util/label_map.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=_b('\n\037com.google.mediapipe.util.protoB\rLabelMapProto'),
  serialized_pb=_b('\n\x1emediapipe/util/label_map.proto\x12\tmediapipe\"F\n\x0cLabelMapItem\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x12\n\nchild_name\x18\x03 \x03(\tB0\n\x1f\x63om.google.mediapipe.util.protoB\rLabelMapProto')
)




_LABELMAPITEM = _descriptor.Descriptor(
  name='LabelMapItem',
  full_name='mediapipe.LabelMapItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mediapipe.LabelMapItem.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='mediapipe.LabelMapItem.display_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='child_name', full_name='mediapipe.LabelMapItem.child_name', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=45,
  serialized_end=115,
)

DESCRIPTOR.message_types_by_name['LabelMapItem'] = _LABELMAPITEM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LabelMapItem = _reflection.GeneratedProtocolMessageType('LabelMapItem', (_message.Message,), dict(
  DESCRIPTOR = _LABELMAPITEM,
  __module__ = 'mediapipe.util.label_map_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.LabelMapItem)
  ))
_sym_db.RegisterMessage(LabelMapItem)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
