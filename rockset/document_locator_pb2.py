# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rockset/document_locator.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rockset/document_locator.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\020io.rockset.protoP\000\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1erockset/document_locator.proto\"7\n\x14\x44ocumentLocatorProto\x12\x0e\n\x06raw_id\x18\x01 \x01(\x04\x12\x0f\n\x07indices\x18\x02 \x03(\rB\x17\n\x10io.rockset.protoP\x00\xf8\x01\x01\x62\x06proto3'
)




_DOCUMENTLOCATORPROTO = _descriptor.Descriptor(
  name='DocumentLocatorProto',
  full_name='DocumentLocatorProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='raw_id', full_name='DocumentLocatorProto.raw_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='indices', full_name='DocumentLocatorProto.indices', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=34,
  serialized_end=89,
)

DESCRIPTOR.message_types_by_name['DocumentLocatorProto'] = _DOCUMENTLOCATORPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DocumentLocatorProto = _reflection.GeneratedProtocolMessageType('DocumentLocatorProto', (_message.Message,), {
  'DESCRIPTOR' : _DOCUMENTLOCATORPROTO,
  '__module__' : 'rockset.document_locator_pb2'
  # @@protoc_insertion_point(class_scope:DocumentLocatorProto)
  })
_sym_db.RegisterMessage(DocumentLocatorProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
