# Football Player Tracker

Computer vision with OpenCV, ML analysis with YOLO.

## Requirements

Download project dependencies: 
```
pip install ultralytics
```

To activate virtual environment:
```
.venv\Scripts\Activate.ps1
```

## Training

Training is done on Google Colabs. To retrain or recalibrate the model used:
1. Copy the `football_training.ipynb` notebook from the `training/` directory to Google Colabs. Remember to set the Roboflow API key.
2. Run the entire notebook. This will take a while.
3. When finished, find the trained model weights at `runs/detect/train`. There should be two files here: `best.pt` and `last.pt`. Copy these two files into the local `models` folder.

## References

Ultralytics: https://github.com/ultralytics/ultralytics

`model.predict()` annotates a given video using the given model and returns anotation data.


