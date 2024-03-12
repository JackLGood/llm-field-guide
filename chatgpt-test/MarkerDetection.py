import cv2
import time

KNOWN_MARKERS = [11, 12]

class Detector:
    def __init__(self, cam_source = 0, debug = False):
        self.aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_100)
        self.aruco_param = cv2.aruco.DetectorParameters()
        self.aruco_detector = cv2.aruco.ArucoDetector(self.aruco_dict, self.aruco_param)

        self.feed = cv2.VideoCapture(cam_source, cv2.CAP_ANY)

        self.debug = debug

        if not self.feed.isOpened():
            # logging.error(f'Cannot open camera {cam_source}')
            exit()

        # self.feed.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        # self.feed.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        self.timeout = 5

    def find_first_marker(self):
        found = False
        marker = -1

        start_time = time.time()

        # Run until found known markers
        while not found:
            _, frame = self.feed.read()

            corners, ids, rejected = self.aruco_detector.detectMarkers(frame)
            if (corners is None or ids is None):
                continue

            if self.debug:
                # print('[INF] Showing detected markers')
                img_copy = img.copy()
                cv2.aruco.drawDetectedMarkers(img_copy, corners, ids)
                cv2.imshow('ShowMarkers', img_copy)

            for id, m_corners in zip(ids, corners):
                m_id = id[0].item()
                if m_id in KNOWN_MARKERS:
                    found = True
                    marker = m_id
                # self.img_markers[m_id] = Marker(m_id, m_corners[0].astype('int32'))
                    
            if time.time() > start_time + 5:
                break
                    
        return marker