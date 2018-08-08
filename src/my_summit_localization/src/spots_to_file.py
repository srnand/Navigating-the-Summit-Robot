#! /usr/bin/env python

import rospy
from my_summit_localization.srv import MyServiceMessage, MyServiceMessageResponse
from geometry_msgs.msg import Pose, PoseWithCovarianceStamped


class SaveSpot():
    def __init__(self):
        self._pose = PoseWithCovarianceStamped()
        self.detection_dict = {"turtle":self._pose, "table":self._pose, "room":self._pose}
        self.my_service = rospy.Service('/save_spot',MyServiceMessage,self.callBack)
        self._pose_sub = rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped , self.sub_callBack)
    
    def sub_callBack(self, request):
        self._pose=request
    
    def callBack(self, request):
        if request.label=="turtle":
            self.detection_dict["turtle"]=self._pose
            MyServiceMessageResponse.message = "Saved Pose for turtle spot"
        elif request.label=="table":
            self.detection_dict["table"]=self._pose
            MyServiceMessageResponse.message = "Saved Pose for table spot"
        elif request.label=="room":
            self.detection_dict["room"]=self._pose
            MyServiceMessageResponse.message = "Saved Pose for room spot"
        elif request.label=="end":
            f=open('spots.txt','w')
            for key, value in self.detection_dict.iteritems():
                    if value:
                        f.write(str(key) + ':\n----------\n' + str(value) + '\n===========\n')
            f.close()
            response.message = "Written Poses to spots.txt file"
        MyServiceMessageResponse.navigation_successful=True
        return MyServiceMessageResponse

rospy.init_node('spot_recorder')

save_spot = SaveSpot()
rospy.spin()
