import pandas as pd
import json

df = pd.read_csv("townPriceData.csv")

regions = df["region"].drop_duplicates().tolist()

final_dict = {"regions":[]}

for region in regions:
	final_dict["regions"].append({"region":region,"zones":[]})
	df_region = df[df["region"]==region]
	zones = df_region["zone"].drop_duplicates().tolist()
	for zone in zones:
		final_dict["regions"][-1]["zones"].append({"zone":zone,"towns":[]})
		df_zone = df_region[df_region["zone"]==zone]
		townCodes = df_zone["townCode"].drop_duplicates().tolist()
		for townCode in townCodes:
			df_town = df_zone[df_zone["townCode"]==townCode]
			town = df_town["town"].drop_duplicates().tolist()[0]
			lat = df_town["lat"].drop_duplicates().tolist()[0]
			lon = df_town["lon"].drop_duplicates().tolist()[0]
			final_dict["regions"][-1]["zones"][-1]["towns"].append({"townCode":townCode,"town":town,"lat":lat,"lon":lon,"items":[]})
			products = df_town["item"].drop_duplicates().tolist()
			for product in products:
				df_product = df_town[df_town["item"]==product]
				df_product["date"] = df_product["date"].apply(lambda x: str(x.replace("-","")))
				final_dict["regions"][-1]["zones"][-1]["towns"][-1]["items"].append({"item":product,"data":df_product[["date","price"]].values.tolist()})

with open('townPriceData.json', 'w') as fp:
    json.dump(final_dict, fp, separators=(',', ':'))



# json format:
# {
# 	"regions":
# 		[
# 			{
# 				"region":"Oromiya",
# 				"zones":
# 					[
# 						{
# 							"zone":"Bale",
# 							"towns":
# 								[
# 									{
# 										"town":"Adaba",
# 										"townCode":"411031",
# 										"lat":7.008576013,
# 										"lon":39.390209962,
# 										"data":[["20100301",3.57],["20100401",2.49]]
# 									}
# 								]
# 						}
# 					]

# 			}
# 		]
# }