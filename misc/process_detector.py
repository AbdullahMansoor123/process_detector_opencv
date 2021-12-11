import cv2
from datetime import datetime
from time import time
import pandas as pd

#Converts time to seconds
def second_maker(start):
    x = datetime.strptime(start, '%M:%S.%f')
    time = x.minute * 60 + x.second + x.microsecond / 1000000
    return round(time) #time is seconds


video_path = 'data_files/WIN_20211129_19_12_57_Pro.mp4'
csv_path = 'data_files/WIN_20211129_19_12_57_Pro.csv'
df = pd.read_csv(csv_path)

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)

previous = time()
duration = 0
print(fps)

while True:
    timer = cv2.getTickCount()
    success, frame = cap.read()
    if not success:
        break

    #read csv file
    # df = pd.read_csv(csv_path)
    for row in df.itertuples():
        _, process, start, stop = row
        # print(start)
        # convert time string to second
        start = second_maker(start)
        stop = second_maker(stop)

        #process = process name shows up when any process time matches with video current 4 time
        current = time()
        duration += current - previous
        current_time = int(duration)
        previous = current

        cv2.putText(frame, f'Duration: {int(duration)}', (10, 85), 1, 2, (0, 255, 255), 2)

        if current_time>=start:
            cv2.putText(frame, f'Process: {process}', (10, 15), 1, 2, (0, 255, 255), 2)
            cv2.putText(frame, f'Start Time: {start}', (10, 35), 1, 2, (0, 0,255), 2)
        #todo
        #code to terminate after condition is fullfiLLED
        if current_time>=stop:
            cv2.putText(frame, f'End Time: {stop}', (10, 50), 1, 2, (0, 255, 0), 2)

        # todo
        # code to terminate after condition is fullfilled

        # cv2.putText(frame, 'Frame Rate: '+str(int(fps)), (10, 75), 1, 1, (0, 255, 255), 2)

        cv2.imshow('Tracking', frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()