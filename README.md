# The "Springfield" Identity - Simpsons Character Classification

## Project Overview
This project implements a **Convolutional Neural Network (CNN) from scratch** to classify 42 different characters from The Simpsons TV show. The model achieves **65.88% validation accuracy** and **0.53 Macro F1 score** on held-out data.


## Model Architecture
- **Type:** Custom CNN built from scratch (no pre-trained weights)
- **Parameters:** 9,706,954 trainable parameters
- **Structure:**
  - 4 Convolutional Blocks (32 → 64 → 128 → 256 filters)
  - BatchNormalization and Dropout for regularization
  - 3 Fully Connected layers (512 → 256 → 42 classes)
- **Input:** 128×128 RGB images
- **Output:** 42-class classification

## Training Details
- **Dataset:** 16,764 images across 42 classes
- **Split:** 80% training (13,411 images) / 20% validation (3,353 images)
- **Epochs:** 30
- **Batch Size:** 32
- **Optimizer:** Adam (learning rate: 0.001)
- **Loss Function:** CrossEntropyLoss with class weights (handles imbalanced data)
- **Scheduler:** ReduceLROnPlateau (reduces LR when validation loss plateaus)
- **Data Augmentation:** 
  - Random horizontal flip
  - Random rotation (±10°)
  - Color jitter (brightness, contrast, saturation)
- **Reproducibility:** Random seed set to 42

## Performance
| Metric | Score |
|--------|-------|
| **Validation Accuracy** | 65.88% |
| **Validation Macro F1** | 0.5311 |
| **Training Accuracy** | 58.62% |
| **Best Epoch** | 30 |

## How to Run

### Inference (`inference.ipynb`)
**Prerequisites:**
- Trained model: `simpsons_cnn.pth`
- Test images folder (UNK)

**Steps:**
```python
# 1. Open inference.ipynb
# 2. Run Cells 1-5 to load model and define functions
# 3. Update paths in Cell 6 (when test data is provided):

test_data_dir = "/path/to/test_images"
model_path = "/path/to/simpsons_cnn.pth"
results = infer(test_data_dir, model_path)

# 4. Run the cell to generate results.json
```

**Output:**
- `results.json` - Predictions in format: `{"image_name.jpg": "character_name"}`

**Note:** Cell 7 is a test cell that verifies the inference function works correctly using mock data. It can be used to validate the pipeline before trying on actual test data.


## Known Limitations
- **Class imbalance:** Some characters have very few examples (e.g., Lionel Hutz: 3 images)
- **Variable image quality:** Training data has inconsistent resolutions and quality

## Results Interpretation
The model performs well on common characters (Homer, Bart, Marge) but may struggle with rare characters due to limited training examples. The Macro F1 score of 0.53 indicates balanced performance across all classes despite the imbalance.
