"""
Provide info on US presidents
"""
from datetime import date
from pprint import pprint

def mkdate(raw_date):
    """
    Convert date string in form 'YYYY-MM-DD' to Python date object. 
    """
    if raw_date != "NONE":
        raw_year, raw_month, raw_day = raw_date.split('-')
        d = date(int(raw_year), int(raw_month), int(raw_day))
    else:
        d = None

    return d

def get_info(index):
    """
    Return dictionary of info for one US President.

    Argument: term number as integer
    """
    with open("../DATA/presidents.txt", encoding="utf8") as pres_in:
        for raw_line in pres_in:
            line = raw_line.rstrip()  # remove  \n
            if line and (line.count(':') == 9):  # if line is not empty string
                flds = line.split(":")
                if int(flds[0]) == index:
                    pres_data = {}
                    pres_data["lastname"] = flds[1]
                    pres_data["firstname"] = flds[2]

                    pres_data["birthdate"] = mkdate(flds[3])
                    pres_data["deathdate"] = mkdate(flds[4])

                    pres_data["birthplace"] = flds[5]
                    pres_data["birthstate"] = flds[6]

                    pres_data["termstart"] = mkdate(flds[7])
                    pres_data["termend"] = mkdate(flds[8])

                    pres_data["party"] = flds[9]

                    return pres_data
                    break

    raise ValueError("Invalid term #")

def get_all_data():
    all_data = []
    for i in range(1, 48):
        all_data.append(get_info(i))
    return all_data

if __name__ == "__main__":
    pres = get_info(18)
    print(pres)
    print('-' * 60)
    pprint(get_all_data())
    pres = get_info(48)
