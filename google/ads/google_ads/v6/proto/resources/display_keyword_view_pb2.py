# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v6/proto/resources/display_keyword_view.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v6/proto/resources/display_keyword_view.proto',
  package='google.ads.googleads.v6.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v6.resourcesB\027DisplayKeywordViewProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V6.Resources\312\002!Google\\Ads\\GoogleAds\\V6\\Resources\352\002%Google::Ads::GoogleAds::V6::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nBgoogle/ads/googleads_v6/proto/resources/display_keyword_view.proto\x12!google.ads.googleads.v6.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xdc\x01\n\x12\x44isplayKeywordView\x12J\n\rresource_name\x18\x01 \x01(\tB3\xe0\x41\x03\xfa\x41-\n+googleads.googleapis.com/DisplayKeywordView:z\xea\x41w\n+googleads.googleapis.com/DisplayKeywordView\x12Hcustomers/{customer_id}/displayKeywordViews/{ad_group_id}~{criterion_id}B\x84\x02\n%com.google.ads.googleads.v6.resourcesB\x17\x44isplayKeywordViewProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V6.Resources\xca\x02!Google\\Ads\\GoogleAds\\V6\\Resources\xea\x02%Google::Ads::GoogleAds::V6::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_DISPLAYKEYWORDVIEW = _descriptor.Descriptor(
  name='DisplayKeywordView',
  full_name='google.ads.googleads.v6.resources.DisplayKeywordView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.resources.DisplayKeywordView.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003\372A-\n+googleads.googleapis.com/DisplayKeywordView', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352Aw\n+googleads.googleapis.com/DisplayKeywordView\022Hcustomers/{customer_id}/displayKeywordViews/{ad_group_id}~{criterion_id}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=196,
  serialized_end=416,
)

DESCRIPTOR.message_types_by_name['DisplayKeywordView'] = _DISPLAYKEYWORDVIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DisplayKeywordView = _reflection.GeneratedProtocolMessageType('DisplayKeywordView', (_message.Message,), {
  'DESCRIPTOR' : _DISPLAYKEYWORDVIEW,
  '__module__' : 'google.ads.googleads_v6.proto.resources.display_keyword_view_pb2'
  ,
  '__doc__': """A display keyword view.
  
  Attributes:
      resource_name:
          Output only. The resource name of the display keyword view.
          Display Keyword view resource names have the form:  ``customer
          s/{customer_id}/displayKeywordViews/{ad_group_id}~{criterion_i
          d}``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.resources.DisplayKeywordView)
  })
_sym_db.RegisterMessage(DisplayKeywordView)


DESCRIPTOR._options = None
_DISPLAYKEYWORDVIEW.fields_by_name['resource_name']._options = None
_DISPLAYKEYWORDVIEW._options = None
# @@protoc_insertion_point(module_scope)
