import argparse

try:
    input = raw_input

except Exception as e:
    pass


def promptWithDefault(text, default = ''):
	strPrompt  = text + "["+ str(default) + "]:"


	d = input(strPrompt)

	if ("" == d):
		d = default
	return d
