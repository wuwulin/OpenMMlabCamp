# OpenMMlabCamp
OpenMMlabCamp-作业2
## Introduction
split_data.py 为数据划分程序
基于MMPreTrain做的水果分类算法

首先采用backbone为Resnet50预训练模型进行微调
fruit_resnet50_8xb32_in1k.py 为config文件
epoch为154时，验证集达到最优效果为：accuracy/top1: 73.4339  accuracy/top5: 93.7355

后来采用efficientnetv2预训练模型进行微调，收敛速度更快，并且达到更高的精度。

Epoch(val) [14][27/27]  accuracy/top1: 86.0789  accuracy/top5: 97.4478  data_time: 0.0001  time: 0.0918

efficientnetv2-b3_8xb32_in1k.py为配置文件
