import os
from PIL import Image
from collections import Counter

# Path to training data
data_dir = r"C:\Users\User\Desktop\springfield_identity\characters_train"

# Initialize counters
class_counts = {}
image_sizes = []
total_images = 0

# Iterate through each character folder
for class_name in os.listdir(data_dir):
    class_path = os.path.join(data_dir, class_name)
    
    # Skip if not a directory
    if not os.path.isdir(class_path):
        continue
    
    # Count images in this class
    images = [f for f in os.listdir(class_path) if f.endswith('.jpg')]
    class_counts[class_name] = len(images)
    total_images += len(images)
    
    # Sample first image to check dimensions
    if images:
        sample_img_path = os.path.join(class_path, images[0])
        try:
            img = Image.open(sample_img_path)
            image_sizes.append(img.size)
        except:
            pass

# Print statistics
print("DATASET EXPLORATION")
print(f"\nTotal Classes: {len(class_counts)}")
print(f"Total Images: {total_images}")
print(f"\nAverage images per class: {total_images / len(class_counts):.1f}")

print("CLASS DISTRIBUTION (Top 10 and Bottom 10)")

# Sort by count
sorted_classes = sorted(class_counts.items(), key=lambda x: x[1], reverse=True)

print("\nTop 10 classes:")
for class_name, count in sorted_classes[:10]:
    print(f"  {class_name:30s}: {count:4d} images")

print("\nBottom 10 classes:")
for class_name, count in sorted_classes[-10:]:
    print(f"  {class_name:30s}: {count:4d} images")

print("IMAGE DIMENSIONS (sample)")
size_counter = Counter(image_sizes)
print("\nMost common image sizes:")
for size, count in size_counter.most_common(5):
    print(f"  {size}: {count} samples")

