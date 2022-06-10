#! /usr/bin/env python
from __future__ import print_function
import rospy
import actionlib
import time
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
class nvgtn:
    def goal_client(self,u,rk,sk,tk,re):
        u = u
        rf = re
        r = []
        s = []
        t = []
        r = rk
        s = sk
        t = tk
        print('hey Im doing well')
        client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        print('this is done')
        client.wait_for_server()
        print('waiting for server ended')
        # Creates a goal to send to the action server.
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "odom"
        k = 0
        for k in range(u):
            goal.target_pose.pose.position.x = r[k]
            goal.target_pose.pose.position.y = s[k]
            goal.target_pose.pose.orientation.w = t[k]
            client.send_goal(goal)
            wait = client.wait_for_result()
            print('waiting for result ended')
            if wait:
                print('Success! The robot moved forward')
                time.sleep(rf)
            else:
                print('Not able to go at goal due to some reason')

if __name__ == '__main__':
    try:
        gh = nvgtn()
        q = []
        w = []
        r = []
        rospy.init_node('navigatn_goals')
        i = int(input('Enter the number of positions'))
        zx = int(input('Enter the time to keep the robot at a position'))
        for o in range(i):
            print('Enter the x,y,z and w orientation')
            xc = input('x co-ordinate')
            q.append(xc)
            yc = input('y co-ordinate')
            w.append(yc)
            rc = input('w orientation')
            r.append(rc)
        gh.goal_client(i,q,w,r,zx)


    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)