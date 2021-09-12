# Cam-Brute

<img width="608" alt="Screenshot 2021-09-12 at 2 52 07 PM" src="https://user-images.githubusercontent.com/90141144/132982352-d18f11b0-6292-4184-b21b-235d216b2946.png">





# About
* Takes iplist as input and doing bruteforce on password
* Prepare access list of specific brand separately and send it to take screenshots
* Stores screenshots of cameras of different brands separately in specific folder
* Also creates logs of done ips so that we can resume the process

 

# Requirements

It requires python 2.X and works only on Linux
```
apt install ffmpeg
pip install colorama
pip install multiprocessing.dummy


```
# Usage

Save iplist in a single file and run the following command

```python CAM-BRUTEFORCE-main.py iplist passlist```

### Example
```python CAM-BRUTEFORCE-main.py iplist passlist```

# Output Result
### Created Screenshots folder, url and rtsp-url file

<img width="582" alt="output-folder" src="https://user-images.githubusercontent.com/90141144/132224303-131fc655-4920-48df-8655-e3517bce9a9a.png">


### Inside Screenshots folder

<img width="589" alt="Screenshots-folder" src="https://user-images.githubusercontent.com/90141144/132225299-33e5ad33-f38a-4670-ab22-d9da45040e01.png">




Special Thanks to Cameradar developers https://github.com/Ullaakut/cameradar

