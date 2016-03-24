# pishutdown
Small http server that enables remote shutdown\reboot of Raspberry Pi (in my case) or any other PC

Just set up Tornado, add the line

*@reboot cd pishutdown_dir python server.py*

to your crontab and with *http://ip:8888/* you get a hello message for testing;

with *http://ip:8888/act/[shutdown|reboot]_pi* you either shutdown or reboot the pc.


