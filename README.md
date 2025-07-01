A simple bash/python script that can keep remote machines logged into captive internet portals and grab the ip,
and send it to a gdrive/cloud store file through rclone.


# REQUIREMENTS

1) Webdriver for your browser of choice that matches the browser version.
2) rclone which can be installed as a binary from the official website.
3) python's selenium library 

# EXECUTION

build bash scripts using 
```
chmod +x script.sh
```
then execute them with 
```
./script.sh
```
run `wifi_checker.sh` for keeping the captive portal logged in and sending the ip address over if the portal
re-connects.
you can also additionally run `ip_logger.sh` to get the ip address every 5 minutes. 
