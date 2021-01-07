# IKPY-based-RL-ENV
## RL Training Framework(IKPY-based)
* Follow OpenAI RL Frame
* How to Use it?
    * ![](https://i.imgur.com/PlM7tzi.png)
    * <code>-h</code>: Show the help message and exit
    * <code>-\-plot</code>: visualize the training trend
        * Keep saving the figure *scores_trend.png*
        * ![](https://i.imgur.com/RuWPvWA.png)
        * <code>-\-plot_T</code>: how often would you like to save the figure and the training record data?
            * Plot the raw data with SMA
                * ![](https://i.imgur.com/YItZ68V.png)
    * <code>-\-info</code>: show the progress bar
        * <code>-\-info_T</code>: how often would you like to update the bar?
        * ![](https://i.imgur.com/JPVMtxD.png)
    * <code>-\-save_models_T</code>: how often would yoy like to save the NNs?
    * <code>-\-clear_output</code>:Would you like to see only a single line updating? 
    * The More Thing You Want to See, The More Time You spent
:::info
:bulb: **注意**: 選擇越頻繁顯示訓練資訊，則需要越多時間完成訓練。以上圖運行之訓練為例，對比上周每epoch顯示所有資訊之6小時訓練過程，本次僅花費4小時完成50000epoch之相同目標的訓練。
<code>python3 RL-training.py --num_epoch 50000 --plot 1 --plot_T 1000 --info 1 --info_T 200  --save_models_T 500  --clear_output 0
</code>
:::
* Class Diagram
  ![](https://i.imgur.com/fWlIP9S.png)
* Eazy to Switch to Deepbots (with Webots)
![](https://i.imgur.com/lfAM1FN.png)
* Idea $1\rightarrow 2\rightarrow3$: 
    1. [IKPY-based-RL-ENV](https://github.com/KelvinYang0320/IKPY-based-RL-ENV): The Most Simplified Enviroment 
    2. Webots: robot simulator
    3. Real-world Franka Emika Panda
## IKPY-based RL訓練環境開發ipynb測試版
* 開發動機：Webots同時運行約三個就會導致GPU超載而螢幕顯示當機
* 優點：
    * 相較Webots以fast mode運行RL訓練約能提升4倍速度
    * 以jupyter notebook操作可以隨時進行cell微調
    * 收斂監測以及python tqdm進度條提供完成時間預測
        * ![](https://i.imgur.com/WoETGd0.gif)

* 缺點：無物理引擎，手臂實體邊界，在操作實際手臂前，宜先在Webots中訓練fine tuning 神經網路。

### DDPG(pytorch)固定單點觸碰測試[30 mins]
* 5000epoch後才存取神經網路
#### Training Result

| Score-Epoch   | Demo          |
| ------------- | ------------- |
|![](https://github.com/KelvinYang0320/IKPY-based-RL-ENV/blob/main/img/onepoint.png)|![](https://github.com/KelvinYang0320/IKPY-based-RL-ENV/blob/main/img/onepoint.gif)|

* 後續改成觸碰平面並加上手指前一軸之端點獎賞設計以維持盡可能平面移動，解決IKPY套件with orientation問題

### DDPG(pytorch)九點平面觸碰測試[6 hrs]
* 因為每epoch均進行存取神經網路，時間較長

| 9 points      | IKPY inverse kinematics Demo          |
| ------------- | ------------- |
|![](https://github.com/KelvinYang0320/IKPY-based-RL-ENV/blob/main/img/ikpyshow9.png)|![](https://github.com/KelvinYang0320/IKPY-based-RL-ENV/blob/main/img/ikpyshow9_reach.png)|


#### Training Result
| Score-Epoch     | Demo          |
| ------------- | ------------- |
|![](https://github.com/KelvinYang0320/IKPY-based-RL-ENV/blob/main/img/ikpy9trend.png)|![](https://github.com/KelvinYang0320/IKPY-based-RL-ENV/blob/main/img/ikpy9.gif)|

