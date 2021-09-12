# Cam-Brute

<img width="608" alt="Screenshot 2021-09-12 at 2 52 07 PM" src="https://user-images.githubusercontent.com/90141144/132982352-d18f11b0-6292-4184-b21b-235d216b2946.png">





# About
* Runs massscan on the input file containing ips or subnets
* Creates a file with desired port with masscan and send it to cameradar to find cameras
* After getting cameras, it creates a list of cameras urls and send it to take screenshots
 

# Requirements

It requires python 2.X and works only on Linux
```
apt install docker
apt install ffmpeg
pip install multiprocessing.dummy
pip install netaddr
pip install masscan

```
# Usage

Save ip/subnets list in a single file and run the following command

```python cam-scan.py iplist threads_count```

### Example
```python cam-scan.py iplist 10```

# Output Result
### Created Screenshots folder, url and rtsp-url file

<img width="582" alt="output-folder" src="https://user-images.githubusercontent.com/90141144/132224303-131fc655-4920-48df-8655-e3517bce9a9a.png">


### Inside Screenshots folder

<img width="589" alt="Screenshots-folder" src="https://user-images.githubusercontent.com/90141144/132225299-33e5ad33-f38a-4670-ab22-d9da45040e01.png">




Special Thanks to Cameradar developers https://github.com/Ullaakut/cameradar

