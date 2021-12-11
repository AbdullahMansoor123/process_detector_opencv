# # import cv2
# # import sys
# # from datetime import datetime
# #
# # # Initialize variables
# # camSource = 0
# # running = True
# # saveCount = 0
# # nSecond = 0
# # totalSec = 3
# # strSec = '321'
# # keyPressTime = 0.0
# # startTime = 0.0
# # timeElapsed = 0.0
# # startCounter = False
# # endCounter = False
# #
# # # Start the camera
# # camObj = cv2.VideoCapture(camSource)
# # if not camObj.isOpened():
# #     sys.exit('Camera did not provide frame.')
# #
# # frameWidth = int(camObj.get(cv2.CAP_PROP_FRAME_WIDTH))
# # frameHeight = int(camObj.get(cv2.CAP_PROP_FRAME_HEIGHT))
# #
# # # Start video stream
# # while running:
# #     readOK, frame = camObj.read()
# #
# #     # Display counter on screen before saving a frame
# #     if startCounter:
# #         if nSecond < totalSec:
# #             # draw the Nth second on each frame
# #             # till one second passes
# #             cv2.putText(img = frame,
# #                         text = strSec[nSecond],
# #                         org = (int(frameWidth/2 - 20),int(frameHeight/2)),
# #                         fontFace = cv2.FONT_HERSHEY_DUPLEX,
# #                         fontScale = 6,
# #                         color = (255,255,255),
# #                         thickness = 5,
# #                         lineType = cv2.LINE_AA)
# #
# #             timeElapsed = (datetime.now() - startTime).total_seconds()
# # #            print 'timeElapsed: {}'.format(timeElapsed)
# #
# #             if timeElapsed >= 1:
# #                 nSecond += 1
# # #                print 'nthSec:{}'.format(nSecond)
# #                 timeElapsed = 0
# #                 startTime = datetime.now()
# #
# #         else:
# #             cv2.imwrite('img' + str(saveCount) + '.jpg', frame)
# # #            print 'saveTime: {}'.format(datetime.now() - keyPressTime)
# #
# #             saveCount += 1
# #             startCounter = False
# #             nSecond = 1
# #
# #     # Get user input
# #     keyPressed = cv2.waitKey(3)
# #     if keyPressed == ord('s'):
# #         startCounter = True
# #         startTime = datetime.now()
# #         keyPressTime = datetime.now()
# # #        print 'startTime: {}'.format(startTime)
# # #        print 'keyPressTime: {}'.format(keyPressTime)
# #
# #     elif keyPressed == ord('q'):
# #         # Quit the while loop
# #         running = False
# #         cv2.destroyAllWindows()
# #
# #     # Show video stream in a window
# #     cv2.imshow('video', frame)
# #
# # camObj.release()
#
#
# def draw_text(frame, text, x, y, color=(255, 0, 255), thickness=4, size=3):
#     if x is not None and y is not None:
#         cv2.putText(
#             frame, text, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, size, color, thickness)
#
#
# import numpy as np
# import cv2
# import time
#
# # timeout = time.time() + 11   # 10 seconds from now
# cap = cv2.VideoCapture(0)
# init_time = time.time()
# test_timeout = init_time + 6
# final_timeout = init_time + 17
# counter_timeout_text = init_time + 1
# counter_timeout = init_time + 1
# counter = 5
# while (cap.isOpened()):
#     ret, frame = cap.read()
#     if ret == True:
#         center_x = int(frame.shape[0] / 2)
#         center_y = int(frame.shape[0] / 2)
#         if (time.time() > counter_timeout_text and time.time() < test_timeout):
#             draw_text(frame, str(counter), center_x, center_y)
#             counter_timeout_text += 0.03333
#         if (time.time() > counter_timeout and time.time() < test_timeout):
#             counter -= 1
#             counter_timeout += 1
#         cv2.imshow('frame', frame)
#         if (cv2.waitKey(1) & 0xFF == ord('q')) or (time.time() > final_timeout):
#             break
#     else:
#         break
# # Release everything if job is finished
# cap.release()
# cv2.destroyAllWindows()
import glob
csv_dir = 'data_files/*.csv'
video_dir = 'data_files/*.mp4'
csv_file_path = glob.glob(csv_dir)
video_file_path = glob.glob(video_dir)
for filename,video_path in zip(csv_file_path,video_file_path):
    print(filename)
    print(video_path)
    # process_detector(filename)

