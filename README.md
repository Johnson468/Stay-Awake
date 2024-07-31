# Stay-Awake
A small python script to move your mouse, press the shift key, and keep your PC awake when you're away
Uses command line arguments to set the number of minutes between movements and requires Python3 or higher.
Default timer is 3 minutes, but can be 1 or more. 

# Dependencies
This software uses PyAutoGui https://github.com/asweigart/pyautogui as the driver behind the movement. 
In addition, screeninfo is needed https://pypi.org/project/screeninfo/ to determine primary monitor resolution.
> Optional- Create Virtual Env Step: ``` python3 -m venv ./StayAwake ```
> ``` pip install -r requirements.txt  ```
