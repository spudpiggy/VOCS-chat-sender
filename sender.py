from pythonosc import udp_client
#from pythonosc.dispatcher import Dispatcher
#from pythonosc import osc_server
import tomllib as toml
import argparse
import curses

with open('config.toml', 'rb') as f:
	config = toml.load(f)
	print("Loaded config!")

if config['defaultDevice'] != 0:	# If a default is set
	device = str(config['defaultDevice'])
	ip = config['targets'][device]['ip']
	port = config['targets'][device]['port']
else:
	tmp_valid = False
	while not tmp_valid:
		for n in config['targets']:
			tmp_dev = config['targets'][str(n)]
			tmp_name = tmp_dev['name']
			tmp_ip = str(tmp_dev['ip'])
			tmp_port = tmp_dev['port']
			print("""#{}
			\tName: {}
			\tIP: {}
			\tPort: {}""".format(n,tmp_name,tmp_ip,tmp_port))
		tmp_choice = str(int(input("Choose a device.\n")))
		try:
			device = config['targets'][tmp_choice]
		except:
			print("Invalid ID! Please try again.")
		else:
			tmp_valid = True
			ip = device['ip']
			port = device['port']

client = udp_client.SimpleUDPClient(ip, port)

screen = curses.initscr()
msg = []
try:
	while True:
		tmp_key = screen.getkey()
		if tmp_key == '\b':
			try:
				msg.pop()
			except:
				continue
		else:
			msg.append(tmp_key)
		client.send_message("/chatbox/input", [ msg, True, False])
finally:
	curses.endwin()