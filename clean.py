import os



# I think the algo needs to be like this:
# Read the first field: id
# Last field will then be: "https://redd.it/<id>"
# Read from first field until last field 
# Title starts at 13 in the list
# If is_self is True then we have text post as well under the column "self"


def read_records(file):
    """
    Reads csv file into unique records
    Returns a list of all records in the csv file
    """
    with open(file, 'r+', encoding="utf8") as f:
        # 13 commas before title
        headers = f.readline()
        print(headers)
        print('\n\n')
        contents = f.readlines()
        print(f'Length of contents: {len(contents)}')
        start = True
        all_records = []
        record = ''
        id = ''
        i = 0
        for line in contents[0:50]:
            print(f"INDEX:{i}")
            if start:
                print("in start")
                id = line.split(',')[0].replace('"', '')
                print(id)
                start = False
            # if there is a link with the same id as the beginning id 
            # print(line.split(',')[-1].replace('"', ''))
            # print(id)
            if id in line.split(',')[-1]: 
                record = record + line
                all_records.append(record)
                record = ''
                start = True
            else:
                
                record = record + line
            i += 1
    
        # for r in all_records:
        #     print(r)
        return all_records


def pretty_print_records(records):
    for x in records:
        pp_records(x)
        

def pp_records(x):
    print('***************************************')
    print('Record:')
    print(x)
    print('***************************************')
    

def fix_title(records):
    pass


if __name__ == '__main__':
    
    data = os.path.join('Data','dummy.csv')
    
    records = read_records(data)
    # fix_title(records)
    
    pretty_print_records(records)
    