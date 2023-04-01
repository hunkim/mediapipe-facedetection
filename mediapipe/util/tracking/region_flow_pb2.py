# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/util/tracking/region_flow.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/util/tracking/region_flow.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=_b('\n\035com.google.mediapipe.trackingP\001'),
  serialized_pb=_b('\n)mediapipe/util/tracking/region_flow.proto\x12\tmediapipe\"\x1f\n\x0fPatchDescriptor\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x02\"\'\n\x17\x42inaryFeatureDescriptor\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"D\n\x15TemporalIRLSSmoothing\x12\x15\n\nweight_sum\x18\x01 \x01(\x02:\x01\x30\x12\x14\n\tvalue_sum\x18\x02 \x01(\x02:\x01\x30\"\x99\x04\n\x11RegionFlowFeature\x12\x0c\n\x01x\x18\x01 \x01(\x02:\x01\x30\x12\x0c\n\x01y\x18\x02 \x01(\x02:\x01\x30\x12\r\n\x02\x64x\x18\x03 \x01(\x02:\x01\x30\x12\r\n\x02\x64y\x18\x04 \x01(\x02:\x01\x30\x12\x14\n\x08track_id\x18\r \x01(\x05:\x02-1\x12\x19\n\x0etracking_error\x18\x05 \x01(\x02:\x01\x30\x12\x16\n\x0birls_weight\x18\x06 \x01(\x02:\x01\x31\x12\x1a\n\x0f\x63orner_response\x18\x0b \x01(\x02:\x01\x30\x12\x36\n\x12\x66\x65\x61ture_descriptor\x18\x07 \x01(\x0b\x32\x1a.mediapipe.PatchDescriptor\x12<\n\x18\x66\x65\x61ture_match_descriptor\x18\x08 \x01(\x0b\x32\x1a.mediapipe.PatchDescriptor\x12\x37\n\rinternal_irls\x18\n \x01(\x0b\x32 .mediapipe.TemporalIRLSSmoothing\x12\r\n\x05label\x18\x0e \x01(\t\x12\r\n\x05\x66lags\x18\x0f \x01(\x05\x12\x12\n\nfeature_id\x18\x10 \x01(\x05\x12\x11\n\x06octave\x18\x11 \x01(\x05:\x01\x30\x12\x45\n\x19\x62inary_feature_descriptor\x18\x12 \x01(\x0b\x32\".mediapipe.BinaryFeatureDescriptor\"\x1e\n\x05\x46lags\x12\x15\n\x11\x46LAG_BROKEN_TRACK\x10\x01*\x04\x08\t\x10\n*\x04\x08\x0c\x10\r\"\xbd\x04\n\x0fRegionFlowFrame\x12:\n\x0bregion_flow\x18\x01 \x03(\x0b\x32%.mediapipe.RegionFlowFrame.RegionFlow\x12\x1d\n\x12num_total_features\x18\x02 \x01(\x05:\x01\x30\x12\x1d\n\x0eunstable_frame\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x12\n\nblur_score\x18\x07 \x01(\x02\x12\x13\n\x0b\x66rame_width\x18\x08 \x01(\x05\x12\x14\n\x0c\x66rame_height\x18\t \x01(\x05\x12\x44\n\x10\x62lock_descriptor\x18\n \x01(\x0b\x32*.mediapipe.RegionFlowFrame.BlockDescriptor\x1a\xa8\x01\n\nRegionFlow\x12\x11\n\tregion_id\x18\x01 \x02(\x05\x12\x15\n\ncentroid_x\x18\x02 \x01(\x02:\x01\x30\x12\x15\n\ncentroid_y\x18\x03 \x01(\x02:\x01\x30\x12\x11\n\x06\x66low_x\x18\x04 \x01(\x02:\x01\x30\x12\x11\n\x06\x66low_y\x18\x05 \x01(\x02:\x01\x30\x12-\n\x07\x66\x65\x61ture\x18\x07 \x03(\x0b\x32\x1c.mediapipe.RegionFlowFeature*\x04\x08\x06\x10\x07\x1an\n\x0f\x42lockDescriptor\x12\x13\n\x0b\x62lock_width\x18\x01 \x01(\x05\x12\x14\n\x0c\x62lock_height\x18\x02 \x01(\x05\x12\x17\n\x0cnum_blocks_x\x18\x03 \x01(\x05:\x01\x30\x12\x17\n\x0cnum_blocks_y\x18\x04 \x01(\x05:\x01\x30*\x04\x08\x03\x10\x04*\x04\x08\x05\x10\x06*\x04\x08\x06\x10\x07\"\x9c\x03\n\x15RegionFlowFeatureList\x12-\n\x07\x66\x65\x61ture\x18\x01 \x03(\x0b\x32\x1c.mediapipe.RegionFlowFeature\x12\x13\n\x0b\x66rame_width\x18\x02 \x01(\x05\x12\x14\n\x0c\x66rame_height\x18\x03 \x01(\x05\x12\x17\n\x08unstable\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x1f\n\x14\x64istance_from_border\x18\x05 \x01(\x05:\x01\x30\x12\x12\n\nblur_score\x18\x06 \x01(\x02\x12\x1a\n\x0blong_tracks\x18\x07 \x01(\x08:\x05\x66\x61lse\x12&\n\x1b\x66rac_long_features_rejected\x18\x08 \x01(\x02:\x01\x30\x12\x1e\n\x12visual_consistency\x18\t \x01(\x02:\x02-1\x12\x19\n\x0etimestamp_usec\x18\n \x01(\x03:\x01\x30\x12\x16\n\x0bmatch_frame\x18\x0b \x01(\x05:\x01\x30\x12\x1c\n\ris_duplicated\x18\x0c \x01(\x08:\x05\x66\x61lse\x12&\n\x1e\x61\x63tively_discarded_tracked_ids\x18\r \x03(\x05\"\x80\x03\n\x0cSalientPoint\x12\x17\n\x0cnorm_point_x\x18\x01 \x01(\x02:\x01\x30\x12\x17\n\x0cnorm_point_y\x18\x02 \x01(\x02:\x01\x30\x12\x44\n\x04type\x18\x0b \x01(\x0e\x32(.mediapipe.SalientPoint.SalientPointType:\x0cTYPE_INCLUDE\x12\x11\n\x04left\x18\x03 \x01(\x02:\x03\x30.3\x12\x13\n\x06\x62ottom\x18\x04 \x01(\x02:\x03\x30.3\x12\x12\n\x05right\x18\t \x01(\x02:\x03\x30.3\x12\x10\n\x03top\x18\n \x01(\x02:\x03\x30.3\x12\x12\n\x06weight\x18\x05 \x01(\x02:\x02\x31\x35\x12\x12\n\nnorm_major\x18\x06 \x01(\x02\x12\x12\n\nnorm_minor\x18\x07 \x01(\x02\x12\r\n\x05\x61ngle\x18\x08 \x01(\x02\"S\n\x10SalientPointType\x12\x10\n\x0cTYPE_INCLUDE\x10\x01\x12\x15\n\x11TYPE_EXCLUDE_LEFT\x10\x02\x12\x16\n\x12TYPE_EXCLUDE_RIGHT\x10\x03*\n\x08\xa0\x9c\x01\x10\x80\x80\x80\x80\x02\"G\n\x11SalientPointFrame\x12&\n\x05point\x18\x01 \x03(\x0b\x32\x17.mediapipe.SalientPoint*\n\x08\xa0\x9c\x01\x10\x80\x80\x80\x80\x02\x42!\n\x1d\x63om.google.mediapipe.trackingP\x01')
)



_REGIONFLOWFEATURE_FLAGS = _descriptor.EnumDescriptor(
  name='Flags',
  full_name='mediapipe.RegionFlowFeature.Flags',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FLAG_BROKEN_TRACK', index=0, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=696,
  serialized_end=726,
)
_sym_db.RegisterEnumDescriptor(_REGIONFLOWFEATURE_FLAGS)

_SALIENTPOINT_SALIENTPOINTTYPE = _descriptor.EnumDescriptor(
  name='SalientPointType',
  full_name='mediapipe.SalientPoint.SalientPointType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TYPE_INCLUDE', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_EXCLUDE_LEFT', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_EXCLUDE_RIGHT', index=2, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2021,
  serialized_end=2104,
)
_sym_db.RegisterEnumDescriptor(_SALIENTPOINT_SALIENTPOINTTYPE)


_PATCHDESCRIPTOR = _descriptor.Descriptor(
  name='PatchDescriptor',
  full_name='mediapipe.PatchDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='mediapipe.PatchDescriptor.data', index=0,
      number=1, type=2, cpp_type=6, label=3,
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
  serialized_start=56,
  serialized_end=87,
)


_BINARYFEATUREDESCRIPTOR = _descriptor.Descriptor(
  name='BinaryFeatureDescriptor',
  full_name='mediapipe.BinaryFeatureDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='mediapipe.BinaryFeatureDescriptor.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=89,
  serialized_end=128,
)


_TEMPORALIRLSSMOOTHING = _descriptor.Descriptor(
  name='TemporalIRLSSmoothing',
  full_name='mediapipe.TemporalIRLSSmoothing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='weight_sum', full_name='mediapipe.TemporalIRLSSmoothing.weight_sum', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value_sum', full_name='mediapipe.TemporalIRLSSmoothing.value_sum', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
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
  serialized_start=130,
  serialized_end=198,
)


_REGIONFLOWFEATURE = _descriptor.Descriptor(
  name='RegionFlowFeature',
  full_name='mediapipe.RegionFlowFeature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='mediapipe.RegionFlowFeature.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='mediapipe.RegionFlowFeature.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dx', full_name='mediapipe.RegionFlowFeature.dx', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dy', full_name='mediapipe.RegionFlowFeature.dy', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='track_id', full_name='mediapipe.RegionFlowFeature.track_id', index=4,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tracking_error', full_name='mediapipe.RegionFlowFeature.tracking_error', index=5,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='irls_weight', full_name='mediapipe.RegionFlowFeature.irls_weight', index=6,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='corner_response', full_name='mediapipe.RegionFlowFeature.corner_response', index=7,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature_descriptor', full_name='mediapipe.RegionFlowFeature.feature_descriptor', index=8,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature_match_descriptor', full_name='mediapipe.RegionFlowFeature.feature_match_descriptor', index=9,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='internal_irls', full_name='mediapipe.RegionFlowFeature.internal_irls', index=10,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label', full_name='mediapipe.RegionFlowFeature.label', index=11,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flags', full_name='mediapipe.RegionFlowFeature.flags', index=12,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature_id', full_name='mediapipe.RegionFlowFeature.feature_id', index=13,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='octave', full_name='mediapipe.RegionFlowFeature.octave', index=14,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='binary_feature_descriptor', full_name='mediapipe.RegionFlowFeature.binary_feature_descriptor', index=15,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REGIONFLOWFEATURE_FLAGS,
  ],
  serialized_options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(9, 10), (12, 13), ],
  oneofs=[
  ],
  serialized_start=201,
  serialized_end=738,
)


_REGIONFLOWFRAME_REGIONFLOW = _descriptor.Descriptor(
  name='RegionFlow',
  full_name='mediapipe.RegionFlowFrame.RegionFlow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='region_id', full_name='mediapipe.RegionFlowFrame.RegionFlow.region_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='centroid_x', full_name='mediapipe.RegionFlowFrame.RegionFlow.centroid_x', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='centroid_y', full_name='mediapipe.RegionFlowFrame.RegionFlow.centroid_y', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flow_x', full_name='mediapipe.RegionFlowFrame.RegionFlow.flow_x', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flow_y', full_name='mediapipe.RegionFlowFrame.RegionFlow.flow_y', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature', full_name='mediapipe.RegionFlowFrame.RegionFlow.feature', index=5,
      number=7, type=11, cpp_type=10, label=3,
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
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(6, 7), ],
  oneofs=[
  ],
  serialized_start=1016,
  serialized_end=1184,
)

_REGIONFLOWFRAME_BLOCKDESCRIPTOR = _descriptor.Descriptor(
  name='BlockDescriptor',
  full_name='mediapipe.RegionFlowFrame.BlockDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='block_width', full_name='mediapipe.RegionFlowFrame.BlockDescriptor.block_width', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_height', full_name='mediapipe.RegionFlowFrame.BlockDescriptor.block_height', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_blocks_x', full_name='mediapipe.RegionFlowFrame.BlockDescriptor.num_blocks_x', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_blocks_y', full_name='mediapipe.RegionFlowFrame.BlockDescriptor.num_blocks_y', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
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
  serialized_start=1186,
  serialized_end=1296,
)

_REGIONFLOWFRAME = _descriptor.Descriptor(
  name='RegionFlowFrame',
  full_name='mediapipe.RegionFlowFrame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='region_flow', full_name='mediapipe.RegionFlowFrame.region_flow', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_total_features', full_name='mediapipe.RegionFlowFrame.num_total_features', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unstable_frame', full_name='mediapipe.RegionFlowFrame.unstable_frame', index=2,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blur_score', full_name='mediapipe.RegionFlowFrame.blur_score', index=3,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frame_width', full_name='mediapipe.RegionFlowFrame.frame_width', index=4,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frame_height', full_name='mediapipe.RegionFlowFrame.frame_height', index=5,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_descriptor', full_name='mediapipe.RegionFlowFrame.block_descriptor', index=6,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_REGIONFLOWFRAME_REGIONFLOW, _REGIONFLOWFRAME_BLOCKDESCRIPTOR, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(3, 4), (5, 6), (6, 7), ],
  oneofs=[
  ],
  serialized_start=741,
  serialized_end=1314,
)


_REGIONFLOWFEATURELIST = _descriptor.Descriptor(
  name='RegionFlowFeatureList',
  full_name='mediapipe.RegionFlowFeatureList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature', full_name='mediapipe.RegionFlowFeatureList.feature', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frame_width', full_name='mediapipe.RegionFlowFeatureList.frame_width', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frame_height', full_name='mediapipe.RegionFlowFeatureList.frame_height', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unstable', full_name='mediapipe.RegionFlowFeatureList.unstable', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distance_from_border', full_name='mediapipe.RegionFlowFeatureList.distance_from_border', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blur_score', full_name='mediapipe.RegionFlowFeatureList.blur_score', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='long_tracks', full_name='mediapipe.RegionFlowFeatureList.long_tracks', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frac_long_features_rejected', full_name='mediapipe.RegionFlowFeatureList.frac_long_features_rejected', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='visual_consistency', full_name='mediapipe.RegionFlowFeatureList.visual_consistency', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(-1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp_usec', full_name='mediapipe.RegionFlowFeatureList.timestamp_usec', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='match_frame', full_name='mediapipe.RegionFlowFeatureList.match_frame', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_duplicated', full_name='mediapipe.RegionFlowFeatureList.is_duplicated', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actively_discarded_tracked_ids', full_name='mediapipe.RegionFlowFeatureList.actively_discarded_tracked_ids', index=12,
      number=13, type=5, cpp_type=1, label=3,
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
  serialized_start=1317,
  serialized_end=1729,
)


_SALIENTPOINT = _descriptor.Descriptor(
  name='SalientPoint',
  full_name='mediapipe.SalientPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='norm_point_x', full_name='mediapipe.SalientPoint.norm_point_x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='norm_point_y', full_name='mediapipe.SalientPoint.norm_point_y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='mediapipe.SalientPoint.type', index=2,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left', full_name='mediapipe.SalientPoint.left', index=3,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.3),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bottom', full_name='mediapipe.SalientPoint.bottom', index=4,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.3),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right', full_name='mediapipe.SalientPoint.right', index=5,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.3),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='top', full_name='mediapipe.SalientPoint.top', index=6,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.3),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='mediapipe.SalientPoint.weight', index=7,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(15),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='norm_major', full_name='mediapipe.SalientPoint.norm_major', index=8,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='norm_minor', full_name='mediapipe.SalientPoint.norm_minor', index=9,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angle', full_name='mediapipe.SalientPoint.angle', index=10,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SALIENTPOINT_SALIENTPOINTTYPE,
  ],
  serialized_options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(20000, 536870912), ],
  oneofs=[
  ],
  serialized_start=1732,
  serialized_end=2116,
)


_SALIENTPOINTFRAME = _descriptor.Descriptor(
  name='SalientPointFrame',
  full_name='mediapipe.SalientPointFrame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='point', full_name='mediapipe.SalientPointFrame.point', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(20000, 536870912), ],
  oneofs=[
  ],
  serialized_start=2118,
  serialized_end=2189,
)

_REGIONFLOWFEATURE.fields_by_name['feature_descriptor'].message_type = _PATCHDESCRIPTOR
_REGIONFLOWFEATURE.fields_by_name['feature_match_descriptor'].message_type = _PATCHDESCRIPTOR
_REGIONFLOWFEATURE.fields_by_name['internal_irls'].message_type = _TEMPORALIRLSSMOOTHING
_REGIONFLOWFEATURE.fields_by_name['binary_feature_descriptor'].message_type = _BINARYFEATUREDESCRIPTOR
_REGIONFLOWFEATURE_FLAGS.containing_type = _REGIONFLOWFEATURE
_REGIONFLOWFRAME_REGIONFLOW.fields_by_name['feature'].message_type = _REGIONFLOWFEATURE
_REGIONFLOWFRAME_REGIONFLOW.containing_type = _REGIONFLOWFRAME
_REGIONFLOWFRAME_BLOCKDESCRIPTOR.containing_type = _REGIONFLOWFRAME
_REGIONFLOWFRAME.fields_by_name['region_flow'].message_type = _REGIONFLOWFRAME_REGIONFLOW
_REGIONFLOWFRAME.fields_by_name['block_descriptor'].message_type = _REGIONFLOWFRAME_BLOCKDESCRIPTOR
_REGIONFLOWFEATURELIST.fields_by_name['feature'].message_type = _REGIONFLOWFEATURE
_SALIENTPOINT.fields_by_name['type'].enum_type = _SALIENTPOINT_SALIENTPOINTTYPE
_SALIENTPOINT_SALIENTPOINTTYPE.containing_type = _SALIENTPOINT
_SALIENTPOINTFRAME.fields_by_name['point'].message_type = _SALIENTPOINT
DESCRIPTOR.message_types_by_name['PatchDescriptor'] = _PATCHDESCRIPTOR
DESCRIPTOR.message_types_by_name['BinaryFeatureDescriptor'] = _BINARYFEATUREDESCRIPTOR
DESCRIPTOR.message_types_by_name['TemporalIRLSSmoothing'] = _TEMPORALIRLSSMOOTHING
DESCRIPTOR.message_types_by_name['RegionFlowFeature'] = _REGIONFLOWFEATURE
DESCRIPTOR.message_types_by_name['RegionFlowFrame'] = _REGIONFLOWFRAME
DESCRIPTOR.message_types_by_name['RegionFlowFeatureList'] = _REGIONFLOWFEATURELIST
DESCRIPTOR.message_types_by_name['SalientPoint'] = _SALIENTPOINT
DESCRIPTOR.message_types_by_name['SalientPointFrame'] = _SALIENTPOINTFRAME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PatchDescriptor = _reflection.GeneratedProtocolMessageType('PatchDescriptor', (_message.Message,), dict(
  DESCRIPTOR = _PATCHDESCRIPTOR,
  __module__ = 'mediapipe.util.tracking.region_flow_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.PatchDescriptor)
  ))
_sym_db.RegisterMessage(PatchDescriptor)

BinaryFeatureDescriptor = _reflection.GeneratedProtocolMessageType('BinaryFeatureDescriptor', (_message.Message,), dict(
  DESCRIPTOR = _BINARYFEATUREDESCRIPTOR,
  __module__ = 'mediapipe.util.tracking.region_flow_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.BinaryFeatureDescriptor)
  ))
_sym_db.RegisterMessage(BinaryFeatureDescriptor)

TemporalIRLSSmoothing = _reflection.GeneratedProtocolMessageType('TemporalIRLSSmoothing', (_message.Message,), dict(
  DESCRIPTOR = _TEMPORALIRLSSMOOTHING,
  __module__ = 'mediapipe.util.tracking.region_flow_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.TemporalIRLSSmoothing)
  ))
_sym_db.RegisterMessage(TemporalIRLSSmoothing)

RegionFlowFeature = _reflection.GeneratedProtocolMessageType('RegionFlowFeature', (_message.Message,), dict(
  DESCRIPTOR = _REGIONFLOWFEATURE,
  __module__ = 'mediapipe.util.tracking.region_flow_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.RegionFlowFeature)
  ))
_sym_db.RegisterMessage(RegionFlowFeature)

RegionFlowFrame = _reflection.GeneratedProtocolMessageType('RegionFlowFrame', (_message.Message,), dict(

  RegionFlow = _reflection.GeneratedProtocolMessageType('RegionFlow', (_message.Message,), dict(
    DESCRIPTOR = _REGIONFLOWFRAME_REGIONFLOW,
    __module__ = 'mediapipe.util.tracking.region_flow_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.RegionFlowFrame.RegionFlow)
    ))
  ,

  BlockDescriptor = _reflection.GeneratedProtocolMessageType('BlockDescriptor', (_message.Message,), dict(
    DESCRIPTOR = _REGIONFLOWFRAME_BLOCKDESCRIPTOR,
    __module__ = 'mediapipe.util.tracking.region_flow_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.RegionFlowFrame.BlockDescriptor)
    ))
  ,
  DESCRIPTOR = _REGIONFLOWFRAME,
  __module__ = 'mediapipe.util.tracking.region_flow_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.RegionFlowFrame)
  ))
_sym_db.RegisterMessage(RegionFlowFrame)
_sym_db.RegisterMessage(RegionFlowFrame.RegionFlow)
_sym_db.RegisterMessage(RegionFlowFrame.BlockDescriptor)

RegionFlowFeatureList = _reflection.GeneratedProtocolMessageType('RegionFlowFeatureList', (_message.Message,), dict(
  DESCRIPTOR = _REGIONFLOWFEATURELIST,
  __module__ = 'mediapipe.util.tracking.region_flow_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.RegionFlowFeatureList)
  ))
_sym_db.RegisterMessage(RegionFlowFeatureList)

SalientPoint = _reflection.GeneratedProtocolMessageType('SalientPoint', (_message.Message,), dict(
  DESCRIPTOR = _SALIENTPOINT,
  __module__ = 'mediapipe.util.tracking.region_flow_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.SalientPoint)
  ))
_sym_db.RegisterMessage(SalientPoint)

SalientPointFrame = _reflection.GeneratedProtocolMessageType('SalientPointFrame', (_message.Message,), dict(
  DESCRIPTOR = _SALIENTPOINTFRAME,
  __module__ = 'mediapipe.util.tracking.region_flow_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.SalientPointFrame)
  ))
_sym_db.RegisterMessage(SalientPointFrame)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
