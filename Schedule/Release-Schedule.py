import re
from datetime import datetime, timedelta


def string_to_datetime(date_string):
    fields = re.split('\W+', date_string)
    ans = datetime(int(fields[2]), int(fields[1]), int(fields[0]),
                   int(fields[3]), int(fields[4]), int(fields[5]),
                   int(fields[6][:-1] if len(fields) == 7 else fields[6]) * 1000)

    if len(fields) == 8:
        offset = int(fields[7]) * (-1 if date_string[-5] == '-' else 1)
        if offset < -1:
            delta = timedelta(0, 0, 0, 0, abs(offset % 100), abs(offset // 100))
            ans += delta
        else:
            delta = timedelta(0, 0, 0, 0, offset % 100, offset // 100)
            ans -= delta

    return ans


def code(json_file):
    time_list = []
    it_data = json_file[0].split(';')

    it_start = string_to_datetime(it_data[1])
    it_end = string_to_datetime(it_data[2])

    time_list.append((it_start, 0))
    time_list.append((it_end, 0))

    for task in json_file[1:]:
        task_data = task.split(';')
        task_start = string_to_datetime(task_data[1])
        task_end = string_to_datetime(task_data[2])

        time_list.append((task_start, 1))
        time_list.append((task_end, -1))

    time_list.sort()

    start_checking = False
    ans = 0
    task_counter = 0
    for i in range(len(time_list)):
        entry = time_list[i]
        if entry[1] == 0:
            if not start_checking:
                start_checking = True
            else:
                break

        task_counter += entry[1]
        if task_counter == 0:
            ans = max(ans, (time_list[i + 1][0] - entry[0]).total_seconds())

    return int(ans)


# print(code(["3;28-05-2017 13:00:00.000+0800;28-05-2017 16:00:00.000+0800",
#       "London morning trading check;28-05-2017 05:15:00.000Z;28-05-2017 06:15:00.000Z",
#       "Tokyo risk testing;28-05-2017 16:15:00.000+0900;28-05-2017 16:45:00.000+0900",
#       "New York midnight database check;28-05-2017 03:50:00.000-0400;28-05-2017 03:59:00.000-0400"]))
