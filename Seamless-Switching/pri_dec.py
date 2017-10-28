""" Global Variables """

target_directory = ''
cwd = ''



def get_ranges():

	ntype = ['cbr',]
	
	min_mspeed = 5
	max_mspeed = 35
	mspeed_leaps = 5

	"""
	min_nodes = 20
	max_nodes = 70
	nodes_leaps = 5
	"""
	
	mspeed = range(min_mspeed, max_mspeed + 1, mspeed_leaps)
#	nodes = range(min_nodes, max_nodes + 1, nodes_leaps)


	return [ntype, mspeed]



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



def decision_maker(first_list, second_list, first_protocol, second_protocol):
	""" Here first refers to AODV, second refers to DSR """

	if first_protocol == 'AODV' and second_protocol == 'DSR':

		aodv_energy = first_list[0]
		aodv_throughput = first_list[1]
		aodv_lost = first_list[2]
		aodv_pdr = first_list[3]
		aodv_sent = first_list[4]
		aodv_recv = first_list[5]


		dsr_energy = second_list[0]
		dsr_throughput = second_list[1]
		dsr_lost = second_list[2]
		dsr_pdr = second_list[3]
		dsr_sent = second_list[4]
		dsr_recv = second_list[5]

	elif first_protocol == 'DSR' and second_protocol == 'AODV':

		dsr_energy = first_list[0]
		dsr_throughput = first_list[1]
		dsr_lost = first_list[2]
		dsr_pdr = first_list[3]
		dsr_sent = first_list[4]
		dsr_recv = first_list[5]


		aodv_energy = second_list[0]
		aodv_throughput = second_list[1]
		aodv_lost = second_list[2]
		aodv_pdr = second_list[3]
		aodv_sent = second_list[4]
		aodv_recv = second_list[5]

	#decision making

	protocol = ''

	aodv = 0
	dsr = 0

	#energy begins

	if (aodv_energy < dsr_energy):
		aodv = aodv + 8

	elif (dsr_energy < aodv_energy):
		dsr = dsr + 8

	else:
		aodv = aodv + 4
		dsr = dsr + 4

	#energy ends


	#throughput begins

	if (aodv_throughput > dsr_throughput):
		aodv = aodv + 32

	elif (dsr_throughput > aodv_throughput):
		dsr = dsr + 32

	else:
		aodv = aodv + 16
		dsr = dsr + 16

	#throughput ends


	#lost begins

	if (aodv_lost < dsr_lost):
		aodv = aodv + 16

	elif (dsr_lost < aodv_lost):
		dsr = dsr + 16

	else:
		aodv = aodv + 8
		dsr = dsr + 8

	#lost ends


	#pdr begins

	if (aodv_pdr > dsr_pdr):
		aodv = aodv + 4

	elif (dsr_pdr > aodv_pdr):
		dsr = dsr + 4

	else:
		aodv = aodv + 2
		dsr = dsr + 2

	#pdr ends


	#sent begins

	if (aodv_sent > dsr_sent):
		aodv = aodv + 2

	elif (dsr_sent > aodv_sent):
		dsr = dsr + 2

	else:
		aodv = aodv + 1
		dsr = dsr + 1

	#sent ends


	#recv begins

	if (aodv_recv > dsr_recv):
		aodv = aodv + 2

	elif (dsr_recv > aodv_recv):
		dsr = dsr + 2

	else:
		aodv = aodv + 1
		dsr = dsr + 1

	#recv ends


	if aodv > dsr:
		protocol = 'AODV'

	elif dsr > aodv:
		protocol = 'DSR'

	else:
		protocol = 'AODV/DSR'



	return protocol







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

	ntype = ranges[0]
	mspeed = ranges[1]

#	parameters = get_parameters()

	""" modify below list as parameters change """
	energy = 'energy'
	throughput = 'throughput'
	lost = 'lost'
	pdr = 'pdr'
	sent = 'sent'
	recv = 'recv'


	energy_file = None
	throughput_file = None
	lost_file = None
	pdr_file = None
	sent_file = None
	recv_file = None


	output_file = open(target_directory + '_results', 'w')

	for ntype_value in ntype:
		
		for mspeed_value in mspeed:

			#energy begins
			filename = filename_maker(ntype_value, energy, mspeed_value)
			filepath = filepath_maker(filename)

			energy_file = open(filepath, 'r')

			
			parts = (energy_file.read()).split('\n\n')

			energy_file.close()

			energy_firstpart = parts[0]
			energy_secondpart = parts[1]

			energy_firstpart = energy_firstpart.split('\n')
			energy_secondpart = energy_secondpart.split('\n')

			first_line = energy_firstpart.pop(0)

			# One time job. This porion can be ignored for subsequent parameters.
			title = first_line.split()
			title = 'NetworkType-' + title[1] + ' MaxSpeed-' + title[5]
			#


			first_heading = energy_firstpart.pop(0)
			second_heading = energy_secondpart.pop(0)


			# One time job. This porion can be ignored for subsequent parameters.
			first_protocol = first_heading[1:-1]
			second_protocol = second_heading[1:-1]
			#


			for i in range(len(energy_firstpart)):
				energy_firstpart[i] = energy_firstpart[i].split()

			for i in range(len(energy_secondpart)):
				energy_secondpart[i] = energy_secondpart[i].split()
			#energy ends

			

			#throughput begins
			filename = filename_maker(ntype_value, throughput, mspeed_value)
			filepath = filepath_maker(filename)

			throughput_file = open(filepath, 'r')


			parts = (throughput_file.read()).split('\n\n')

			throughput_file.close()

			throughput_firstpart = parts[0]
			throughput_secondpart = parts[1]

			throughput_firstpart = throughput_firstpart.split('\n')
			throughput_secondpart = throughput_secondpart.split('\n')

			first_line = throughput_firstpart.pop(0)

			# One time job. Already done once.
		#	title = first_line.split()
		#	title = 'NetworkType-' + title[1] + ' Mobility-' + title[3] + 'MaxSpeed-' + title[6]
			#


			first_heading = throughput_firstpart.pop(0)
			second_heading = throughput_secondpart.pop(0)


			# One time job. Already done once.
		#	first_protocol = first_heading[1:-1]
		#	second_protocol = second_heading[1:-1]
			#


			for i in range(len(throughput_firstpart)):
				throughput_firstpart[i] = throughput_firstpart[i].split()

			for i in range(len(throughput_secondpart)):
				throughput_secondpart[i] = throughput_secondpart[i].split()
			#throughput ends

			#lost begins
			filename = filename_maker(ntype_value, lost, mspeed_value)
			filepath = filepath_maker(filename)

			lost_file = open(filepath, 'r')


			parts = (lost_file.read()).split('\n\n')

			lost_file.close()

			lost_firstpart = parts[0]
			lost_secondpart = parts[1]

			lost_firstpart = lost_firstpart.split('\n')
			lost_secondpart = lost_secondpart.split('\n')

			first_line = lost_firstpart.pop(0)

			# One time job. Already done once.
		#	title = first_line.split()
		#	title = 'NetworkType-' + title[1] + ' Mobility-' + title[3] + 'MaxSpeed-' + title[6]
			#


			first_heading = lost_firstpart.pop(0)
			second_heading = lost_secondpart.pop(0)


			# One time job. Already done once.
		#	first_protocol = first_heading[1:-1]
		#	second_protocol = second_heading[1:-1]
			#


			for i in range(len(lost_firstpart)):
				lost_firstpart[i] = lost_firstpart[i].split()

			for i in range(len(lost_secondpart)):
				lost_secondpart[i] = lost_secondpart[i].split()
			#lost ends

			#pdr begins
			filename = filename_maker(ntype_value, pdr, mspeed_value)
			filepath = filepath_maker(filename)

			pdr_file = open(filepath, 'r')


			parts = (pdr_file.read()).split('\n\n')

			pdr_file.close()

			pdr_firstpart = parts[0]
			pdr_secondpart = parts[1]

			pdr_firstpart = pdr_firstpart.split('\n')
			pdr_secondpart = pdr_secondpart.split('\n')

			first_line = pdr_firstpart.pop(0)

			# One time job. Already done once.
		#	title = first_line.split()
		#	title = 'NetworkType-' + title[1] + ' Mobility-' + title[3] + 'MaxSpeed-' + title[6]
			#


			first_heading = pdr_firstpart.pop(0)
			second_heading = pdr_secondpart.pop(0)


			# One time job. Already done once.
		#	first_protocol = first_heading[1:-1]
		#	second_protocol = second_heading[1:-1]
			#


			for i in range(len(pdr_firstpart)):
				pdr_firstpart[i] = pdr_firstpart[i].split()

			for i in range(len(pdr_secondpart)):
				pdr_secondpart[i] = pdr_secondpart[i].split()
			#pdr ends


			#sent begins
			filename = filename_maker(ntype_value, sent, mspeed_value)
			filepath = filepath_maker(filename)

			sent_file = open(filepath, 'r')


			parts = (sent_file.read()).split('\n\n')

			sent_file.close()

			sent_firstpart = parts[0]
			sent_secondpart = parts[1]

			sent_firstpart = sent_firstpart.split('\n')
			sent_secondpart = sent_secondpart.split('\n')

			first_line = sent_firstpart.pop(0)

			# One time job. Already done once.
		#	title = first_line.split()
		#	title = 'NetworkType-' + title[1] + ' Mobility-' + title[3] + 'MaxSpeed-' + title[6]
			#


			first_heading = sent_firstpart.pop(0)
			second_heading = sent_secondpart.pop(0)


			# One time job. Already done once.
		#	first_protocol = first_heading[1:-1]
		#	second_protocol = second_heading[1:-1]
			#


			for i in range(len(sent_firstpart)):
				sent_firstpart[i] = sent_firstpart[i].split()

			for i in range(len(sent_secondpart)):
				sent_secondpart[i] = sent_secondpart[i].split()
			#sent ends

			#recv begins
			filename = filename_maker(ntype_value, recv, mspeed_value)
			filepath = filepath_maker(filename)

			recv_file = open(filepath, 'r')


			parts = (recv_file.read()).split('\n\n')

			recv_file.close()

			recv_firstpart = parts[0]
			recv_secondpart = parts[1]

			recv_firstpart = recv_firstpart.split('\n')
			recv_secondpart = recv_secondpart.split('\n')

			first_line = recv_firstpart.pop(0)

			# One time job. Already done once.
		#	title = first_line.split()
		#	title = 'NetworkType-' + title[1] + ' Mobility-' + title[3] + 'MaxSpeed-' + title[6]
			#


			first_heading = recv_firstpart.pop(0)
			second_heading = recv_secondpart.pop(0)


			# One time job. Already done once.
		#	first_protocol = first_heading[1:-1]
		#	second_protocol = second_heading[1:-1]
			#


			for i in range(len(recv_firstpart)):
				recv_firstpart[i] = recv_firstpart[i].split()

			for i in range(len(recv_secondpart)):
				recv_secondpart[i] = recv_secondpart[i].split()
			#recv ends

			#comparison and decision making
			decision_list = []

			for i in range(len(energy_firstpart)):

				nodes = energy_firstpart[i][0]

				first_energyvalue = float(energy_firstpart[i][1])
				first_throughputvalue = float(throughput_firstpart[i][1])
				first_lostvalue = float(lost_firstpart[i][1])
				first_pdrvalue = float(pdr_firstpart[i][1])
				first_sentvalue = float(sent_firstpart[i][1])
				first_recvvalue = float(recv_firstpart[i][1])


				second_energyvalue = float(energy_secondpart[i][1])
				second_throughputvalue = float(throughput_secondpart[i][1])
				second_lostvalue = float(lost_secondpart[i][1])
				second_pdrvalue = float(pdr_secondpart[i][1])
				second_sentvalue = float(sent_secondpart[i][1])
				second_recvvalue = float(recv_secondpart[i][1])


				first_list = [first_energyvalue, first_throughputvalue, first_lostvalue, first_pdrvalue, first_sentvalue,first_recvvalue]
				second_list = [second_energyvalue, second_throughputvalue, second_lostvalue, second_pdrvalue, second_sentvalue, second_recvvalue]

				protocol = decision_maker(first_list, second_list, first_protocol, second_protocol)

				decision_list.append([nodes, protocol])



			output_file.write(title + '\n')

			for entry in decision_list:
				output_file.write(entry[0] + ' ' + entry[1] + '\n')

			output_file.write('\n')

	output_file.close()



main()