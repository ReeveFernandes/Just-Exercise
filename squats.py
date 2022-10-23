def squats():
    import cv2  # imports opencv into the program
    import mediapipe as mp  # imports mediapipe into program
    import numpy as np  # for trigonometry

    def calculate_angle(a, b, c):
        a = np.array(a)  # First point
        b = np.array(b)  # Mid point
        c = np.array(c)  # End point

        radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1],
                                                                    a[0] - b[0])  # to find mid angle in radians
        angle = np.abs(radians * 180.0 / np.pi)  # converting radians

        if angle > 180.0:  # in order to always have angle within 180, if greater than 180 then subtract from 360
            angle = 360 - angle

        return angle

    # To count for break later in the code
    break_left_angle = 0.0
    break_right_angle = 0.0

    mp_drawing = mp.solutions.drawing_utils  # for drawing utilities
    mp_pose = mp.solutions.pose  # import pose estimation model

    # VIDEO FEED
    cap = cv2.VideoCapture(0)  # setting video capture device (laptop camera), number 0 represents mac cam

    # Squats counter variables
    counter = 0
    stage = ""

    # Setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5,
                      min_tracking_confidence=0.5) as pose:  # Set up mediapipe instance,detetction confidence is 50% and tracking confidence is 50%
        while cap.isOpened():
            ret, frame = cap.read()  # give feed from web came, ret is return variable, frame gives image

            # Recolor image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # recoloring the  image from bgr to rgb
            image.flags.writeable = False  # performace tuning

            # Make detection, accesses our pose model
            results = pose.process(image)

            # Recolor back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # rerendering the changed image

            # Extract landmarks
            try:
                landmarks = results.pose_landmarks.landmark

                # Get coordinates for left side
                left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                left_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                             landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                left_ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                              landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

                # Get coordinates for right side
                right_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                             landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                right_knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                              landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
                right_ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                               landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]

                # We need torso-leg coordination

                # Get coordinates for left shoulder-left leg
                left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,  # used for break statement
                                 landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                left_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                             landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]

                # Get coordinates for right shoulder-right leg
                right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,  # used for break statement
                                  landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                right_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                             landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                right_knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                              landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]

                # For break statement
                left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                              landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                               landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

                # Calculate angle
                angle_left = calculate_angle(left_hip, left_knee, left_ankle)
                angle_right = calculate_angle(right_hip, right_knee, right_ankle)
                angle_left_upper = calculate_angle(left_shoulder, left_hip, left_knee)
                angle_right_upper = calculate_angle(right_shoulder, right_hip, right_knee)
                break_left_angle = calculate_angle(left_wrist, right_shoulder, right_wrist)
                break_right_angle = calculate_angle(right_wrist, left_shoulder, left_wrist)

                # Squats counter logic
                if (angle_left > 120 and angle_left > 120) and (angle_left_upper > 160 and angle_right_upper > 160):
                    stage = "up"
                elif (angle_left < 90 and angle_right < 90) and (
                        angle_left_upper < 100 and angle_right_upper < 100) and stage == "up":
                    stage = "down"
                    counter += 1
                    print(counter)

            except:
                pass

            # Render squat counter
            # setup status box
            cv2.rectangle(image, (0, 0), (300, 73), (245, 117, 16), -1)

            # represent data
            cv2.putText(image, 'REPS    STAGE', (15, 12),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, str(counter) + " " + stage, (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (225, 255, 255), 2, cv2.LINE_AA)

            # # Stage data
            # cv2.putText(image, 'STAGE', (65, 12),
            #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            # cv2.putText(image, stage, (60, 60),
            #             cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            # Render detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                      mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                      # draws detections to the image
                                      )

            cv2.imshow('Mediapipe Feed', image)  # visualisation of image via pop up, frame is called mediapipe feed

            if cv2.waitKey(10) & (
                    break_left_angle > 160 and break_right_angle > 160):  # keeping wrists alongside shoulders in straight link closes the window
                break

        cap.release()
        cv2.destroyAllWindows()

        return counter
