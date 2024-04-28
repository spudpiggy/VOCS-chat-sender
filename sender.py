import pythonosc as osc
import tomllib as toml
import argparse

with open('config.toml', 'rb') as f:
	config = toml.load(f)
print(config['defaultDevice'])