# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rockset/document.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from rockset import value_pb2 as rockset_dot_value__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rockset/document.proto',
  package='rockset',
  syntax='proto3',
  serialized_options=b'\n\020io.rockset.protoP\000\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16rockset/document.proto\x12\x07rockset\x1a\x13rockset/value.proto\"I\n\x08\x44ocument\x12\n\n\x02id\x18\x02 \x01(\t\x12\x12\n\nevent_time\x18\x01 \x01(\x03\x12\x1d\n\x05value\x18\x03 \x01(\x0b\x32\x0e.rockset.ValueB\x17\n\x10io.rockset.protoP\x00\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[rockset_dot_value__pb2.DESCRIPTOR,])




_DOCUMENT = _descriptor.Descriptor(
  name='Document',
  full_name='rockset.Document',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='rockset.Document.id', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='event_time', full_name='rockset.Document.event_time', index=1,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='rockset.Document.value', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=129,
)

_DOCUMENT.fields_by_name['value'].message_type = rockset_dot_value__pb2._VALUE
DESCRIPTOR.message_types_by_name['Document'] = _DOCUMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Document = _reflection.GeneratedProtocolMessageType('Document', (_message.Message,), {
  'DESCRIPTOR' : _DOCUMENT,
  '__module__' : 'rockset.document_pb2'
  # @@protoc_insertion_point(class_scope:rockset.Document)
  })
_sym_db.RegisterMessage(Document)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
