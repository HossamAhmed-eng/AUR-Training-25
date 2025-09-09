#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String , Int32
import random

class TemperatureNode(Node):
    def __init__(self):
        super().__init__('TemperatureNode')
        self.publisher_ = self.create_publisher(Int32, 'temperature', 10)
        self.create_timer(1,self.timer_callback)
        self.num=None

    def timer_callback(self):
        self.num=random.randint(15,45)
        msg=Int32() 
        msg.data=self.num 
        self.publisher_.publish(msg) 

def main():
    rclpy.init()
    node = TemperatureNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()