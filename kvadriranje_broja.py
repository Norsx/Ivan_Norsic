#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class MyNode(Node):

    def __init__(self):
        super().__init__("kvadriranje_broja")
        self.broj_subscriber_ = self.create_subscription(Int16, 'broj', self.broj_callback, 10)
        self.kvadrat_broja_publisher_ = self.create_publisher(Int16, 'kvadrat_broja', 10)

    def broj_callback(self, msg: Int16):
        broj = msg.data
        kvadrat = broj * broj
        self.kvadrat_broja_publisher_.publish(Int16(data=kvadrat))

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
