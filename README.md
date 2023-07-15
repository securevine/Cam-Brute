# Cam-Brute

<img width="883" alt="Screenshot 2021-09-12 at 2 52 07 PM" src="https://user-images.githubusercontent.com/90141144/132982352-d18f11b0-6292-4184-b21b-235d216b2946.png">





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
### Created Screenshots folder of different Camera brands , access list and log file

<img width="883" alt="Screenshot 2023-07-15 at 8 04 38 PM" src="https://github.com/securevine/Cam-Brute/assets/90141144/a7db689a-d56b-4e47-8b97-3a588d6fb9b4">


### Inside Screenshots folder

<img width="883" alt="Screenshots-folder" src="https://user-images.githubusercontent.com/90141144/132225299-33e5ad33-f38a-4670-ab22-d9da45040e01.png">





