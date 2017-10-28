cwd = ''
target_directory = ''

def get_ranges():

	ntype = ['cbr',]

	params = ['energy', 'lost', 'pdr', 'recv', 'sent', 'throughput']

	min_mspeed = 5
	max_mspeed = 35
	mspeed_leaps = 5


	mspeed = range(min_mspeed, max_mspeed + 1, mspeed_leaps)
	


	return [ntype, params, mspeed]


def comparator(first, second, param):

	if param in ['pdr', 'throughput', 'recv']:

		return (float(first) > float(second))

	elif param in ['energy', 'lost', 'sent']:

		return (float(second) > float(first))



def filename_maker(ntype, param, mspeed):

	SEPARATOR = '-'

	filename = str(ntype) + SEPARATOR + str(param) + SEPARATOR + str(mspeed)


	return filename



def filepath_maker(filename):

	windows = 'win'
	linux = 'linux'

	import sys

	platform = sys.platform

	
	SLASH = ''

	if windows in platform:
		SLASH = '\\'

	elif linux in platform:
		SLASH = '/'

	else:
		SLASH = '/'


	path = cwd + SLASH + target_directory + SLASH + filename


	return path

def init():

	import sys
	import os

	global target_directory
	target_directory = sys.argv[1]
	
	global cwd
	cwd = os.getcwd()



def main():
	
	init()

	

	ranges = get_ranges()

	network_type = ranges[0]
	parameter = ranges[1]
	max_speed = ranges[2]

	aodv = 'AODV'
	dsr = 'DSR'

	output_filename  = 'topo_results'

	output = open(output_filename, 'a')

	results = []

	for param in parameter:

		aodv_count = 0
		dsr_count = 0
		either_count = 0
		total_count = 0

		aodv_percent = 0.
		dsr_percent = 0.
		either_percent = 0.

		for mspeed in max_speed:
			for ntype in network_type:

				filename = filename_maker(ntype, param, mspeed)
				filepath = filepath_maker(filename)

			#	print(filename)

				input_file = open(filepath, 'r')

				parts = (input_file.read()).split('\n\n')

			#	print(parts)

				input_file.close()

				first_part = parts[0]
				second_part = parts[1]

				first_part = first_part.split('\n')
				second_part = second_part.split('\n')

				first_part.pop(0)
				first_part.pop(0)

			#	print(first_part)

				second_part.pop(0)

			#	print(second_part)

				for i in range(len(first_part)):

					first_part[i] = first_part[i].split()
					second_part[i] = second_part[i].split()

					first = float(first_part[i][1])
					second = float(second_part[i][1])

					if comparator(first, second, param):
						aodv_count = aodv_count + 1

					elif comparator(second, first, param):
						dsr_count = dsr_count + 1

					elif first == second:
						either_count = either_count + 1
	#	print(param)

		total_count = aodv_count + dsr_count + either_count

		aodv_percent = (float(aodv_count) / total_count) * 100
		dsr_percent = (float(dsr_count) / total_count) * 100
		either_percent = (float(either_count)/ total_count) * 100

		aodv_percent = round(aodv_percent, 2)
		dsr_percent = round(dsr_percent, 2)
		either_percent = round(either_percent, 2)


		result = [param, str(aodv_percent), str(dsr_percent), str(either_percent)]
	#	print(result)

		results.append(result)

	output.write('Model: ' + target_directory + '\n\n')

	for result in results:

		output.write(result[0] + ':' + '\n\n')
	
		output.write(aodv + ': ' + result[1] + ' %' + '\n')
		output.write(dsr + ': ' + result[2] + ' %' +  '\n')
		output.write('Either: ' + result[3] + ' %' + '\n\n')

	output.write('\n\n--------------------------------\n')







main()


















"""

import sys

target_file = sys.argv[1]
file_pointer = open(target_file, 'r')

contents = file_pointer.read()

contents = contents.split('\n')

aodv = 'AODV'
dsr = 'DSR'

aodv_count = 0
dsr_count = 0

for case in contents:

	case = case.split('\n')
	case.pop()
	for entry in case:

		entry = entry.split(' ')

		if entry[1] == aodv:
			aodv_count = aodv_count + 1

		elif entry[1] == dsr:
			dsr_count = dsr_count + 1

total_count = aodv_count + dsr_count

aodv_percent = (float(aodv_count) / total_count) * 100
dsr_percent = (float(dsr_count) / total_count) * 100

print(aodv + ': ' + str(aodv_percent))
print(dsr + ': ' + str(dsr_percent))




"""