import pandas as pd

file_name = "dataset.xlsx"


def get_yearly_count(api_well_number):
    flag = False
    xl_file = pd.read_excel(file_name)
    data_lst = []
    oil_lst = []
    gas_lst = []
    brine_lst = []
    yearly_count = []
    if not xl_file.empty:
        for index, row in xl_file.iterrows():
            data_lst.append({"API WELL NUMBER": (row["API WELL  NUMBER"]), "QUARTER": row["QUARTER 1,2,3,4"],
                             "OIL": row["OIL"], "GAS": row["GAS"], "BRINE": row["BRINE"], "TOWNSHIP": row["TOWNSHIP"], "COUNTY": row["COUNTY"],
                             "Production Year": row["Production Year"], "WELLNAME": row["WELL NAME"], "WELLNUMBER": row["WELL NUMBER"], "DAYS": row["DAYS"]})
    for data in data_lst:
        if data["API WELL NUMBER"] == api_well_number:
            flag = True
            oil_lst.append(data["OIL"])
            gas_lst.append(data["GAS"])
            brine_lst.append(data["BRINE"])
    yearly_count.append({"API WELL NUMBER": api_well_number, "OIL": sum(oil_lst),
                         "GAS": sum(gas_lst), "BRINE": sum(brine_lst), "TOWNSHIP": data["TOWNSHIP"], "COUNTY": data["TOWNSHIP"],
                         "Production Year": data["Production Year"], "WELLNAME": data["WELLNAME"], "WELLNUMBER": data["WELLNUMBER"],"DAYS": data["DAYS"]})
    if flag:
        return yearly_count[0]
    else:
        return False

