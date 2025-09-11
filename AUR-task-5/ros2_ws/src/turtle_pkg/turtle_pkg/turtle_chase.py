#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn , Kill
from turtlesim.msg import Pose
from random import randint
from functools import partial
from std_msgs.msg import Int32
import math
class turtlechase(Node):
    def __init__(self):
        super().__init__("turtlechase")
        self.spawn_client = self.create_client(Spawn, 'spawn')
        self.kill_client = self.create_client(Kill, 'kill')
        # wait for services
        while not self.spawn_client.wait_for_service(1):
            self.get_logger().warn("Waiting for spawn service...")
        while not self.kill_client.wait_for_service(1):
            self.get_logger().warn("Waiting for kill service...")
        self.turtles = ["turtle2", "turtle3", "turtle4"]
        self.enemy_positions = {}
        self.score=0
        self.player_pose = None
        self.turtlecounter=0
        self.create_timer(0.1,self.timer_callback)
        for t in self.turtles:
            self.spawn_turtle(t)
        #------- publish score
        self.score_pub = self.create_publisher(Int32, '/score', 10)
        #----------- subs
        self.sub_turtle1 = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback_turtle1,
            10
            )
        self.sub_turtle2 = self.create_subscription(
            Pose,
            '/turtle2/pose',
            self.pose_callback_turtle2,
            10
            )

        self.sub_turtle3 = self.create_subscription(
            Pose,
            '/turtle3/pose',
            self.pose_callback_turtle3,
            10
            )
        self.sub_turtle4 = self.create_subscription(
            Pose,
            '/turtle4/pose',
            self.pose_callback_turtle4,
            10
            )
    #---- end subs
        
    #------- pose callbacks pubs
    def pose_callback_turtle1(self,msg):
        self.player_pose = msg
    def pose_callback_turtle2(self,msg):
        self.enemy_positions['turtle2'] = msg
    def pose_callback_turtle3(self,msg):
        self.enemy_positions['turtle3'] = msg
    def pose_callback_turtle4(self,msg):
        self.enemy_positions['turtle4'] = msg
#---- timer
    def timer_callback(self):
        self.check_collisions()
#--------------------------- spawn
    def spawn_turtle(self, name):
        request = Spawn.Request()
        request.x = float(randint(1, 10))
        request.y = float(randint(1, 10))
        request.theta = 0.0
        request.name = name
        future = self.spawn_client.call_async(request)
        future.add_done_callback(partial(self.spawn_callback, name=name))

    def spawn_callback(self, future, name):
        try:
            response = future.result()
            self.get_logger().info(f"Spawned turtle: {response.name or name}")
        except Exception as e:
            self.get_logger().error(f"Spawn {name} failed: {e}")
#--------------------------- kill
    def kill_turtle(self, name):
        request = Kill.Request()
        request.name = name
        future = self.kill_client.call_async(request)
        future.add_done_callback(partial(self.kill_callback, name=name))

    def kill_callback(self, future, name):
        try:
            future.result()
            self.get_logger().info(f"Killed turtle: {name}")
            # respawn same one
            self.spawn_turtle(name)
        except Exception as e:
            self.get_logger().error(f"Kill {name} failed: {e}")
#--------------------------- check col
    def check_collisions(self):
        if self.player_pose is None:
            return 
        for name, pose in list(self.enemy_positions.items()):
            dist = math.sqrt((pose.x-self.player_pose.x)**2+(pose.y - self.player_pose.y)**2)
            if dist < 0.5:
                self.get_logger().info(f"{name} was hit!")
                self.score+=1 # Update the score and publish it
                msg = Int32()
                msg.data = self.score
                self.score_pub.publish(msg)
                self.kill_turtle(name)
                self.spawn_turtle(name)

def main():
    rclpy.init()
    node = turtlechase()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()