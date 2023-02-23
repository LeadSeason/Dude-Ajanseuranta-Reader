# RFID reader python script

## How what why
This script is used to track dude participants in the dude room.
reading a card will send the card id to the remote server.

### Systemd
Script in ran and kept running on  using systemd services  
unit is located in `/etc/systemd/system/card-reader.service`  

systemctl can be used to start, stop, restart and get status  
status = `systemctl status card-reader.service`  
start = `systemctl start card-reader.service`  
stop = `systemctl stop card-reader.service`  
restart = `systemctl restart card-reader.service`  
enable on boot = `systemctl enable card-reader.service`  
disable on boot = `systemctl disable card-reader.service`  

### Server returns
`200 = ok` card acepted and saved  
`420 = No card in database` No card found in database use /add to add new card  
`500 = Error` Error in backend  

The server location is decided with the variable in the script called: SERVER_ADDRESS

## Issues
### script is ran as root.
make group called gpio or use tty group with the permissions to gpio .. etc
use an unprivilaged user called like cardreader with the group
only permissions to gpio but not root permissions
https://archlinuxarm.org/wiki/Raspberry_Pi

## Questions
If you have any questions feel free to email me at <a href="mailto:leadseason@proton.me">leadseason@proton.me</a>