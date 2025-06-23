from ultralytics import YOLO
import cv2
from deep_sort_realtime.deepsort_tracker import DeepSort

model = YOLO("best.pt") 
cap = cv2.VideoCapture("15sec_input_720p.mp4")
tracker = DeepSort(max_age=30)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    detections = results[0].boxes.data.cpu().numpy()

    dets_for_tracker = []
    for *xyxy, conf, cls in detections:
        if(conf < 0.8):
            continue
        x1, y1, x2, y2 = map(int, xyxy)
        dets_for_tracker.append(([x1, y1, x2 - x1, y2 - y1], conf, 'player'))

    tracks = tracker.update_tracks(dets_for_tracker, frame=frame)
    for track in tracks:
        if not track.is_confirmed():
            continue
        track_id = track.track_id
        ltrb = track.to_ltrb()
        cv2.rectangle(frame, (int(ltrb[0]), int(ltrb[1])), (int(ltrb[2]), int(ltrb[3])), (0,255,0), 2)
        cv2.putText(frame, f"ID: {track_id}", (int(ltrb[0]), int(ltrb[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    cv2.imshow("Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
