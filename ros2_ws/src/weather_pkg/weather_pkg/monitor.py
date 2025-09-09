#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String , Int32
import json
class MonitorNode(Node):
    def __init__(self):
        super().__init__('MonitoringNode')
        self.get_logger().info(f"Monitoring Node ON!")
        self.temp=0
        self.humidity=0
        self.pressure=0
        self.subscription = self.create_subscription(
            Int32,
            'temperature',
            self.Temperature_callback,
            10)
        self.subscription = self.create_subscription(
            Int32,
            'humidity',
            self.humidity_callback,
            10)
        self.subscription = self.create_subscription(
            Int32,
            'pressure',
            self.pressure_callback,
            10)
        self.create_timer(1,self.timer_callback)
        self.log_txt = open("monitor_log.txt", "a")
        self.log_json = open("monitor_log.json", "a")
    def timer_callback(self):
        line = f"Temp = {self.temp} °C, Humidity = {self.humidity} %, Pressure = {self.pressure} hPa"
        self.get_logger().info(line)
        self.log_txt.write(line + "\n")
        self.log_txt.flush()
        entry = {
            "temperature": self.temp,
            "humidity": self.humidity,
            "pressure": self.pressure
        }
        self.log_json.write(json.dumps(entry) + "\n")
        self.log_json.flush()

    def Temperature_callback(self, msg:Int32):
        self.temp=msg.data
    def humidity_callback(self, msg:Int32):
        self.humidity=msg.data
    def pressure_callback(self, msg:Int32):
        self.pressure=msg.data

def main():
    rclpy.init()
    node = MonitorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()