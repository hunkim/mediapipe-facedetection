# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/components/processors/proto/classifier_options.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/tasks/cc/components/processors/proto/classifier_options.proto',
  package='mediapipe.tasks.components.processors.proto',
  syntax='proto2',
  serialized_options=_b('\n6com.google.mediapipe.tasks.components.processors.protoB\026ClassifierOptionsProto'),
  serialized_pb=_b('\nGmediapipe/tasks/cc/components/processors/proto/classifier_options.proto\x12+mediapipe.tasks.components.processors.proto\"\x9e\x01\n\x11\x43lassifierOptions\x12 \n\x14\x64isplay_names_locale\x18\x01 \x01(\t:\x02\x65n\x12\x17\n\x0bmax_results\x18\x02 \x01(\x05:\x02-1\x12\x17\n\x0fscore_threshold\x18\x03 \x01(\x02\x12\x1a\n\x12\x63\x61tegory_allowlist\x18\x04 \x03(\t\x12\x19\n\x11\x63\x61tegory_denylist\x18\x05 \x03(\tBP\n6com.google.mediapipe.tasks.components.processors.protoB\x16\x43lassifierOptionsProto')
)




_CLASSIFIEROPTIONS = _descriptor.Descriptor(
  name='ClassifierOptions',
  full_name='mediapipe.tasks.components.processors.proto.ClassifierOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='display_names_locale', full_name='mediapipe.tasks.components.processors.proto.ClassifierOptions.display_names_locale', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("en").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_results', full_name='mediapipe.tasks.components.processors.proto.ClassifierOptions.max_results', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score_threshold', full_name='mediapipe.tasks.components.processors.proto.ClassifierOptions.score_threshold', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category_allowlist', full_name='mediapipe.tasks.components.processors.proto.ClassifierOptions.category_allowlist', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category_denylist', full_name='mediapipe.tasks.components.processors.proto.ClassifierOptions.category_denylist', index=4,
      number=5, type=9, cpp_type=9, label=3,
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
  serialized_start=121,
  serialized_end=279,
)

DESCRIPTOR.message_types_by_name['ClassifierOptions'] = _CLASSIFIEROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClassifierOptions = _reflection.GeneratedProtocolMessageType('ClassifierOptions', (_message.Message,), dict(
  DESCRIPTOR = _CLASSIFIEROPTIONS,
  __module__ = 'mediapipe.tasks.cc.components.processors.proto.classifier_options_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.tasks.components.processors.proto.ClassifierOptions)
  ))
_sym_db.RegisterMessage(ClassifierOptions)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
