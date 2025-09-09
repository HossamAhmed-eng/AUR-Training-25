#!/usr/bin/env python3
import sys, termios, tty
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class KeyboardNode(Node):
    def __init__(self):
        super().__init__('keyboard_node')
        self.pub1 = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pub2 = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)
        self.run()
    def get_key(self):
        tty.setraw(sys.stdin.fileno())
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, termios.tcgetattr(sys.stdin))
        return key
    def run(self):
        print("Arrow keys -> turtle1 | WASD -> turtle2 | q to quit")
        while True:
            key = self.get_key()
            twist1, twist2 = Twist(), Twist()
            # Turtle1 with arrow keys
            if key == '\x1b':   # special key (escape sequence)
                _ = sys.stdin.read(1)  # skip [
                key2 = sys.stdin.read(1)
                if key2 == 'A': twist1.linear.x = 2.0    # up
                if key2 == 'B': twist1.linear.x = -2.0   # down
                if key2 == 'C': twist1.angular.z = -2.0  # right
                if key2 == 'D': twist1.angular.z = 2.0   # left
                self.pub1.publish(twist1)
            # Turtle2 with WASD
            if key.lower() == 'w': twist2.linear.x = 2.0
            if key.lower() == 's': twist2.linear.x = -2.0
            if key.lower() == 'a': twist2.angular.z = 2.0
            if key.lower() == 'd': twist2.angular.z = -2.0
            if key.lower() == 'q': break
            self.pub2.publish(twist2)
def main():
    rclpy.init()
    KeyboardNode()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
