# init basic structures
file_value = []
names = {}
tasks = []
grades = []
message = ''


def open_source_file():
    filename = 'students.csv'
    try:
        with open(filename, 'r', encoding='utf-8-sig') as fopen:
            for line in fopen:
                line = line.strip('\n').split(';')
                file_value.append(line)
    except FileNotFoundError as err:
        print('Sorry. File has been not found: ', filename)


def create_split_data():
    for i in range(len(file_value)):
        for j in range(len(file_value)):
            if j < 3:
                for item in file_value:
                    names.setdefault(item[0] + ' ' + item[1] + ' ' + item[2], {}).update({item[3]: item[4]})
            elif j == 3:
                tasks.append(file_value[i][j])
            elif j == 4:
                grades.append(file_value[i][j])


def load_msg_file_and_send():
    message_file = 'message.txt'
    try:
        with open(message_file, 'r', encoding='utf-8-sig') as fopen:
            message = fopen.read()
        for name, task, grade in zip(names, tasks, grades):
            print(message.format(name, task, grade, int(grade) + 1))
    except FileNotFoundError as err:
        print('Sorry. File has been not found: ', message_file)




if __name__ == '__main__':
    open_source_file()
    create_split_data()
    load_msg_file_and_send()
