import ikpy
from ikpy.chain import Chain
from ikpy.link import OriginLink, URDFLink
import numpy as np
import ikpy.utils.plot as plot_utils
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
from IPython.display import clear_output
import sys

from argparse import ArgumentParser
from PandaEnv import PandaEnv

parser = ArgumentParser()
parser.add_argument("--num_epoch", dest="num_epoch", help="number of epochs to train", type=int)
parser.add_argument("--plot", help="optional plotting argument", dest="plot", type=int, choices=[0, 1])
parser.add_argument("--plot_T", help="optional plotting period argument", dest="plot_T", type=int)
parser.add_argument("--info", help="optional training info argument", dest="info", type=int, choices=[0, 1])
parser.add_argument("--info_T", help="optional info showing period argument", dest="info_T", type=int)
parser.add_argument("--save_models_T", help="optional save models period argument", dest="per_T", type=int)
parser.add_argument("--clear_output", help="optional clear output argument", dest="clearOutput", type=int, choices=[0, 1])
args = parser.parse_args()

num_epoch = args.num_epoch
env = PandaEnv()
# env.show_my_chain_links()
from ddpg_torch import Agent
import numpy as np

from IPython.display import clear_output
def plot(scores):
        """Plot the training progresses."""
        # clear_output(True)
        plt.figure(figsize=(20, 5))
        plt.plot(scores)
        plt.savefig('scores_trend.png')
        plt.close()
        # plt.show()
        

env = PandaEnv()
agent = Agent(alpha=0.000025, beta=0.00025, input_dims=[10], tau=0.001, 
              batch_size=64,  layer1_size=400, layer2_size=400, n_actions=7)

#agent.load_models()
np.random.seed(0)

score_history = []

step_cnt = 0
for i in range(num_epoch):
    if(args.info and i%args.info_T==0): 
        sys.stdout.write('[%d %%][' %(int(100*i/num_epoch)))
        for j in range(int(20*i/num_epoch)):
            sys.stdout.write('█')
        sys.stdout.write('][%d/%d]\n' %(i,num_epoch))
        sys.stdout.flush()
    # sys.stdout.flush()
    agent.save_models() # ...save models...
    obs = env.reset()
    done = False
    score = 0
    while not done:
        step_cnt = step_cnt + 1
        if(step_cnt>500):
            step_cnt=0
            break
        act = agent.choose_action(obs)
        new_state, reward, done, info = env.step(act*0.032)
        agent.remember(obs, act, reward, new_state, int(done))
        
        score += reward
        obs = new_state
        #env.render()
    agent.learn()
    score_history.append(score)
    
    if((args.info and i%args.per_T==0) or i==num_epoch-1):
        agent.save_models()
        sys.stdout.write('episode %d | score %.2f | trailing 100 games avg %.3f\n' % (i,score, np.mean(score_history[-100:])))
        sys.stdout.flush()
    if((args.plot and i%args.plot_T==0) or i==num_epoch-1):
        # print(args.plot)
        plot(score_history)
        np.save('training_record', np.array(score_history))
    
    if(args.clearOutput):
        clear_output(True)
# plotLearning(score_history, filename, window=100)