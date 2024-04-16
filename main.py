from ultralytics import YOLO
#run model yolov8
model = YOLO('best.pt')
#run real time
results = model(source = "badfire.mp4", show = True )
# if u want to save, here:
#results = model(source = "badfire.mp4", show = True, save = True )



