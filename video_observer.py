
import cv2
import sys
import datetime
import time
import os

# simple observer by USB camera
if __name__ == "__main__":
	
	capture_span_min = int(sys.argv[1]) if len(sys.argv) >= 2 else 60
	capture_save_dir = sys.argv[2] if len(sys.argv) >= 3 else None
	if capture_save_dir and not os.path.exists(capture_save_dir):
		os.makedirs(capture_save_dir)
		
	cap = cv2.VideoCapture(0)
	
	while True:
		
		for _ in range(5):
			ret, frame = cap.read()
	
		if ret is None or ret is False:
			time.sleep(1000)
			continue
		
		now = datetime.datetime.now()
		cv2.putText(frame, str(now), (10, 40), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255))
		
		print(capture_save_dir)
		if capture_save_dir:
			capture_path = os.path.join(capture_save_dir, now.strftime("%Y-%m-%d_%H-%M-%S.jpg"))
			cv2.imwrite(capture_path, frame)

		cv2.imshow("cap", frame)
		
		if cv2.waitKey(1000*60*capture_span_min) == ord('q'):
			break
			
		