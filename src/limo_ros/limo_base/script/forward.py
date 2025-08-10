#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def main():
    # Inizializza il nodo ROS
    rospy.init_node('avanti_limo', anonymous=True)

    # Publisher su /cmd_vel
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    # Frequenza di pubblicazione: 10 Hz
    rate = rospy.Rate(10)

    # Crea messaggio Twist
    twist = Twist()
    twist.linear.x = 0.1      # Velocità avanti (m/s)
    twist.angular.z = 0.1     # Angolo di sterzo (rad/s)

    # Ciclo di pubblicazione
    while not rospy.is_shutdown():
        pub.publish(twist)
        rate.sleep()

if __name__ == '__main__':
    main()
