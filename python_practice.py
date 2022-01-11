counties = ["Arapahoe","Denver","Jefferson"]
counties 
counties[0]
len(counties)
counties[0:2]
counties.append("El Paso")

counties_dict = {"Arapahoe":422829, "Denver":463353, "Jefferson":432438}
counties_dict
len(counties_dict)
counties_dict.items()
counties_dict.keys()
counties_dict.values()
counties_dict.get("Denver")
counties_dict['Denver']
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data