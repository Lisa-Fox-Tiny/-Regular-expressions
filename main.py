import re
from pprint import pprint
import csv

pattern_from_phone = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
phone_sub = r'+7(\2)-\3-\4-\5 \6\7'



with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


    def structured_data(contact_list):
        new_list = list()
        for element in contacts_list:
            name = ' '.join(element[:3]).split(' ')
            result = [name[0], name[1], name[2], element[3], element[4], re.sub(pattern_from_phone, phone_sub, element[5]), element[6]]
            new_list.append(result)
        return removing_duplicates(new_list)


    def removing_duplicates(info):
        for element in info:
            first_name = element[0]
            last_name = element[1]
            for new_element in info:
                new_first_name = new_element[0]
                new_last_name = new_element[1]
                i = 2
                if first_name == new_first_name and last_name == new_last_name:
                    while i < 7:
                        if element[i] == "": element[i] = new_element[i]
                        i += 1

        result_list = list()
        for el in info:
            if el not in result_list:
                result_list.append(el)

        return result_list


with open("new_phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(structured_data(contacts_list))