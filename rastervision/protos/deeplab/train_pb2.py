# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rastervision/protos/deeplab/train.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rastervision/protos/deeplab/train.proto',
  package='deeplab.protos',
  syntax='proto2',
  serialized_pb=_b('\n\'rastervision/protos/deeplab/train.proto\x12\x0e\x64\x65\x65plab.protos\"\xb3\x07\n\x12TrainingParameters\x12\x1d\n\x15initialize_last_layer\x18\x01 \x01(\t\x12\'\n\x1flast_layers_contain_logits_only\x18\x02 \x01(\t\x12\x17\n\x0fupsample_logits\x18\x03 \x01(\t\x12\x1c\n\x14\x66ine_tune_batch_norm\x18\x04 \x01(\t\x12\x1a\n\x12\x62\x61se_learning_rate\x18\x05 \x01(\t\x12&\n\x1elast_layer_gradient_multiplier\x18\x06 \x01(\t\x12\x16\n\x0elearning_power\x18\x07 \x01(\t\x12\"\n\x1alearning_rate_decay_factor\x18\x08 \x01(\t\x12\x10\n\x08momentum\x18\t \x01(\t\x12 \n\x18slow_start_learning_rate\x18\n \x01(\t\x12\x14\n\x0cweight_decay\x18\x0b \x01(\t\x12 \n\x18learning_rate_decay_step\x18\x0c \x01(\t\x12\x17\n\x0fslow_start_step\x18\r \x01(\t\x12\x17\n\x0flearning_policy\x18\x0e \x01(\t\x12\x18\n\x10max_scale_factor\x18\x0f \x01(\t\x12\x18\n\x10min_scale_factor\x18\x10 \x01(\t\x12\x1e\n\x16scale_factor_step_size\x18\x11 \x01(\t\x12\x1d\n\x15\x64\x65\x63oder_output_stride\x18\x12 \x02(\x05\x12\x15\n\routput_stride\x18\x13 \x02(\x05\x12\x15\n\rmodel_variant\x18\x14 \x02(\t\x12\x14\n\x0c\x61trous_rates\x18\x15 \x03(\x05\x12\x1a\n\x0btrain_split\x18\x16 \x01(\t:\x05train\x12\x17\n\x07\x64\x61taset\x18\x17 \x01(\t:\x06\x63ustom\x12\x18\n\x10train_batch_size\x18\x18 \x02(\x05\x12 \n\x18training_number_of_steps\x18\x19 \x02(\x05\x12\x17\n\x0ftrain_crop_size\x18\x1a \x03(\x05\x12\x1d\n\x0f\x64l_custom_train\x18\x1b \x01(\x05:\x04\x31\x33\x33\x33\x12\"\n\x14\x64l_custom_validation\x18\x1c \x01(\x05:\x04\x31\x33\x33\x33\x12#\n\x15save_summaries_images\x18\x1d \x01(\x08:\x04true\x12\x1f\n\x12save_interval_secs\x18\x1e \x01(\x05:\x03\x36\x30\x30\x12\x1f\n\x13save_summaries_secs\x18\x1f \x01(\x05:\x02\x36\x30\x12\x15\n\nnum_clones\x18  \x01(\x05:\x01\x31')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TRAININGPARAMETERS = _descriptor.Descriptor(
  name='TrainingParameters',
  full_name='deeplab.protos.TrainingParameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='initialize_last_layer', full_name='deeplab.protos.TrainingParameters.initialize_last_layer', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_layers_contain_logits_only', full_name='deeplab.protos.TrainingParameters.last_layers_contain_logits_only', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='upsample_logits', full_name='deeplab.protos.TrainingParameters.upsample_logits', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fine_tune_batch_norm', full_name='deeplab.protos.TrainingParameters.fine_tune_batch_norm', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='base_learning_rate', full_name='deeplab.protos.TrainingParameters.base_learning_rate', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_layer_gradient_multiplier', full_name='deeplab.protos.TrainingParameters.last_layer_gradient_multiplier', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='learning_power', full_name='deeplab.protos.TrainingParameters.learning_power', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='learning_rate_decay_factor', full_name='deeplab.protos.TrainingParameters.learning_rate_decay_factor', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='momentum', full_name='deeplab.protos.TrainingParameters.momentum', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='slow_start_learning_rate', full_name='deeplab.protos.TrainingParameters.slow_start_learning_rate', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weight_decay', full_name='deeplab.protos.TrainingParameters.weight_decay', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='learning_rate_decay_step', full_name='deeplab.protos.TrainingParameters.learning_rate_decay_step', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='slow_start_step', full_name='deeplab.protos.TrainingParameters.slow_start_step', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='learning_policy', full_name='deeplab.protos.TrainingParameters.learning_policy', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_scale_factor', full_name='deeplab.protos.TrainingParameters.max_scale_factor', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_scale_factor', full_name='deeplab.protos.TrainingParameters.min_scale_factor', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scale_factor_step_size', full_name='deeplab.protos.TrainingParameters.scale_factor_step_size', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='decoder_output_stride', full_name='deeplab.protos.TrainingParameters.decoder_output_stride', index=17,
      number=18, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_stride', full_name='deeplab.protos.TrainingParameters.output_stride', index=18,
      number=19, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='model_variant', full_name='deeplab.protos.TrainingParameters.model_variant', index=19,
      number=20, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='atrous_rates', full_name='deeplab.protos.TrainingParameters.atrous_rates', index=20,
      number=21, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='train_split', full_name='deeplab.protos.TrainingParameters.train_split', index=21,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("train").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataset', full_name='deeplab.protos.TrainingParameters.dataset', index=22,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("custom").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='train_batch_size', full_name='deeplab.protos.TrainingParameters.train_batch_size', index=23,
      number=24, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='training_number_of_steps', full_name='deeplab.protos.TrainingParameters.training_number_of_steps', index=24,
      number=25, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='train_crop_size', full_name='deeplab.protos.TrainingParameters.train_crop_size', index=25,
      number=26, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dl_custom_train', full_name='deeplab.protos.TrainingParameters.dl_custom_train', index=26,
      number=27, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1333,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dl_custom_validation', full_name='deeplab.protos.TrainingParameters.dl_custom_validation', index=27,
      number=28, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1333,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='save_summaries_images', full_name='deeplab.protos.TrainingParameters.save_summaries_images', index=28,
      number=29, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='save_interval_secs', full_name='deeplab.protos.TrainingParameters.save_interval_secs', index=29,
      number=30, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=600,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='save_summaries_secs', full_name='deeplab.protos.TrainingParameters.save_summaries_secs', index=30,
      number=31, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=60,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_clones', full_name='deeplab.protos.TrainingParameters.num_clones', index=31,
      number=32, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=1007,
)

DESCRIPTOR.message_types_by_name['TrainingParameters'] = _TRAININGPARAMETERS

TrainingParameters = _reflection.GeneratedProtocolMessageType('TrainingParameters', (_message.Message,), dict(
  DESCRIPTOR = _TRAININGPARAMETERS,
  __module__ = 'rastervision.protos.deeplab.train_pb2'
  # @@protoc_insertion_point(class_scope:deeplab.protos.TrainingParameters)
  ))
_sym_db.RegisterMessage(TrainingParameters)


# @@protoc_insertion_point(module_scope)
