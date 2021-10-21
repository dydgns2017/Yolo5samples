## Racoon Sample


### 1. Download Dataset

[this](https://public.roboflow.com/object-detection/raccoon/38) sample datasets for Yolo v5 pytorch

move yaml file to `yolov5/data` folder

### 2. Train


```bash
python train.py --img 640 --batch 16 --epochs 3 --data racoon.yaml --weights yolov5s.pt
```