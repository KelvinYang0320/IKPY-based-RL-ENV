# IKPY-based-RL-ENV
## IKPY-based RL訓練環境開發初版
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
![](https://i.imgur.com/vrWElW1.png)![](https://i.imgur.com/e3dcf3t.png)

#### Training Result
| Score-Epoch     | Demo          |
| ------------- | ------------- |
|![](https://github.com/KelvinYang0320/IKPY-based-RL-ENV/blob/main/img/ikpy9trend.png)|![](https://github.com/KelvinYang0320/IKPY-based-RL-ENV/blob/main/img/ikpy9.gif)|

