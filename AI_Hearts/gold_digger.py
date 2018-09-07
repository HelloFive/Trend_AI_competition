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

#	print is_data_filtered_correctly(data_cleaned_player2)
#	print is_data_filtered_correctly(data_cleaned_player3)
#	print is_data_filtered_correctly(data_cleaned_player4)	
	clean_data(data_cleaned_player1)
	print("Data count %s"%len(data_cleaned_player1))
	with open("jason.txt", "w") as file:
		for deal in data_cleaned_player1:
			for _round in deal:
				for log in _round:
					if "serverRandom': T" in log:
						#import pdb; pdb.set_trace()
						pass
					file.write(log)
	
def clean_data(data):
	removal_data=[]
	for deal in data:
		for _round in deal:
			broken = False
			for log in _round:
				if "serverRandom': T" in log:
					print(data.index(deal))
					removal_data.append(deal)
					broken = True
					break
			if broken:
				break
	for deal in removal_data:
		data.remove(deal)
	print("Data count %s"%len(data))

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
        deal_count = -1
        round_count = 0
	is_first_round = True

	initial_logs = []
	
        for line in data:
		if "INFO new_deal" in line:
			print("Round Count: %s"%(round_count+1))
			deal_count += 1
			round_count = 0
			is_first_round = True
			data_cleaned.append([])
			data_cleaned[deal_count].append([])
			if len(initial_logs) > 0:
				data_cleaned[deal_count][round_count] = initial_logs
				initial_logs = []
			data_cleaned[deal_count][round_count].append(line)
		elif "INFO new_round" in line:
			if is_first_round:
				is_first_round = False
			else:
				round_count += 1
				data_cleaned[deal_count].append([])
			data_cleaned[deal_count][round_count].append(line)
		else:
			if deal_count <0:
				initial_logs.append(line)
			else:
				data_cleaned[deal_count][round_count].append(line)
			
	print("Deal count: %s"%(deal_count+1))



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
