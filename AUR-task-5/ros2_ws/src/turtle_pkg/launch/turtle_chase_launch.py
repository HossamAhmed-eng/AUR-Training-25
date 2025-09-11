from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    sim_node = Node(
        package='turtlesim',
        executable='turtlesim_node',
        name='sim'
    )
    chase_node = Node(
        package='turtle_pkg', 
        executable='turtle_chase',
        name='turtle_chase'
    )
    ld.add_action(sim_node)
    ld.add_action(chase_node)
    return ld
