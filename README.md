# Yolo5samples

This repository just for yolo5samples execute & test & study

## 1. Settings environment for Yolo5

```bash
conda create -n yolov5 python=3.7
conda activate yolov5
conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cudatoolkit=11.1 -c pytorch -c conda-forge -y
```

```bash
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
```

## 2. Environment test

change dir

```bash
cd yolov5/
```

and then excute follow code

```python
import torch

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5l, yolov5x, custom

# Images
img = 'https://ultralytics.com/images/zidane.jpg'  # or file, Path, PIL, OpenCV, numpy, list

# Inference
results = model(img)

# Results
results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
```

results images like that show if you corretly installed environment

![image](https://user-images.githubusercontent.com/36920367/136014975-4a71ef16-dc5f-4ec4-9ed9-5ca22ff7e98f.png)

```python
python detect.py --source 0  # webcam
                            file.jpg  # image
                            file.mp4  # video
                            path/  # directory
                            path/*.jpg  # glob
                            'https://youtu.be/NUsoVlDFqZg'  # YouTube
                            'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
```

## 3. Samples

### 3.1. custom train datasets with CVAT

1. Download labeled datasets in CVAT server ( EXPORT DATASET YOLO 1.1 )
2. Modify Downloaded(yaml) files reference this [URL](https://github.com/ultralytics/yolov5/issues/12)
- like [this](KFSDataset.yml)
3. Train excute
```bash
python train.py --img 640 --batch 16 --epochs 3 --data KFSDataset.yaml --weights yolov5s.pt
```

reference [this](https://github.com/ultralytics/yolov5/issues/5040#issuecomment-934619308) issue if you got a error like this
```bash
UnicodeDecodeError: 'cp949' codec can't decode byte 0xf0 in position 9: illegal multibyte sequence
```


### 3.2 [Racoon Dataset Train & Detect Sample](./Raccon_sample)

## 4. Referenced

- https://github.com/ultralytics/yolov5
- https://github.com/mikel-brostrom/Yolov5_DeepSort_Pytorch
- https://towardsdatascience.com/yolo-v5-is-here-b668ce2a4908
