#! /usr/bin/env python
import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseResult, MoveBaseFeedback
import actionlib

def feedback_callback(feedback):
    print('[Feedback] Going to Goal Pose...')

rospy.init_node('move_base_action_client')

client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
client.wait_for_server()

goal = MoveBaseGoal()
goal.target_pose.header.frame_id = 'map'
goal.target_pose.pose.position.x = 1.16
goal.target_pose.pose.position.y = -4.76
goal.target_pose.pose.position.z = 0.0
goal.target_pose.pose.orientation.x = 0.0
goal.target_pose.pose.orientation.y = 0.0
goal.target_pose.pose.orientation.z = 0.75
goal.target_pose.pose.orientation.w = 0.66

client.send_goal(goal, feedback_cb=feedback_callback)
client.wait_for_result()

print('[Result] State: %d'%(client.get_state()))
