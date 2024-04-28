from pythonosc import udp_client
#from pythonosc.dispatcher import Dispatcher
#from pythonosc import osc_server
import tomllib as toml
import argparse
import sys
import curses

with open('config.toml', 'rb') as f:
	config = toml.load(f)
	print("Loaded config!")

if config['defaultDevice'] != 0:	# If a default is set
	device = config['defaultDevice']
else:
	tmp_valid = False
	while not tmp_valid:
		for n in config['targets']:
			tmp_dev = config['targets'][str(n)]
			tmp_name = tmp_dev['name']
			tmp_ip = tmp_dev['ip']
			tmp_port = tmp_dev['port']
			print("""#{}
			\tName: {}
			\tIP: {}
			\tPort: {}""".format(n,tmp_name,tmp_ip,tmp_port))
		tmp_choice = str(input("Choose a device.\n"))
		try:
			device = config['targets'][tmp_choice]
		except:
			print("Invalid ID! Please try again.")
		else:
			tmp_valid = True
			ip = tmp_ip
			port = tmp_port

#client = udp_client.SimpleUDPClient(ip, port)
def getch():
    screen = curses.initscr()
    print(screen.getch())


while True:
	getch()
	#client.send_message("/chatbox/input", [ str(msgOutput), True, False])