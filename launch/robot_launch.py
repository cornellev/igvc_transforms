import os
from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    pkg_root    = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    urdf = os.path.join(pkg_root,'urdf','robot_urdf.xacro')
    sensor_cfg = os.path.join(pkg_root,'config','sensors.yaml')

    robot_description = ParameterValue(
        Command(['xacro ',os.path.normpath(urdf), ' sensor_cfg:=', sensor_cfg]),
        value_type=str
    )

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}]
        )
    ])
