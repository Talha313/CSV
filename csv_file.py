import csv
items_list=[]
def read():
    with open('med.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        z = '0'
        a = '75000'
        for row in csv_reader:
            name_list = row[1].split(",")
            zip_list = row[2]
            dosage_list = row[3].split(",")
            unit_list = row[4].split(",")
            freq_list = row[5].split(",")
            supply_list = row[6].split(",")
            cost_list = row[7].split(",")
            for counter in range(0,len(name_list)):
                item_dic = {}
                if (counter < len(name_list)):
                    item_dic['name'] = name_list[counter].strip(" ")
                else:
                    item_dic['name']=name_list[0].strip(" ")
                if (len(zip_list) == 0):
                    item_dic['zip'] = a + zip_list
                elif(len(zip_list)<5):
                    item_dic['zip'] =z+zip_list.strip(" ")
                else:
                     item_dic['zip'] = zip_list.strip(" ")

                if (counter < len(dosage_list)):
                    item_dic['dosage'] = dosage_list[counter].strip(" ")
                else:
                    item_dic['dosage'] = dosage_list[0].strip(" ")
                if (counter < len(unit_list)):
                    item_dic['unit'] = unit_list[counter].strip(" ")
                else:
                    item_dic['unit'] = unit_list[0].strip(" ")
                if (counter < len(freq_list)):
                    item_dic['frequency'] = freq_list[counter].strip(" ")
                else:
                    item_dic['frequency'] = freq_list[0].strip(" ")
                if (counter < len(supply_list)):
                    item_dic['supply'] = supply_list[counter].strip(" ")
                else:
                    item_dic['supply'] = supply_list[0].strip(" ")
                item_dic['quantity']=(float(item_dic['frequency']))*(float(item_dic['supply']))
                if (counter < len(cost_list)):
                    item_dic['cost'] = cost_list[counter].strip(" ")
                else:
                    item_dic['cost'] = cost_list[0].strip(" ")
                if item_dic not in items_list:
                    items_list.append(item_dic)
                item_dic['zip']=item_dic['zip']
def write(list):
    with open('med_check.csv', 'w') as f:
       csv_linr = "Name,ZipCode,Unit,Quantity,Cost\n"
       f.write(csv_linr)
       for i in list:
            csv_var=i['name']+","+i['zip']+","+i['dosage']+i['unit']+","+str(i['quantity'])+","+i['cost']+"\n"
            f.write(csv_var)

if __name__ == "__main__":
    read()
   # print(items_list)
    write(items_list)















