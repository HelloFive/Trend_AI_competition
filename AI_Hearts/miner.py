import os
import argparse

def main(cli_args):
	player1_data = []
	player2_data = []
	player3_data = []
	player4_data = []
	table_data = []
	with open(os.path.join("/home/admin/tanil/trend-hearts-1.0.0-alpha.7/sample_bot_v1.0.3", cli_args.player1_file), "r") as file:
		player1_data = file.readlines()
	with open(os.path.join("/home/admin/tanil/trend-hearts-1.0.0-alpha.7/sample_bot_v1.0.3", cli_args.player2_file), "r") as file:
		player2_data = file.readlines()
	with open(os.path.join("/home/admin/tanil/trend-hearts-1.0.0-alpha.7/sample_bot_v1.0.3", cli_args.player3_file), "r") as file:
		player3_data = file.readlines()
	with open(os.path.join("/home/admin/tanil/trend-hearts-1.0.0-alpha.7/sample_bot_v1.0.3", cli_args.player4_file), "r") as file:
		player4_data = file.readlines()
	with open(os.path.join("/home/admin/tanil/trend-hearts-1.0.0-alpha.7/logs", cli_args.table_file, "common.log"), "r") as file:
		table_data = file.readlines()
		
		
	deal_num_table = parse_table(table_data)
	deal_num_player1 = parse_player(player1_data)
	deal_num_player2 = parse_player(player2_data)
	deal_num_player3 = parse_player(player3_data)
	deal_num_player4 = parse_player(player4_data)
	
	deal_num_smallest = min([deal_num_table, deal_num_player1, deal_num_player2, deal_num_player3, deal_num_player4])
	print 'jasonp: smallest=', deal_num_smallest

## Things to Do:
## 	1. table with upto the deal_count
## 	2. is_data_filtered_correctly function wrong or the data is not valid.
	
	data_cleaned_player1 = []
	data_cleaned_player2 = []
	data_cleaned_player3 = []
	data_cleaned_player4 = []

	parse_player_upto_deal(player1_data, deal_num_smallest, data_cleaned_player1)
#	parse_player_upto_deal(player2_data, deal_num_smallest, data_cleaned_player2)
#	parse_player_upto_deal(player3_data, deal_num_smallest, data_cleaned_player3)
#	parse_player_upto_deal(player4_data, deal_num_smallest, data_cleaned_player4)

	print "JASONP_LOG: is_data_filtered_correctly(data_cleaned_player1)=",is_data_filtered_correctly(data_cleaned_player1)
#	print is_data_filtered_correctly(data_cleaned_player2)
#	print is_data_filtered_correctly(data_cleaned_player3)
#	print is_data_filtered_correctly(data_cleaned_player4)	

	import pdb; pdb.set_trace()	
	pass


def is_data_filtered_correctly(data_cleaned):
	for list_of_list in data_cleaned:
		boolean = 1
		for list1 in list_of_list:
			if "u'serverRandom': True" in list1:
				boolean *= 0
				data_cleaned.remove(list_of_list)
				print "data_filtered"
				break
			else:
				boolean *= 1	
	return boolean

###HERE: why do I get false result here!???			


#def parse_table_upto_deal(data, deal_num_smallest, data_cleaned):
#	deal_count = 0
#	is_deal_1_appeared = 0
#	list_of_one_deal = []
#	for line in data:
#		if ">>> >> response: new_deal" in line:
#			continue:
#		else if ">>> >> response: new_round" in line:
#			continue:
 

def parse_player_upto_deal(data, deal_num_smallest, data_cleaned):
        deal_count = 0
        round_count = 0
        list_of_one_deal = []
        list_of_one_round = []
	
        #for line in data:
	#	if "INFO new_deal" in line:
	#		deal_count += 1
			












                if deal_count == deal_num_smallest:
                        list_of_one_deal.append(list_of_one_round)
                        data_cleaned.append(list_of_one_deal)
                        list_of_one_round = []
                        list_of_one_deal = []
                        break
                elif "INFO new_deal" in line:
			#print "INFO new_deal"
                        if deal_count != 0:
                                data_cleaned.append(list_of_one_deal)
                                list_of_one_deal = []
                        list_of_one_deal.append(line)
                        deal_count += 1
                        print "round_count=", round_count
			if round_count != 13:
				print line
                        round_count = 0
                elif "INFO new_round" in line:
                		if round_count != 0:
                			list_of_one_deal.append(list_of_one_round)
                		list_of_one_round = []
                		round_count += 1
                else:
                        list_of_one_round.append(line)
        print "deal_count=", deal_count



def parse_player(data):
	deal_number = 0
	for line in data:
		if "INFO new_deal" in line:
			deal_number += 1
	print 'parse_player: deal_number = ', deal_number
	return deal_number

def parse_table(data):
	deal_number = 0
	for line in data:
		if "response: new_deal" in line:
			deal_number += 1
	print 'parse_table: deal_number = ', deal_number
	return deal_number

def configure_parser():
	parser = argparse.ArgumentParser(description="gold diggers parameters")
	parser.add_argument("player1_file", type=str)
	parser.add_argument("player2_file", type=str)
	parser.add_argument("player3_file", type=str)
	parser.add_argument("player4_file", type=str)
	parser.add_argument("table_file", type=str)
	return parser
	
if __name__ == '__main__':
	cli_parser = configure_parser()
	main(cli_parser.parse_args())
