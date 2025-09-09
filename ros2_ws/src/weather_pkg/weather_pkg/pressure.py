#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String , Int32
import random

class PressureNode(Node):
    def __init__(self):
        super().__init__('PressureNode')
        self.publisher_ = self.create_publisher(Int32, 'pressure', 10)
        self.create_timer(3,self.timer_callback)
        self.num=None

    def timer_callback(self):
        self.num=random.randint(900,1100)
        msg=Int32() 
        msg.data=self.num 
        self.publisher_.publish(msg) 

def main():
    rclpy.init()
    node = PressureNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()