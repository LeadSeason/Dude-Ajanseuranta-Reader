# RFID reader python script

## Related Projects
Main:    [ToniLipponen/Dude-Ajanseuranta](https://github.com/ToniLipponen/Dude-Ajanseuranta)  
Fronend: [LeadSeason/Dude-Ajanseuranta-Frontend](https://github.com/LeadSeason/Dude-Ajanseuranta-Frontend)  
Backend: [ToniLipponen/Dude-Ajanseuranta-Backend](https://github.com/ToniLipponen/Dude-Ajanseuranta-Backend)  
Reader:  [LeadSeason/Dude-Ajanseuranta-Reader](https://github.com/LeadSeason/Dude-Ajanseuranta-Reader)

## How what why
This script is used to track dude participants in the dude room.  
reading a card will send the card id to the remote server.  
Originaly this readme was made as an note to future dude participants if changes are wanted

### Systemd
Script in ran and kept running on  using systemd services  
unit is located in `/etc/systemd/system/card-reader.service`  

systemctl can be used to start, stop, restart and get status  
- status = `systemctl status card-reader.service`  
- start = `systemctl start card-reader.service`  
- stop = `systemctl stop card-reader.service`  
- restart = `systemctl restart card-reader.service`  
- enable on boot = `systemctl enable card-reader.service`  
- disable on boot = `systemctl disable card-reader.service`  

### Server returns (OutDated)
`200 = ok` card acepted and saved  
`420 = No card in database` No card found in database use /add to add new card  
`500 = Error` Error in backend  

The server location is decided with the variable in the script called: SERVER_ADDRESS

## Todo
- [ ] Update README Server return with new returns
- [ ] Add /boot/config.txt configuration
- [ ] Add more bee sounds. Beep on script start, Beep on new card added, etc
- [ ] Add reason and why archlinuxarm was used to readme.
- [ ] Authentication between server and reader

## Issues
### script is ran as root.
make group called gpio or use tty group with the permissions to gpio .. etc
use an unprivilaged user called like cardreader with the group
only permissions to gpio but not root permissions
https://archlinuxarm.org/wiki/Raspberry_Pi

## Questions
If you have any questions feel free to email me at <a href="mailto:leadseason@proton.me">leadseason@proton.me</a>


## License
<p align="center">
  <a href="https://www.gnu.org/licenses/gpl-3.0.en.html">GPL-3.0</a>
  <br>
  <img href="https://www.gnu.org/licenses/gpl-3.0.en.html" src="https://www.gnu.org/graphics/gplv3-127x51.png">
</p>

