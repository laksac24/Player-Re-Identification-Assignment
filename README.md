# 🏃‍♂️ Soccer Player Re-Identification (Single Camera Feed)

This project identifies and tracks soccer players in a single camera feed, maintaining consistent IDs even if players leave and re-enter the frame. It uses a fine-tuned YOLOv11 model for detection and DeepSORT for tracking and re-identification.

## 📁 Project Structure

```
.
├── main.py                  # Main tracking and detection script
├── 15sec_input_720p.mp4     # Input video (15 seconds)
├── best.pt                  # YOLOv11 fine-tuned model (player/ball detection)
├── requirements.txt         # Python dependencies
└── README.md
```

## ⚙️ Setup Instructions

### 1. Clone the repo & create a virtual environment
```bash
git clone <https://github.com/laksac24/Player-Re-Identification-Assignment.git>

python -m venv venv  # to create a virtual env
venv\Scripts\activate  # On Windows
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:
```
ultralytics
opencv-python
deep_sort_realtime
```

## 🧠 YOLOv11 Model Download

Download the fine-tuned model here:  
👉 [Google Drive Link](https://drive.google.com/file/d/1-5fOSHOSB9UXyP_enOoZNAMScrePVcMD/view)

Place `best.pt` in your project directory.

## ▶️ How to Run

```bash
python main.py
```

The script will:
- Load YOLOv11 model
- Detect and track players in `15sec_input_720p.mp4`
- Maintain consistent player IDs even if they go out and come back into the frame
- Display tracking results in a live OpenCV window

Press `q` to quit the video playback.


