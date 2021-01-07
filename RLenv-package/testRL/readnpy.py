import numpy as np
import matplotlib.pyplot as plt
score_history = np.load('training_record.npy')
fig = plt.figure()
plt.plot(range(len(score_history)),score_history , label="raw data")

SMA50 = []
cnt = 0
for i in range(len(score_history)-50):
    cnt = 0
    for j in range(50):
        cnt = cnt + score_history[i+j]
    SMA50.append(cnt/50)
plt.plot(range(len(SMA50)),SMA50 , label="SMA50")
plt.xlabel("Epoch")
plt.ylabel("Score")
plt.legend()
plt.savefig("final_plot.png")