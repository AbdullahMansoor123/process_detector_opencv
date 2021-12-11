import cv2
from datetime import datetime
import pandas as pd
import glob
import os

# Converts time string to seconds
def second_maker(start):
    x = datetime.strptime(start, '%M:%S.%f')
    time = x.minute * 60 + x.second + x.microsecond / 1000000
    return round(time)  # time is seconds

# resize image frame
def resize(image):
    return cv2.resize(image, (1280, 600))

# Print process activity from csv onto video frames
def process_indicator(csv_path, video_path):
    csv_df = pd.read_csv(csv_path)
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    count = 0
    while True:
        success, frame = cap.read()
        count += 1
        if not success:
            break
        cv2.putText(frame, f'Video Frame: {count}', (10, 25), 2, 1, (255, 0, 255), 2)

        for row in csv_df.itertuples():  # read each row by row
            _, process, start, stop = row
            start_frame = int(second_maker(start) * fps)  # convert start time to frames
            stop_frame = int(second_maker(stop) * fps)  # convert stop time to frames

            if count in range(start_frame, stop_frame):
                cv2.putText(frame, f'Process: {process}', (10, 50), 2, 1, (0, 255, 255), 2)
                cv2.putText(frame, f'Start Frame: {start_frame}', (10, 75), 2, 1, (0, 255, 0), 2)

            elif count == stop_frame:
                cv2.putText(frame, f'Process: {process}', (10, 50), 2, 1, (0, 255, 255), 2)
                cv2.putText(frame, f'Start Frame: {start_frame}', (10, 75), 2, 1, (0, 255, 0), 2)
                cv2.putText(frame, f'End Frame: {stop_frame}', (10, 100), 2, 1, (0, 0, 255), 2)

            elif stop_frame < count:
                pass

        cv2.imshow('Process Indicator', resize(frame))
        if cv2.waitKey(0) & 0xff == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# Change the directories to your videos and csv files location
csv_files = glob.glob('data_files/labels/'+'*')
vid_files = glob.glob('data_files/videos/'+'*')

# Runs the "process_indicator" function
for index, (csv_path, video_path) in enumerate(zip(csv_files, vid_files)):
    process_indicator(csv_path, video_path)
    video_name = os.path.basename(video_path)
    print(f'{index}.  {video_name} processing completed')
print(f'\nTotal files processed: {len(csv_files)}')
