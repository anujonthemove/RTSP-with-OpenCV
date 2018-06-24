# Instructions

- Download `live555MediaServer` from the link in the description below and keep it inside 'videos' directory.
- Run media server. 
    - If you are on Linux, follow the steps below
    `$ cd RTSP-with-OpenCV/`
    `$ chmod +x ./videos/live555MediaServer`
    `$ ./videos/live555MediaServer`
    - this will generate a rtsp link (via local system IP)
- Copy the link generated above and paste it in place of <rtsp-url> in the rtsp_poc.py code[line number 10]
- Run the code from another terminal: 
`$ python rtsp_poc.py`

# Directory description 
## - videos
- a directory to keep local videos. For this example, you'd need a video which has humans with frontal faces visible. An example video could be ["Obama out" speech](https://www.youtube.com/watch?v=NxFkEj7KPC0). Also, live media server works with many video formats but only '.webm' format has been tested(with OpenCV in this example). You may check other formats on the official website

## - models
- OpenCV's frontal face haar cascade detector

# Codes
##### rtsp_poc.py
- Code to demonstrate a simple face detection model running on a video streamed over RTSP

##### check_rtsp_exceptions.py
- Code to demonstrate how to use exception handling with RTSP feeds

# Live Media Server
- This is an open source video streamer which can stream locally stored video over rtsp
- For more details, please refer to the official page: http://www.live555.com/mediaServer/