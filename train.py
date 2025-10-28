from ultralytics import YOLO

def main():
   # Load model
   model = YOLO("yolov12n.pt")

   # Train
   model.train(data="datasets/pvztrain.yaml", epochs=1024, patience=150)

   # Validate
   model.val()

   # 将模型导出为ONNX格式
   # model.export(format='onnx')

if __name__ == "__main__":
   main()
