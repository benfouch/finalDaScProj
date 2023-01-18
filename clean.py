import os
import pandas as pd


# I think the algo needs to be like this:
# Read the first field: id
# Last field will then be: "https://redd.it/<id>"
# Read from first field until last field 
# Title starts at 13 in the list
# If is_self is True then we have text post as well under the column "self"



class Record():
    
    def __init__(self):
        self.id = None
        self.author = None
        self.created = None
        self.retrieved = None
        self.edited = None
        self.pinned = None
        self.archived = None
        self.locked = None
        self.removed = None
        self.deleted = None
        self.is_self = None
        self.is_video = None
        self.is_original_content = None
        self.title = None
        self.link_flair_text = None
        self.upvote_ratio = None
        self.score = None
        self.gilded = None
        self.total_awards_received = None
        self.num_comments = None
        self.num_crossposts = None
        self.selftext = None
        self.thumbnail = None
        self.shortlink = None
        
    def pretty_print(self):
        print('***************************************')

        for attr, value in self.__dict__.items():
            print(f'{attr}: {value}')
            
        print('***************************************')


    
    










#############################################
# Routine
#############################################

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
        for line in contents:
            
            if start:
                
                id = line.split(',')[0].replace('"', '')
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
    
        
        return all_records



def write_to_csv(records, filename):
    data = [record.__dict__ for record in records]
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    
    

def fix_records(records):
    
    record_objects = []
    for x in records:
        r = f(x)
        if r != -1:
            record_objects.append(r)
            r.pretty_print()
    return record_objects
            
    

def f(record):
    """ 
    Fixes one title
    Titles always start at index 13 when splitting by commas
    """
    result = Record()
    
    # splits record on commas
    x = record.split(',')
    result.id = x[0].replace('\"', '')
    result.author = x[1].replace('\"', '')
    result.created = x[2].replace('\"', '')
    result.retrieved = x[3].replace('\"', '')
    result.edited = x[4].replace('\"', '')
    result.pinned = x[5]
    result.archived = x[6]
    result.locked = x[7]
    result.removed = x[8]
    result.deleted = x[9]
    result.is_self = x[10]
    result.is_video = x[11]
    result.is_original_content = x[12]
    

    
    
    
    
    title = ''
    # start index (where title starts in every csv file)
    index = 13
    flag = True
    
    # loop until you can convert the input to float
    # save the index
    while flag:

        title = title + x[index]
        index = index + 1
        try:
            float(x[index])
            flag = False
        except ValueError:
            flag = True
    
    title_split = title.split('"')
    title_split = [x for x in title_split if x != '']
    
    # If length was less than 2 there was an error
    if len(title_split) < 2:
        return -1
    
    # If the length is greater than 2 than we had quotes in the title
    elif len(title_split) > 2:
        result.link_flair_text = title_split[-1]
        title_split.pop()
        title_split = " ".join(x for x in title_split)
        result.title = title_split[0].replace('\n', '')
       
    # if length equal to two this is normal case
    # it has the title and link flair text
    elif len(title_split) == 2: 
        result.link_flair_text = title_split[-1]
        title_split.pop()
        result.title = title_split[0].replace('\n', '')

    
    # Numbers are easy to work with
    # Assigning all the values from title to selftext here
    
    result.upvote_ratio = x[index]
    result.score = x[index + 1]
    result.gilded = x[index + 2]
    result.total_awards_received = x[index + 3]
    result.num_comments = x[index + 4]
    result.num_crossposts = x[index + 5]
    index = index + 6

    # selftext is all text except last two which are shortlink and thumbnail
    selftext_intermediate = " ".join(y for y in x[index:-2])
    result.selftext = selftext_intermediate.replace("\"", '').replace('\n', '')
    result.thumbnail = x[-2].replace("\"", '')
    result.shortlink = x[-1].replace("\"", '').replace('\n', '')
    

    
    
    
    
    return result
    


if __name__ == '__main__':
    
    data = os.path.join('Data','dummy.csv')
    
    records = read_records(data)
    records = fix_records(records)
    write_to_csv(records, 'dummy_text_clean.csv')
    # pretty_print_records(records)
    