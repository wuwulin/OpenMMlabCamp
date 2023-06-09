import os
import random
from PIL import Image

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径

train_mulu=r"D:/fruit/training_set"
val_mulu=r"D:/fruit/val_set"
trainval_percent=0.2 #可自行进行调节
train_percent=1
txtsavepath = 'ImageSets\Main'
file_root=r'D:\fruit30_train'
total_file_ = os.listdir(file_root)
for fruit_file in total_file_:
    fruit_file_path=os.path.join(file_root,fruit_file)
    # print("fruit_file_path: ",fruit_file_path)
    total_xml = os.listdir(fruit_file_path)
    num = len(total_xml)
    list = range(num)
    tv = int(num * trainval_percent)
    tr = int(tv * train_percent)
    trainval = random.sample(list, tv)
    train = random.sample(trainval, tr)
    for i in list:
        name = total_xml[i] + '\n'
        fruit_name_and_num=os.path.join(fruit_file_path,total_xml[i])
        fru_img = Image.open(fruit_name_and_num)
        if i in trainval:
            # ftrainval.write(name)
            if i in train:
                new=train_mulu+'/'+fruit_file
                mkdir(train_mulu)
                mkdir(new)
                img_path_save=train_mulu+'/'+fruit_file+'/'+total_xml[i]
                fru_img.save(img_path_save)
        else:
            new = val_mulu + '/' + fruit_file
            mkdir(val_mulu)
            mkdir(new)
            img_path_save = val_mulu + '/' + fruit_file + '/' + total_xml[i]
            fru_img.save(img_path_save)



