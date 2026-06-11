import os

from launch import LaunchDescription
from launch_ros.actions import Node


xfer_format = 0
multi_topic = 0
data_src = 0
publish_freq = 10.0
output_type = 0
frame_id = 'livox_frame'

cur_path = os.path.split(os.path.realpath(__file__))[0] + '/'
cur_config_path = cur_path + '../config'

mid360_156_config_path = os.path.join(cur_config_path, 'MID360_192_168_1_156.json')
mid360_12_config_path = os.path.join(cur_config_path, 'MID360_192_168_1_12.json')


def build_params(user_config_path):
    return [
        {"xfer_format": xfer_format},
        {"multi_topic": multi_topic},
        {"data_src": data_src},
        {"publish_freq": publish_freq},
        {"output_data_type": output_type},
        {"frame_id": frame_id},
        {"user_config_path": user_config_path},
        {"cmdline_input_bd_code": "livox0000000001"},
        {"lvx_file_path": "/home/livox/livox_test.lvx"},
    ]


def generate_launch_description():
    mid360_156 = Node(
        package='livox_ros_driver2',
        executable='livox_ros_driver2_node',
        namespace='mid360_156',
        name='livox_lidar_publisher',
        output='screen',
        parameters=build_params(mid360_156_config_path),
    )

    mid360_12 = Node(
        package='livox_ros_driver2',
        executable='livox_ros_driver2_node',
        namespace='mid360_12',
        name='livox_lidar_publisher',
        output='screen',
        parameters=build_params(mid360_12_config_path),
    )

    return LaunchDescription([
        mid360_156,
        mid360_12,
    ])
