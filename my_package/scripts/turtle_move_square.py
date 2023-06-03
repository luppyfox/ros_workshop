import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math

class Turtlebot:
    def __init__(self):
        rospy.init_node('turtle', anonymous = True)
        self.pose_sub = rospy.Subscriber('/turtle1/pose', Pose, self.update_pose)
        self.vel_pub = rospy.Publisher('/turtle1/cmd_vel', Pose, queue_size = 10)
        self.current = Pose()
        self.tol = 0.1
        self.rate = rospy.Rate(1)
        self.start_pose = Pose()

    def update_pose(self, data):
        self.current.x = data.x
        self.current.y = data.y
        self.current.theta = data.theta
    
    def send_vel(self, x_vel, angular_vel):
        cmd_vel = Twist()
        cmd_vel.linear.x = x_vel
        cmd_vel.angular.z = angular_vel
        self.vel_pub.publish(cmd_vel)
    
    def set_start(self):
        self.rate.sleep()
        self.start_pose.x = self.current.x
        self.start_pose.y = self.current.y
        self.start_pose.theta = self.current.theta
        rospy.loginfo(f"set start point at x = {self.start_pose.x} y = {self.start_pose.y} theta = {self.start_pose.theta}")


    def distance_error(self, distance_goal):
        self.rate.sleep()
        distance = math.sqrt(math.pow(self.current.x - self.start_pose.x,2) + math.pow(self.start_pose.y - self.current.y,2))
        distance_error = distance_goal - distance
        rospy.loginfo(f"distance erroe {distance_error}")
        return distance_error
    
    def andular_error(self, angular_goal):
        self.rate.sleep()
        angular_goal = (angular_goal*math.pi)/180
        turn_angle = self.current.theta - self.start_pose.theta
        if turn_angle > math.pi:
            turn_angle -= math.pi*2
        if turn_angle < math.pi:
            turn_angle += math.pi*2
        else:
            turn_angle = abs(turn_angle)
        angular_error = abs(angular_goal - turn_angle)
        return(angular_error)

    def turtle_move(self, x_goal):
        self.set_start()
        rospy.loginfo(f"start moving {x_goal} unit")
        while abs(self.distance_error(x_goal))>self.tol:
            self.send_vel(0.5, 0)
        rospy.loginfo("Finish goal")
        self.send_vel(0, 0)
    
    def turn(self, deg):
        self.start_pose
        cmd_vel = 0.5
        rospy.loginfo(f"start turning {deg} degree")
        while abs(self.andular_error(deg))>self.tol:
            self.send_vel(0, 0.3)
        self.send_vel(0,0)
        
if __name__ == '__main__':
    tt = Turtlebot()
    for i in range(4):
        tt.turn(90)
        tt.turtle_move(4)