import csv

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# remove unnecessary punctuation chars
def strip_punctuation(string):
    for char in punctuation_chars:
        string = string.replace(char, '')
    return string

# read list of positive words and count them
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
            
def get_pos(string):
    string = strip_punctuation(string)
    pos_count = 0
    for word in string.split():
        if word.lower() in positive_words:
            pos_count += 1
    return pos_count

# read list of negative words and count them
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(string):
    string = strip_punctuation(string)
    pos_count = 0
    for word in string.split():
        if word.lower() in negative_words:
            pos_count += 1
    return pos_count

# read data, process them and write result to a new file
with open('project_twitter_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader, None)  # skip the headers
    with open('resulting_data.csv', 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file)
        csv_writer.writerow(['Number of Retweets', 'Number of Replies',
                         'Positive Score', 'Negative Score', 'Net Score'])
        for row in csv_reader:
            retweets = row[1]
            replies = row[2]
            positive_score = get_pos(row[0]) 
            negative_score = get_neg(row[0]) 
            net_score = positive_score + negative_score
            csv_writer.writerow([retweets, replies, positive_score,
                             negative_score, net_score])
