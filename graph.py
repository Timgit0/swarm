from matplotlib import pyplot as plt

# FileNumbers = [2, 3, 4, 5, 6, 7, 8, 9]
FileNumbers = [2, 3]
start_of_file_name = "results"
end_of_the_file_name = ".txt"


def number_from_string(string):
    number = ""
    for j in string:
        if j in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            number += j
        else:
            break
    return int(number)


def success_or_fail_from_string(string):
    answer = ""
    for j in string:
        if j not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "\n", " "]:
            answer += j
    return answer


for num in FileNumbers:
    File = start_of_file_name + str(num) + end_of_the_file_name
    with open(File, "r") as file:
        file_max = 0
        for i in file.readlines():
            file_max = max(file_max, (number_from_string(i)))
    file_max += 1
    x = list(range(file_max))
    y = [0] * file_max
    with open(File, "r") as file:
        for i in file.readlines():
            if success_or_fail_from_string(i) == "success":
                y[number_from_string(i)] += 1
    plt.plot(x, y, label="successes" + str(num), color=(0, 1/10*num, 0))


plt.xlim(0, 150)
plt.legend()
plt.show()
