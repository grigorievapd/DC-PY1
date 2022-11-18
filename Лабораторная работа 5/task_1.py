# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
num = 16
list_of_num_dic = [{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)} for i in range(num)]
pprint(list_of_num_dic)
