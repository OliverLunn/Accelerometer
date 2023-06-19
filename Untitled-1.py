import re
string = "acc average x,y,z pk x,y,z (g) = -0.007, -0.033, -1.000, 0.010, 0.025, 0.028"
#string = string.replace(" ", "")
#string = re.sub("[^0-9.,-_]", "", string)

print(string)


string_1 = string.split()
avg_acc_z = string_1[7]
pk_acc_z = string_1[12]
print(avg_acc_z, pk_acc_z)
