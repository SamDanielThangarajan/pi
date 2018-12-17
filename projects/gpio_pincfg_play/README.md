#GPIO_PINCFG_PLAY

## BE
Backend rest server written in python

### APIS

#### GPIOS
GET /gpios[?list=all|reg]  
POST /gpios -d 'pin=<no>' -d 'mode=input|output' [-d 'switch=on|OFF']  


#### GPIO
GET /gpio/<pin>  
PUT /gpio/<pin> -d 'switch=on|off'  
