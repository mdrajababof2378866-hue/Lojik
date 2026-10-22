# ============================================================
#  PROTOBUF DEFINITIONS (inlined)
# ============================================================
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()

# ---- MajoRLoGinrEq (MajorLogin req) ----
DESCRIPTOR_REQ = _descriptor.FileDescriptor(
    name='MajoRLoGinrEq.proto', package='', syntax='proto3', serialized_options=None,
    serialized_pb=b'\n\x13MajoRLoGinrEq.proto\"\xfa\n\n\nMajorLogin\x12\x12\n\nevent_time\x18\x03 \x01(\t\x12\x11\n\tgame_name\x18\x04 \x01(\t\x12\x13\n\x0bplatform_id\x18\x05 \x01(\x05\x12\x16\n\x0e\x63lient_version\x18\x07 \x01(\t\x12\x17\n\x0fsystem_software\x18\x08 \x01(\t\x12\x17\n\x0fsystem_hardware\x18\t \x01(\t\x12\x18\n\x10telecom_operator\x18\n \x01(\t\x12\x14\n\x0cnetwork_type\x18\x0b \x01(\t\x12\x14\n\x0cscreen_width\x18\x0c \x01(\r\x12\x15\n\rscreen_height\x18\r \x01(\r\x12\x12\n\nscreen_dpi\x18\x0e \x01(\t\x12\x19\n\x11processor_details\x18\x0f \x01(\t\x12\x0e\n\x06memory\x18\x10 \x01(\r\x12\x14\n\x0cgpu_renderer\x18\x11 \x01(\t\x12\x13\n\x0bgpu_version\x18\x12 \x01(\t\x12\x18\n\x10unique_device_id\x18\x13 \x01(\t\x12\x11\n\tclient_ip\x18\x14 \x01(\t\x12\x10\n\x08language\x18\x15 \x01(\t\x12\x0f\n\x07open_id\x18\x16 \x01(\t\x12\x14\n\x0copen_id_type\x18\x17 \x01(\t\x12\x13\n\x0b\x64\x65vice_type\x18\x18 \x01(\t\x12\'\n\x10memory_available\x18\x19 \x01(\x0b\x32\r.GameSecurity\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x1d \x01(\t\x12\x17\n\x0fplatform_sdk_id\x18\x1e \x01(\x05\x12\x1a\n\x12network_operator_a\x18) \x01(\t\x12\x16\n\x0enetwork_type_a\x18* \x01(\t\x12\x1c\n\x14\x63lient_using_version\x18\x39 \x01(\t\x12\x1e\n\x16\x65xternal_storage_total\x18< \x01(\x05\x12\"\n\x1a\x65xternal_storage_available\x18= \x01(\x05\x12\x1e\n\x16internal_storage_total\x18> \x01(\x05\x12\"\n\x1ainternal_storage_available\x18? \x01(\x05\x12#\n\x1bgame_disk_storage_available\x18@ \x01(\x05\x12\x1f\n\x17game_disk_storage_total\x18\x41 \x01(\x05\x12%\n\x1d\x65xternal_sdcard_avail_storage\x18\x42 \x01(\x05\x12%\n\x1d\x65xternal_sdcard_total_storage\x18\x43 \x01(\x05\x12\x10\n\x08login_by\x18I \x01(\x05\x12\x14\n\x0clibrary_path\x18J \x01(\t\x12\x12\n\nreg_avatar\x18L \x01(\x05\x12\x15\n\rlibrary_token\x18M \x01(\t\x12\x14\n\x0c\x63hannel_type\x18N \x01(\x05\x12\x10\n\x08\x63pu_type\x18O \x01(\x05\x12\x18\n\x10\x63pu_architecture\x18Q \x01(\t\x12\x1b\n\x13\x63lient_version_code\x18S \x01(\t\x12\x14\n\x0cgraphics_api\x18V \x01(\t\x12\x1d\n\x15supported_astc_bitset\x18W \x01(\r\x12\x1a\n\x12login_open_id_type\x18X \x01(\x05\x12\x18\n\x10\x61nalytics_detail\x18Y \x01(\x0c\x12\x14\n\x0cloading_time\x18\\ \x01(\r\x12\x17\n\x0frelease_channel\x18] \x01(\t\x12\x12\n\nextra_info\x18^ \x01(\t\x12 \n\x18\x61ndroid_engine_init_flag\x18_ \x01(\r\x12\x0f\n\x07if_push\x18\x61 \x01(\x05\x12\x0e\n\x06is_vpn\x18\x62 \x01(\x05\x12\x1c\n\x14origin_platform_type\x18\x63 \x01(\t\x12\x1d\n\x15primary_platform_type\x18\x64 \x01(\t\"5\n\x0cGameSecurity\x12\x0f\n\x07version\x18\x06 \x01(\x05\x12\x14\n\x0chidden_value\x18\x08 \x01(\x04\x62\x06proto3'
)

_MAJORLOGIN = _descriptor.Descriptor(
    name='MajorLogin', full_name='MajorLogin', filename=None, file=DESCRIPTOR_REQ,
    containing_type=None, extensions=[], nested_types=[], enum_types=[], serialized_options=None,
    is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[],
    serialized_start=24, serialized_end=1426,
    fields=[
        _descriptor.FieldDescriptor(name='event_time', full_name='MajorLogin.event_time', index=0, number=3, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='game_name', full_name='MajorLogin.game_name', index=1, number=4, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='platform_id', full_name='MajorLogin.platform_id', index=2, number=5, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='client_version', full_name='MajorLogin.client_version', index=3, number=7, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='system_software', full_name='MajorLogin.system_software', index=4, number=8, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='system_hardware', full_name='MajorLogin.system_hardware', index=5, number=9, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='telecom_operator', full_name='MajorLogin.telecom_operator', index=6, number=10, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='network_type', full_name='MajorLogin.network_type', index=7, number=11, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='screen_width', full_name='MajorLogin.screen_width', index=8, number=12, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='screen_height', full_name='MajorLogin.screen_height', index=9, number=13, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='screen_dpi', full_name='MajorLogin.screen_dpi', index=10, number=14, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='processor_details', full_name='MajorLogin.processor_details', index=11, number=15, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='memory', full_name='MajorLogin.memory', index=12, number=16, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='gpu_renderer', full_name='MajorLogin.gpu_renderer', index=13, number=17, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='gpu_version', full_name='MajorLogin.gpu_version', index=14, number=18, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='unique_device_id', full_name='MajorLogin.unique_device_id', index=15, number=19, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='client_ip', full_name='MajorLogin.client_ip', index=16, number=20, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='language', full_name='MajorLogin.language', index=17, number=21, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='open_id', full_name='MajorLogin.open_id', index=18, number=22, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='open_id_type', full_name='MajorLogin.open_id_type', index=19, number=23, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='device_type', full_name='MajorLogin.device_type', index=20, number=24, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='memory_available', full_name='MajorLogin.memory_available', index=21, number=25, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='access_token', full_name='MajorLogin.access_token', index=22, number=29, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='platform_sdk_id', full_name='MajorLogin.platform_sdk_id', index=23, number=30, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='network_operator_a', full_name='MajorLogin.network_operator_a', index=24, number=41, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='network_type_a', full_name='MajorLogin.network_type_a', index=25, number=42, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='device_model', full_name='MajorLogin.device_model', index=26, number=25, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='country_code', full_name='MajorLogin.country_code', index=27, number=26, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='client_using_version', full_name='MajorLogin.client_using_version', index=28, number=57, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='external_storage_total', full_name='MajorLogin.external_storage_total', index=29, number=60, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='external_storage_available', full_name='MajorLogin.external_storage_available', index=30, number=61, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='internal_storage_total', full_name='MajorLogin.internal_storage_total', index=31, number=62, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='internal_storage_available', full_name='MajorLogin.internal_storage_available', index=32, number=63, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='game_disk_storage_available', full_name='MajorLogin.game_disk_storage_available', index=33, number=64, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='game_disk_storage_total', full_name='MajorLogin.game_disk_storage_total', index=34, number=65, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='external_sdcard_avail_storage', full_name='MajorLogin.external_sdcard_avail_storage', index=35, number=66, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='external_sdcard_total_storage', full_name='MajorLogin.external_sdcard_total_storage', index=36, number=67, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='field_70', full_name='MajorLogin.field_70', index=37, number=70, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='login_by', full_name='MajorLogin.login_by', index=38, number=73, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='library_path', full_name='MajorLogin.library_path', index=39, number=74, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='reg_avatar', full_name='MajorLogin.reg_avatar', index=40, number=76, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='library_token', full_name='MajorLogin.library_token', index=41, number=77, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='channel_type', full_name='MajorLogin.channel_type', index=42, number=78, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='cpu_type', full_name='MajorLogin.cpu_type', index=43, number=79, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='cpu_architecture', full_name='MajorLogin.cpu_architecture', index=44, number=81, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='client_version_code', full_name='MajorLogin.client_version_code', index=45, number=83, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='field_85', full_name='MajorLogin.field_85', index=46, number=85, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='graphics_api', full_name='MajorLogin.graphics_api', index=47, number=86, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='supported_astc_bitset', full_name='MajorLogin.supported_astc_bitset', index=48, number=87, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='login_open_id_type', full_name='MajorLogin.login_open_id_type', index=49, number=88, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='analytics_detail', full_name='MajorLogin.analytics_detail', index=50, number=89, type=12, cpp_type=9, label=1, has_default_value=False, default_value=b"", message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='loading_time', full_name='MajorLogin.loading_time', index=51, number=92, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='release_channel', full_name='MajorLogin.release_channel', index=52, number=93, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='extra_info', full_name='MajorLogin.extra_info', index=53, number=94, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='android_engine_init_flag', full_name='MajorLogin.android_engine_init_flag', index=54, number=95, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='if_push', full_name='MajorLogin.if_push', index=55, number=97, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='is_vpn', full_name='MajorLogin.is_vpn', index=56, number=98, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='origin_platform_type', full_name='MajorLogin.origin_platform_type', index=57, number=99, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='primary_platform_type', full_name='MajorLogin.primary_platform_type', index=58, number=100, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='field_96', full_name='MajorLogin.field_96', index=59, number=96, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='field_102', full_name='MajorLogin.field_102', index=60, number=102, type=12, cpp_type=9, label=1, has_default_value=False, default_value=b"", message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='field_104', full_name='MajorLogin.field_104', index=61, number=104, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='field_105', full_name='MajorLogin.field_105', index=62, number=105, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='field_106', full_name='MajorLogin.field_106', index=63, number=106, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='field_107', full_name='MajorLogin.field_107', index=64, number=107, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
    ],
)

_GAMESECURITY = _descriptor.Descriptor(
    name='GameSecurity', full_name='GameSecurity', filename=None, file=DESCRIPTOR_REQ,
    containing_type=None, extensions=[], nested_types=[], enum_types=[], serialized_options=None,
    is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[],
    serialized_start=1428, serialized_end=1481,
    fields=[
        _descriptor.FieldDescriptor(name='version', full_name='GameSecurity.version', index=0, number=6, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
        _descriptor.FieldDescriptor(name='hidden_value', full_name='GameSecurity.hidden_value', index=1, number=8, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_REQ),
    ],
)

_MAJORLOGIN.fields_by_name['memory_available'].message_type = _GAMESECURITY
DESCRIPTOR_REQ.message_types_by_name['MajorLogin'] = _MAJORLOGIN
DESCRIPTOR_REQ.message_types_by_name['GameSecurity'] = _GAMESECURITY
_sym_db.RegisterFileDescriptor(DESCRIPTOR_REQ)

MajorLogin_pb = _reflection.GeneratedProtocolMessageType('MajorLogin', (_message.Message,), {
    'DESCRIPTOR': _MAJORLOGIN,
    '__module__': 'MajoRLoGinrEq_pb2'
})
_sym_db.RegisterMessage(MajorLogin_pb)

GameSecurity_pb = _reflection.GeneratedProtocolMessageType('GameSecurity', (_message.Message,), {
    'DESCRIPTOR': _GAMESECURITY,
    '__module__': 'MajoRLoGinrEq_pb2'
})
_sym_db.RegisterMessage(GameSecurity_pb)

# ---- MajorLoginRes ----
DESCRIPTOR_RES = _descriptor.FileDescriptor(
    name='MajoRLoGinrEs.proto', package='', syntax='proto3', serialized_options=None,
    serialized_pb=b'\n\x13MajoRLoGinrEs.proto\"o\n\x10\x42lacklistInfoRes\x12\x1e\n\nban_reason\x18\x01 \x01(\x0e\x32\n.BanReason\x12\x17\n\x0f\x65xpire_duration\x18\x02 \x01(\r\x12\x10\n\x08\x62\x61n_time\x18\x03 \x01(\r\x12\x10\n\x08\x62\x61n_type\x18\x04 \x01(\t\"f\n\x0eLoginQueueInfo\x12\r\n\x05\x41llow\x18\x01 \x01(\x08\x12\x16\n\x0equeue_position\x18\x02 \x01(\r\x12\x16\n\x0eneed_wait_secs\x18\x03 \x01(\r\x12\x15\n\rqueue_is_full\x18\x04 \x01(\x08\"\xa0\x01\n\x10\x46\x46\x41ntiConfigDesc\x12\x0e\n\x06region\x18\x01 \x01(\t\x12\x0e\n\x06\x65nable\x18\x02 \x01(\x08\x12\x12\n\nhpe_enable\x18\x03 \x01(\x08\x12\x12\n\nffi_enable\x18\x04 \x01(\x08\x12\x1c\n\x14mtp_lite_data_enable\x18\x05 \x01(\x08\x12\x12\n\nffm_enable\x18\x06 \x01(\x08\x12\x12\n\nffo_enable\x18\x07 \x01(\x08\"\xb8\x04\n\rMajorLoginRes\x12\x12\n\naccount_id\x18\x01 \x01(\x04\x12\x13\n\x0block_region\x18\x02 \x01(\t\x12\x13\n\x0bnoti_region\x18\x03 \x01(\t\x12\x11\n\tip_region\x18\x04 \x01(\t\x12\x19\n\x11\x61gora_environment\x18\x05 \x01(\t\x12\x19\n\x11new_active_region\x18\x06 \x01(\t\x12\x19\n\x11recommend_regions\x18\x07 \x03(\t\x12\r\n\x05token\x18\x08 \x01(\t\x12\x0b\n\x03ttl\x18\t \x01(\r\x12\x12\n\nserver_url\x18\n \x01(\t\x12\x16\n\x0e\x65mulator_score\x18\x0b \x01(\r\x12$\n\tblacklist\x18\x0c \x01(\x0b\x32\x11.BlacklistInfoRes\x12#\n\nqueue_info\x18\r \x01(\x0b\x32\x0f.LoginQueueInfo\x12\x0e\n\x06tp_url\x18\x0e \x01(\t\x12\x15\n\rapp_server_id\x18\x0f \x01(\r\x12\x0f\n\x07ip_city\x18\x10 \x01(\t\x12\x16\n\x0eip_subdivision\x18\x11 \x01(\t\x12\x0b\n\x03kts\x18\x15 \x01(\r\x12\n\n\x02\x61k\x18\x16 \x01(\x0c\x12\x0b\n\x03\x61iv\x18\x17 \x01(\x0c\x12\x12\n\nffanti_url\x18\x18 \x01(\t\x12.\n\x13\x66\x66_anti_config_desc\x18\x19 \x01(\x0b\x32\x11.FFAntiConfigDesc\x12\x1f\n\x17\x63onnection_seed_enabled\x18\x1a \x01(\x08\x12\x17\n\x0f\x63onnection_seed\x18\x1b \x01(\t*\xa2\x01\n\tBanReason\x12\x15\n\x11\x42\x61nReason_UNKNOWN\x10\x00\x12\x1a\n\x16\x42\x61nReason_IN_GAME_AUTO\x10\x01\x12\x14\n\x10\x42\x61nReason_REFUND\x10\x02\x12\x14\n\x10\x42\x61nReason_OTHERS\x10\x03\x12\x15\n\x11\x42\x61nReason_SKINMOD\x10\x04\x12\x1f\n\x1a\x42\x61nReason_IN_GAME_AUTO_NEW\x10\xf6\x07\x62\x06proto3'
)

_BANREASON = _descriptor.EnumDescriptor(
    name='BanReason', full_name='BanReason', filename=None, file=DESCRIPTOR_RES,
    values=[
        _descriptor.EnumValueDescriptor(name='BanReason_UNKNOWN', index=0, number=0, serialized_options=None, type=None),
        _descriptor.EnumValueDescriptor(name='BanReason_IN_GAME_AUTO', index=1, number=1, serialized_options=None, type=None),
        _descriptor.EnumValueDescriptor(name='BanReason_REFUND', index=2, number=2, serialized_options=None, type=None),
        _descriptor.EnumValueDescriptor(name='BanReason_OTHERS', index=3, number=3, serialized_options=None, type=None),
        _descriptor.EnumValueDescriptor(name='BanReason_SKINMOD', index=4, number=4, serialized_options=None, type=None),
        _descriptor.EnumValueDescriptor(name='BanReason_IN_GAME_AUTO_NEW', index=5, number=1014, serialized_options=None, type=None),
    ],
    containing_type=None, serialized_options=None, serialized_start=975, serialized_end=1137,
)

_BLACKLISTINFORES = _descriptor.Descriptor(
    name='BlacklistInfoRes', full_name='BlacklistInfoRes', filename=None, file=DESCRIPTOR_RES,
    containing_type=None, extensions=[], nested_types=[], enum_types=[], serialized_options=None,
    is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[],
    serialized_start=23, serialized_end=134,
    fields=[
        _descriptor.FieldDescriptor(name='ban_reason', full_name='BlacklistInfoRes.ban_reason', index=0, number=1, type=14, cpp_type=8, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='expire_duration', full_name='BlacklistInfoRes.expire_duration', index=1, number=2, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='ban_time', full_name='BlacklistInfoRes.ban_time', index=2, number=3, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='ban_type', full_name='BlacklistInfoRes.ban_type', index=3, number=4, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
    ],
)

_LOGINQUEUEINFO = _descriptor.Descriptor(
    name='LoginQueueInfo', full_name='LoginQueueInfo', filename=None, file=DESCRIPTOR_RES,
    containing_type=None, extensions=[], nested_types=[], enum_types=[], serialized_options=None,
    is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[],
    serialized_start=136, serialized_end=238,
    fields=[
        _descriptor.FieldDescriptor(name='Allow', full_name='LoginQueueInfo.Allow', index=0, number=1, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='queue_position', full_name='LoginQueueInfo.queue_position', index=1, number=2, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='need_wait_secs', full_name='LoginQueueInfo.need_wait_secs', index=2, number=3, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='queue_is_full', full_name='LoginQueueInfo.queue_is_full', index=3, number=4, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
    ],
)

_FFANTICONFIGDESC = _descriptor.Descriptor(
    name='FFAntiConfigDesc', full_name='FFAntiConfigDesc', filename=None, file=DESCRIPTOR_RES,
    containing_type=None, extensions=[], nested_types=[], enum_types=[], serialized_options=None,
    is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[],
    serialized_start=241, serialized_end=401,
    fields=[
        _descriptor.FieldDescriptor(name='region', full_name='FFAntiConfigDesc.region', index=0, number=1, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='enable', full_name='FFAntiConfigDesc.enable', index=1, number=2, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='hpe_enable', full_name='FFAntiConfigDesc.hpe_enable', index=2, number=3, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='ffi_enable', full_name='FFAntiConfigDesc.ffi_enable', index=3, number=4, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='mtp_lite_data_enable', full_name='FFAntiConfigDesc.mtp_lite_data_enable', index=4, number=5, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='ffm_enable', full_name='FFAntiConfigDesc.ffm_enable', index=5, number=6, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='ffo_enable', full_name='FFAntiConfigDesc.ffo_enable', index=6, number=7, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
    ],
)

_MAJORLOGINRES = _descriptor.Descriptor(
    name='MajorLoginRes', full_name='MajorLoginRes', filename=None, file=DESCRIPTOR_RES,
    containing_type=None, extensions=[], nested_types=[], enum_types=[], serialized_options=None,
    is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[],
    serialized_start=404, serialized_end=972,
    fields=[
        _descriptor.FieldDescriptor(name='account_id', full_name='MajorLoginRes.account_id', index=0, number=1, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='lock_region', full_name='MajorLoginRes.lock_region', index=1, number=2, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='noti_region', full_name='MajorLoginRes.noti_region', index=2, number=3, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='ip_region', full_name='MajorLoginRes.ip_region', index=3, number=4, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='agora_environment', full_name='MajorLoginRes.agora_environment', index=4, number=5, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='new_active_region', full_name='MajorLoginRes.new_active_region', index=5, number=6, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='recommend_regions', full_name='MajorLoginRes.recommend_regions', index=6, number=7, type=9, cpp_type=9, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='token', full_name='MajorLoginRes.token', index=7, number=8, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='ttl', full_name='MajorLoginRes.ttl', index=8, number=9, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='server_url', full_name='MajorLoginRes.server_url', index=9, number=10, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='emulator_score', full_name='MajorLoginRes.emulator_score', index=10, number=11, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='blacklist', full_name='MajorLoginRes.blacklist', index=11, number=12, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='queue_info', full_name='MajorLoginRes.queue_info', index=12, number=13, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='tp_url', full_name='MajorLoginRes.tp_url', index=13, number=14, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='app_server_id', full_name='MajorLoginRes.app_server_id', index=14, number=15, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='ip_city', full_name='MajorLoginRes.ip_city', index=15, number=16, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='ip_subdivision', full_name='MajorLoginRes.ip_subdivision', index=16, number=17, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='kts', full_name='MajorLoginRes.kts', index=17, number=21, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='ak', full_name='MajorLoginRes.ak', index=18, number=22, type=12, cpp_type=9, label=1, has_default_value=False, default_value=b"", message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='aiv', full_name='MajorLoginRes.aiv', index=19, number=23, type=12, cpp_type=9, label=1, has_default_value=False, default_value=b"", message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='ffanti_url', full_name='MajorLoginRes.ffanti_url', index=20, number=24, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='ff_anti_config_desc', full_name='MajorLoginRes.ff_anti_config_desc', index=21, number=25, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='connection_seed_enabled', full_name='MajorLoginRes.connection_seed_enabled', index=22, number=26, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
        _descriptor.FieldDescriptor(name='connection_seed', full_name='MajorLoginRes.connection_seed', index=23, number=27, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_RES),
    ],
)

_BLACKLISTINFORES.fields_by_name['ban_reason'].enum_type = _BANREASON
_MAJORLOGINRES.fields_by_name['blacklist'].message_type = _BLACKLISTINFORES
_MAJORLOGINRES.fields_by_name['queue_info'].message_type = _LOGINQUEUEINFO
_MAJORLOGINRES.fields_by_name['ff_anti_config_desc'].message_type = _FFANTICONFIGDESC
DESCRIPTOR_RES.message_types_by_name['BlacklistInfoRes'] = _BLACKLISTINFORES
DESCRIPTOR_RES.message_types_by_name['LoginQueueInfo'] = _LOGINQUEUEINFO
DESCRIPTOR_RES.message_types_by_name['FFAntiConfigDesc'] = _FFANTICONFIGDESC
DESCRIPTOR_RES.message_types_by_name['MajorLoginRes'] = _MAJORLOGINRES
DESCRIPTOR_RES.enum_types_by_name['BanReason'] = _BANREASON
_sym_db.RegisterFileDescriptor(DESCRIPTOR_RES)

MajorLoginRes_pb = _reflection.GeneratedProtocolMessageType('MajorLoginRes', (_message.Message,), {
    'DESCRIPTOR': _MAJORLOGINRES,
    '__module__': 'MajoRLoGinrEs_pb2'
})
_sym_db.RegisterMessage(MajorLoginRes_pb)

# ---- GetLoginDataRes ----
DESCRIPTOR_GLD = _descriptor.FileDescriptor(
    name='thunderFF.proto', package='', syntax='proto3', serialized_options=None,
    serialized_pb=b'\n\x0fthunderFF.proto\"Z\n\x0fGetLoginDataRes\x12\x10\n\x08nickname\x18\x04 \x01(\t\x12\x18\n\x10\x66unctional_addrs\x18\x0e \x01(\t\x12\x1b\n\x13informational_addrs\x18  \x01(\t\x62\x06proto3'
)

_GETLOGINDATARES = _descriptor.Descriptor(
    name='GetLoginDataRes', full_name='GetLoginDataRes', filename=None, file=DESCRIPTOR_GLD,
    containing_type=None, extensions=[], nested_types=[], enum_types=[], serialized_options=None,
    is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[],
    serialized_start=19, serialized_end=109,
    fields=[
        _descriptor.FieldDescriptor(name='nickname', full_name='GetLoginDataRes.nickname', index=0, number=4, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_GLD),
        _descriptor.FieldDescriptor(name='functional_addrs', full_name='GetLoginDataRes.functional_addrs', index=1, number=14, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_GLD),
        _descriptor.FieldDescriptor(name='informational_addrs', full_name='GetLoginDataRes.informational_addrs', index=2, number=32, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b"".decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR_GLD),
    ],
)

DESCRIPTOR_GLD.message_types_by_name['GetLoginDataRes'] = _GETLOGINDATARES
_sym_db.RegisterFileDescriptor(DESCRIPTOR_GLD)

GetLoginDataRes_pb = _reflection.GeneratedProtocolMessageType('GetLoginDataRes', (_message.Message,), {
    'DESCRIPTOR': _GETLOGINDATARES,
    '__module__': 'thunderFF_pb2'
})
_sym_db.RegisterMessage(GetLoginDataRes_pb)
