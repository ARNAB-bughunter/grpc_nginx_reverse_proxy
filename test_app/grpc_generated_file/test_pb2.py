# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntest.proto\x12\nhelloworld\"\x19\n\tInputJson\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"\x1a\n\nOutputJson\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t2@\n\x04Test\x12\x38\n\x05Hello\x12\x15.helloworld.InputJson\x1a\x16.helloworld.OutputJson\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'test_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_INPUTJSON']._serialized_start=26
  _globals['_INPUTJSON']._serialized_end=51
  _globals['_OUTPUTJSON']._serialized_start=53
  _globals['_OUTPUTJSON']._serialized_end=79
  _globals['_TEST']._serialized_start=81
  _globals['_TEST']._serialized_end=145
# @@protoc_insertion_point(module_scope)
