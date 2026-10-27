"""
Automated Kaggle Dataset Downloader & Preparer for PlantVillage.
Allows fetching the full dataset directly using Kaggle API or kagglehub.
"""

import os
import sys
import argparse
import subprocess
import zipfile

KAGGLE_DATASET_ID = "emmarex/plantdisease"
ALT_KAGGLE_DATASET_ID = "vipoooool/new-plant-diseases-dataset"


def check_kaggle_credentials():
    kaggle_json = os.path.expanduser("~/.kaggle/kaggle.json")
    has_env = "KAGGLE_USERNAME" in os.environ and "KAGGLE_KEY" in os.environ
    if not (os.path.exists(kaggle_json) or has_env):
        print("\n⚠️  Kaggle API Credentials Not Found!")
        print("To download the full dataset automatically via Kaggle CLI:")
        print("1. Sign in to https://www.kaggle.com and visit your Account settings.")
        print("2. Click 'Create New Token' to download 'kaggle.json'.")
        print("3. Place it at ~/.kaggle/kaggle.json or set environment variables:")
        print("   export KAGGLE_USERNAME='your_username'")
        print("   export KAGGLE_KEY='your_api_key'\n")
        return False
    return True


def download_dataset(output_dir: str = "dataset"):
    os.makedirs(output_dir, exist_ok=True)
    
    if not check_kaggle_credentials():
        print("Alternatively, download the PlantVillage dataset manually from:")
        print(f"👉 https://www.kaggle.com/datasets/{ALT_KAGGLE_DATASET_ID}")
        print(f"and unzip the dataset contents into '{output_dir}/'.")
        return False

    print(f"⬇️ Downloading dataset '{KAGGLE_DATASET_ID}' from Kaggle...")
    try:
        subprocess.run(
            ["kaggle", "datasets", "download", "-d", KAGGLE_DATASET_ID, "-p", output_dir, "--unzip"],
            check=True
        )
        print(f"✅ Successfully downloaded and extracted dataset to '{output_dir}'.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error downloading from Kaggle: {e}")
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download PlantVillage dataset from Kaggle")
    parser.add_argument("--output_dir", type=str, default="dataset", help="Output directory path")
    args = parser.parse_args()
    
    download_dataset(args.output_dir)
