import pandas as pd
import re
import datetime
import os

def detect_ECOS_file():
	ECOS_list = []
	parent_dir = os.getcwd()
	file_list = os.listdir(parent_dir)
	for i in file_list:
		if i[0:4] == "ECOS":
			ECOS_list.append(i)
	return ECOS_list[0]

def load_excel():
	file_name = detect_ECOS_file()
	df = pd.read_excel(file_name)
	dropped_df = df.iloc[:-2]
	new_df = dropped_df.drop(index=0)
	return new_df

def targeted_template(file_name):
	df = pd.read_excel(file_name)
	columns_names = get_columns_names(df)
	return df

def get_columns_values(df):
	content_list = []
	column_list = list(df.columns.values)
	for i in column_list:
		content_list.append(df[i].tolist())
	return content_list

def convert_df(content_list):
	a = []
	for i in range(len(content_list[0])+1):
		a.append("")
	plantNo = []
	for b in range(len(content_list[0])+1):
		plantNo.append("WH15")
	plantName = []
	for c in range(len(content_list[0])+1):
		plantName.append("印尼")
	orderNo = []
	for d in range(len(content_list[0])+1):
		orderNo.append("SMILIDNORDER")
	brand = []
	for e in range(len(content_list[0])+1):
		brand.append("MG")
	materialNo = content_list[9]
	BOMVersion = []
	for x in range(len(content_list[0])+1):
		BOMVersion.append("20240125")
	product = []
	for h in content_list[9]:
		if str(h)[0:3] == "MGN":
			product.append("EH3")
		else:
			product.append("US1")
	modelYear = []
	for i in content_list[9]:
		if str(i)[0:3] == "MGN":
			modelYear.append("2022")
		else:
			modelYear.append("2021")
	VIN = content_list[1]
	PINCODE = content_list[2]
	PN = []
	for i in PINCODE:
		if "'" in i:
			init_value = i[1:]
			value = int(str(init_value), 16)
			PN.append(value)
		else:
			value = int(str(i), 16)
			PN.append(value)
	finishTime = content_list[7]
	VHCModel = []
	for j in content_list[9]:
		if str(j)[0:2] == "MG":
			if str(j)[5:6] == "D":
				VHCModel.append("EH3DP2")
			else:
				VHCModel.append("EH3CP2")
		elif str(j)[0:2] == "MD":
			if str(j)[5:6] == "D":
				VHCModel.append("US1D26")
			else:
				VHCModel.append("US1C26")
	engineNo = a
	data_in_list = [[plantNo], [plantName], [orderNo], [brand], [materialNo], [BOMVersion], [product], [modelYear], [VIN], [PN], [finishTime], [VHCModel], [engineNo]]
	df = pd.DataFrame(list(zip(plantNo, plantName, orderNo, brand, materialNo, 
									BOMVersion, product, modelYear, VIN, PN, finishTime, 
									VHCModel, engineNo)), 
	columns=["Plant No", "Plant Name", "Order No", "Brand", "Material  No", 
								"BOM Version", "Product", "Model Year", "VIN", "PN", "Finish Time", 
								"VHC Model", "Engine No"])
	return data_in_list, df

def write_file(dataframe):
	file_name = detect_ECOS_file()
	dataframe.to_excel(f"{file_name[5:]}Done.xlsx", index=False)

def generate_subfiles(dataframe):
	row_value_list = []
	for index, rows in dataframe.iterrows():
		row_value_list.append(rows)
	return row_value_list

def __main__():
	df = load_excel()
	column = get_columns_values(df)
	data_in_list, df_converted = convert_df(column)
	#row_value_list = generate_subfiles(df_converted)
	#print(data_in_list)
	#print(df_converted)
	write_file(df_converted)
	#file_list = detect_ECOS_file()
	#print(file_list)
__main__()