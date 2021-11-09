# %%
"""
python train.py  --batch 4 --epochs 500 --device 0 --data KFSDataset.yaml --weights yolov5s.pt
python detect.py --source 'https://www.youtube.com/watch?v=Ofp26_oc4CA' --weights  "/c/Users/yonghoon/Desktop/Yolo5samples/yolov5/runs/train/exp17/weights/best.pt"
"""
import torch
# %%

model = torch.hub.load('../yolov5', 
                        'custom',
                        path='../yolov5/runs/train/exp17/weights/best.pt',
                        source='local',
                        force_reload=True) # local repo
# %%
img = "imgs/testjpg.jpg"
results = model(img)
results.show()
# %%
