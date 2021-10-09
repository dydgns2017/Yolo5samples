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

- 추가예정

## 4. Referenced

- https://github.com/ultralytics/yolov5
- https://towardsdatascience.com/yolo-v5-is-here-b668ce2a4908
