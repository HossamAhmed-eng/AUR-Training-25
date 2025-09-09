#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String , Int16

class MyNode(Node):
    def __init__(self):
        super().__init__('TimerNode')
        self.get_logger().info("TimerNode Started!")
        self.counter=10
        self.create_timer(1,self.timer_callback)
    def timer_callback(self):
        if self.counter==0:
            self.get_logger().info("Time is up!")
            self.counter-=1
        elif self.counter>0:
            self.get_logger().info(f'Countdown : {self.counter}')
            self.counter-=1
    

def main():
    rclpy.init()
    node = MyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()