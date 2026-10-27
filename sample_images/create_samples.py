import os
from PIL import Image, ImageDraw

def create_sample_images():
    os.makedirs("sample_images", exist_ok=True)
    
    # 1. Healthy green leaf
    img_healthy = Image.new("RGB", (300, 300), color=(240, 248, 240))
    draw = ImageDraw.Draw(img_healthy)
    draw.ellipse([50, 40, 250, 260], fill=(46, 125, 50), outline=(27, 94, 32), width=3)
    draw.line([150, 40, 150, 260], fill=(20, 70, 25), width=3)
    draw.line([150, 100, 90, 80], fill=(20, 70, 25), width=2)
    draw.line([150, 130, 210, 110], fill=(20, 70, 25), width=2)
    draw.line([150, 180, 80, 170], fill=(20, 70, 25), width=2)
    draw.line([150, 210, 220, 200], fill=(20, 70, 25), width=2)
    img_healthy.save("sample_images/healthy_leaf.jpg")

    # 2. Diseased leaf with necrotic spots (blight / fungal infection simulation)
    img_diseased = Image.new("RGB", (300, 300), color=(245, 245, 235))
    draw_d = ImageDraw.Draw(img_diseased)
    draw_d.ellipse([50, 40, 250, 260], fill=(100, 140, 50), outline=(60, 90, 30), width=3)
    draw_d.line([150, 40, 150, 260], fill=(50, 70, 20), width=3)
    # Brown & yellow necrotic spots
    draw_d.ellipse([90, 90, 130, 130], fill=(139, 69, 19), outline=(180, 120, 20), width=2)
    draw_d.ellipse([170, 120, 215, 160], fill=(160, 82, 45), outline=(200, 140, 30), width=2)
    draw_d.ellipse([110, 180, 145, 215], fill=(110, 50, 15), outline=(150, 90, 20), width=2)
    draw_d.ellipse([180, 190, 205, 215], fill=(139, 69, 19))
    img_diseased.save("sample_images/diseased_leaf_spot.jpg")

    print("Created synthetic sample leaf images in sample_images/")

if __name__ == "__main__":
    create_sample_images()
