# %%
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
