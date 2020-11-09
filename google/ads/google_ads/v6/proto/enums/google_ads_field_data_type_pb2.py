# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v6/proto/enums/google_ads_field_data_type.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v6/proto/enums/google_ads_field_data_type.proto',
  package='google.ads.googleads.v6.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v6.enumsB\033GoogleAdsFieldDataTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V6.Enums\312\002\035Google\\Ads\\GoogleAds\\V6\\Enums\352\002!Google::Ads::GoogleAds::V6::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nDgoogle/ads/googleads_v6/proto/enums/google_ads_field_data_type.proto\x12\x1dgoogle.ads.googleads.v6.enums\x1a\x1cgoogle/api/annotations.proto\"\xdb\x01\n\x1aGoogleAdsFieldDataTypeEnum\"\xbc\x01\n\x16GoogleAdsFieldDataType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0b\n\x07\x42OOLEAN\x10\x02\x12\x08\n\x04\x44\x41TE\x10\x03\x12\n\n\x06\x44OUBLE\x10\x04\x12\x08\n\x04\x45NUM\x10\x05\x12\t\n\x05\x46LOAT\x10\x06\x12\t\n\x05INT32\x10\x07\x12\t\n\x05INT64\x10\x08\x12\x0b\n\x07MESSAGE\x10\t\x12\x11\n\rRESOURCE_NAME\x10\n\x12\n\n\x06STRING\x10\x0b\x12\n\n\x06UINT64\x10\x0c\x42\xf0\x01\n!com.google.ads.googleads.v6.enumsB\x1bGoogleAdsFieldDataTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V6.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V6\\Enums\xea\x02!Google::Ads::GoogleAds::V6::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_GOOGLEADSFIELDDATATYPEENUM_GOOGLEADSFIELDDATATYPE = _descriptor.EnumDescriptor(
  name='GoogleAdsFieldDataType',
  full_name='google.ads.googleads.v6.enums.GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BOOLEAN', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DATE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENUM', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FLOAT', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INT32', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INT64', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MESSAGE', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESOURCE_NAME', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UINT64', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=165,
  serialized_end=353,
)
_sym_db.RegisterEnumDescriptor(_GOOGLEADSFIELDDATATYPEENUM_GOOGLEADSFIELDDATATYPE)


_GOOGLEADSFIELDDATATYPEENUM = _descriptor.Descriptor(
  name='GoogleAdsFieldDataTypeEnum',
  full_name='google.ads.googleads.v6.enums.GoogleAdsFieldDataTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GOOGLEADSFIELDDATATYPEENUM_GOOGLEADSFIELDDATATYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=134,
  serialized_end=353,
)

_GOOGLEADSFIELDDATATYPEENUM_GOOGLEADSFIELDDATATYPE.containing_type = _GOOGLEADSFIELDDATATYPEENUM
DESCRIPTOR.message_types_by_name['GoogleAdsFieldDataTypeEnum'] = _GOOGLEADSFIELDDATATYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GoogleAdsFieldDataTypeEnum = _reflection.GeneratedProtocolMessageType('GoogleAdsFieldDataTypeEnum', (_message.Message,), {
  'DESCRIPTOR' : _GOOGLEADSFIELDDATATYPEENUM,
  '__module__' : 'google.ads.googleads_v6.proto.enums.google_ads_field_data_type_pb2'
  ,
  '__doc__': """Container holding the various data types.""",
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.enums.GoogleAdsFieldDataTypeEnum)
  })
_sym_db.RegisterMessage(GoogleAdsFieldDataTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
