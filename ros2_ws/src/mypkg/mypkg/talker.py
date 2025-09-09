#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String , Int16
import random

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('publisher_node')
        self.publisher_ = self.create_publisher(Int16, 'topic', 10)
        self.create_timer(1,self.timer_callback)
        self.num=None

    def timer_callback(self):
        self.num=random.randint(1,100)
        msg=Int16() # define your message type 
        msg.data=self.num # assign value
        self.publisher_.publish(msg) #publish your message

def main():
    rclpy.init()
    node = MinimalPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()