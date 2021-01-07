import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
from IPython.display import clear_output
import sys
import ikpy
from ikpy.chain import Chain
from ikpy.link import OriginLink, URDFLink
import numpy as np
import ikpy.utils.plot as plot_utils
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
class PandaEnv():
    def __init__(self):
        self.my_chain = Chain.from_urdf_file("./panda_with_bound.URDF")
        self.my_chain_ = Chain.from_urdf_file("./panda_with_bound_nofinger_center.URDF")
        self.state = [0]*10
        self.motorPosList =[0]*7
#         self.target_position = [0]*3
        TargetList = [[0.5, 0, 0], [0.4, 0, 0], [0.6, 0, 0], [0.4, 0.2, 0], [0.5, 0.2, 0], [0.6, 0.2, 0], [0.4, -0.2, 0], [0.5, -0.2, 0], [0.6, -0.2, 0]]
        self.target_position = np.array(TargetList[random.randint(0, 8)])
        # self.show(Panda=True, target=self.target_position)
        
    def show_my_chain_links(self):
        print("Len of links =", len(self.my_chain.links))
        print(self.my_chain.links)
        
    def reset(self): 
        self.motorPosList =[0]*7
#         self.target_position = np.random.randn(3)
#         self.target_position = self.target_position/np.linalg.norm(self.target_position)/2

        TargetList = [[0.5, 0, 0], [0.4, 0, 0], [0.6, 0, 0], [0.4, 0.2, 0], [0.5, 0.2, 0], [0.6, 0.2, 0], [0.4, -0.2, 0], [0.5, -0.2, 0], [0.6, -0.2, 0]]
        self.target_position = np.array(TargetList[random.randint(0, 8)])
        self.state = self.target_position.tolist() + self.motorPosList
        return self.state
    
    def show(self, Panda="True", target=[0]*3, joints=[0]*9):
#         print("target =",target)
        clear_output(True)
        fig = plt.figure(figsize = (10, 10))
        ax = plt.gca(projection='3d')
        axis_len = 1.4
        ax.plot([0, axis_len], [0, 0],[0, 0], color='g', marker='^', linestyle='dashed', linewidth=2)
        ax.plot([0, 0], [0, axis_len],[0, 0], color='c', marker='^', linestyle='dashed', linewidth=2)
        ax.plot([0, 0], [0, 0],[0, axis_len], color='orange', marker='^', linestyle='dashed', linewidth=2)
        ax.text(axis_len,0,0,'x')
        ax.text(0,axis_len,0,'y')
        ax.text(0,0,axis_len,'z')
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
        if(Panda):
            self.my_chain.plot(joints=joints, ax=ax, target=target)
            '''
            Param:
            joints (list) – The list of the positions of each joint
            ax (matplotlib.axes.Axes) – A matplotlib axes
            target (numpy.array) – An optional target
            show (bool) – Display the axe. Defaults to False
            '''
        joint6Pos = self.my_chain_.forward_kinematics(joints[0:8],full_kinematics=False)[:3,3]
        ax.scatter(joint6Pos[0], joint6Pos[1], joint6Pos[2], c='r', s=100, marker='o')
        # plt.show()
        
#         plt.clf()
    def step_eval(self, action):
        self.motorPosList = [action[i] + self.motorPosList[i] for i in range(len(action))]
        self.motorPosList[0] = np.clip(self.motorPosList[0], -2.8973, 2.8973)
        self.motorPosList[1] = np.clip(self.motorPosList[1], -1.7628, 1.7628)
        self.motorPosList[2] = np.clip(self.motorPosList[2], -2.8973, 2.8973)
        self.motorPosList[3] = np.clip(self.motorPosList[3], -3.0718, -0.0698)
        self.motorPosList[4] = np.clip(self.motorPosList[4], -2.8973, 2.8973)
        self.motorPosList[5] = np.clip(self.motorPosList[5], -0.0175, 3.7525)
        self.motorPosList[6] = np.clip(self.motorPosList[6], -2.8973, 2.8973)
        
        new_state = self.target_position.tolist() + self.motorPosList
        self.show(Panda="True", target=self.target_position, joints=[0]+self.motorPosList+[0])
        endPointPos = self.my_chain.forward_kinematics([0]+self.motorPosList+[0],full_kinematics=False)[:3, 3]
        distance = np.linalg.norm(endPointPos-self.target_position)
        reward = -distance
        if distance < 0.03: 
            reward += 0.5
        elif distance < 0.015: 
            reward += 1.5
        if(distance < 0.01):
            done = True 
        else:
            done = False
        info = "nothing"
        self.state = new_state
        return new_state, reward, done, info
    
    def step(self, action)->tuple:
        self.motorPosList = [action[i] + self.motorPosList[i] for i in range(len(action))]
        self.motorPosList[0] = np.clip(self.motorPosList[0], -2.8973, 2.8973)
        self.motorPosList[1] = np.clip(self.motorPosList[1], -1.7628, 1.7628)
        self.motorPosList[2] = np.clip(self.motorPosList[2], -2.8973, 2.8973)
        self.motorPosList[3] = np.clip(self.motorPosList[3], -3.0718, -0.0698)
        self.motorPosList[4] = np.clip(self.motorPosList[4], -2.8973, 2.8973)
        self.motorPosList[5] = np.clip(self.motorPosList[5], -0.0175, 3.7525)
        self.motorPosList[6] = np.clip(self.motorPosList[6], -2.8973, 2.8973)
        
        new_state = self.target_position.tolist() + self.motorPosList
        
        endPointPos = self.my_chain.forward_kinematics([0]+self.motorPosList+[0],full_kinematics=False)[:3, 3]
        distance = np.linalg.norm(endPointPos-self.target_position)
#         print(self.target_position)
        reward = -distance
        if distance < 0.015: 
            reward += 1.5
        elif distance < 0.03: 
            reward += 0.5
        if(distance < 0.01):
            done = True 
        else:
            done = False
        info = "nothing"
        self.state = new_state
        return new_state, reward, done, info