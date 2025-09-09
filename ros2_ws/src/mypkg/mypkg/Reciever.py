#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String , Int16

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Int16,
            'topic',
            self.listener_callback,
            10)

    def listener_callback(self, msg:Int16):
        if msg.data % 2 ==0:
            self.get_logger().info(f"{msg.data} is Even ")
        else:
            self.get_logger().info(f"{msg.data} is Odd ")


def main():
    rclpy.init()
    node = MinimalSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()