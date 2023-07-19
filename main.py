import sys
from os.path import exists
import csv

in_list = []

print(sys.argv)

if len(sys.argv) < 3:
    print("not enough parameters")
    sys.exit()

input_file = sys.argv[1]
output_file = sys.argv[2]

if not exists(sys.argv[1]):
    print("file does not exist")
    sys.exit()

with open(input_file) as file:
    read = csv.reader(file)
    for row in read:
        in_list.append(row)
print(in_list[1])
for parameter in sys.argv[3:]:
    parameter_list = parameter.split(",")
    new_value = ",".join(parameter_list[2:])
    print(parameter_list[0],parameter_list[1], new_value)
    if len(parameter_list) != 3:
        print("Too many or too few values given, no changes saved")
        continue
    column = int(parameter_list[0])
    row = int(parameter_list[1])
    change_value = parameter_list[2]
    if row <0 or row > len(in_list):
        print(f"Row value is less or greater than {len(in_list)}")
        break
    change = in_list[row]
    if column < 0 or column >= len(change):
        print(f"Column value is less or greater than {len(in_list)}")
        break
    change[column] = change_value
    print(f"Value changed row({row}):column({column}) in value{change_value}")
else:
    with open(output_file, 'w', newline='') as file:
        csv.writer(file).writerows(in_list)