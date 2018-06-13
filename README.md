# palm-read

This is the open source project made in HackNTU 2017. We labeled around 2000 pictures and used VGG16 as based model to train a CNN model. You can use it to build your own palm recognition.

## Install
First, clone the project.
```
$ git clone https://github.com/kkshyu/palm-read.git
```
Second, pull the Git LFS file. (If you dont't have git-lfs, please follow [here](https://github.com/git-lfs/git-lfs/wiki/Installation))
```
$ git lfs pull
```
At last, install the dependencies. (We suggest you to install in `virtualenv with Python3.5`)
```
(venv)$ pip install -r requirements.txt
```

## Get started
You can use our pre-trained model to make prediction.
```
python test_palm.py
```
Or, you can train yourself.
```
python train_palm.py
```

## Configuration
In `settings.py`, you can customize your own settings.
* IMG_WIDTH, IMG_HEIGHT: image size to be reized. If your memory is not enough, make it smaller.
* FLOW_PARAMS: image flow to train. If your memory is not enough, make it smaller.
* TUNED_PARAMS: Keras model tunning parameters. If you don't have much time, make them smaller.
* IMG_AUG: image augmentation. Make good augmentation for your training data set.

---
More Information: [When AI meets 3000-year-old Chinese Palmistry](https://towardsdatascience.com/when-ai-meets-3000-year-old-chinese-palmistry-a767b7f3defb)
