mport rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class MyNode(Node):
    def __init__(self):
        super().__init__("brojcanik")
        self.counter = 0
        self.create_timer(1.0, self.timer_callback)
        self.publisher = self.create_publisher(Int16, 'broj', 10)

    def timer_callback(self):
        self.counter += 1
        msg = Int16()
        msg.data = self.counter
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
