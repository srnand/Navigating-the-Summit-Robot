#! /usr/bin/env python

import rospy
from my_summit_localization.srv import MyServiceMessage
from std_srvs.srv import Empty, EmptyRequest
from geometry_msgs.msg import Pose


count=0

def callBack(request):
    pose=Pose()
    count+=1
    string=""
    string=pose.position.x+" "+pose.position.y+" "+pose.position.z+" "+pose.orientation.x+" "+pose.orientation.y+" "+pose.orientation.z+" "+pose.orientation.w
    MyServiceMessageResponse.navigation_successful=True
    MyServiceMessageResponse.message = request.label+" : "+string
    
    print MyServiceMessageResponse.message
    
    if count==3:
        f=open('spots.txt','w')
        f.write(MyServiceMessageResponse.message)
        f.close()
    return MyServiceMessageResponse

rospy.init_node('spot_recorder')
my_service = rospy.Service('/save_spot',MyServiceMessage,callBack)

rospy.spin()
