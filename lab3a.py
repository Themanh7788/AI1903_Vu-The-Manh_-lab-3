#Q1a:
def print_pattern_number(n):
    for i in range (1,n+1):
        for j in range (1,i+1):
            print(j, end = " ")
        print()
print_pattern_number(5)
#Q1b:
def cal_sum(n):
        return sum(range(1,n+1))
n = int(input("Enter number "))
print("Sum is",cal_sum(n))
#Q2:
number = [46,80,650,450,789,20,45]
for num in number:
    if num > 500:
        break
    if num > 150:
        continue
    if num % 5 == 0:
        print(num)
print(len(number))
#Q2.3
List1 = [10,20,30,40,50]
for num in reversed(List1):
     print(num)
#Q3a:
str = input("original string is:")
def export_word(str):
    length = len(str)
    if length < 4:
         return False
    else:
         middle_start = (length - 4) // 2
    middle_end = middle_start + 4

    result_str = str[middle_start:middle_end]
    return result_str
output_str = export_word(str)

print("Middle four chars are:", output_str)
#Q3b:
def  insert_middle(s1, s2):
    mid = len(s1) // 2
    s3 = s1[:mid] + s2 + s1[mid:]
    return s3
s1 = "Ault"
s2 = "Kelly"
result = insert_middle(s1, s2)
print(result)
#Q3c:
s1 = "America"
s2 = "Japan"
def insert_middle(str):
     mid = len(str)//2
     return str[mid]
combine_word = s1[0] + insert_middle(s1) + s1[-1] + s2[0] + insert_middle(s2)+ s2[-1]
print(combine_word)
#Q3d:
def arrange_characters(s):
    lowercase_chars = [char for char in s if char.islower()]
    uppercase_chars = [char for char in s if char.isupper()]
    arranged_string = ''.join(lowercase_chars + uppercase_chars)
    return arranged_string
str1 = PyNaTive
result = arrange_characters(str1)
print(result)
#Q3e:
str = input("String")
chars = 0
digits = 0
symbols = 0
for i in range(len(str)):
     if('0'<= str[i] and str[i] <= '9'):
          digits +=1
     elif(('a <= str[i]') and str[i] <= 'z') or ('A' <= str[i] and str[i]<= 'Z'):
          chars +=1
     else:
          symbols +=1
print(digits,chars,symbols)
#Q4a:
str1 = 'I am 25 years and 10 months old'
def remove_non_digits(str):
    result = ''.join(char for char in str if char.isdigit())
    return result
result = remove_non_digits(str1)
print(result)
#Q4b:
def remove_empty_strings(lst):
    result = [string for string in lst if string]
    return result
string_list = ["Emma", "Jon", "","Kelly", None, "Eric", ""]
result = remove_empty_strings(string_list)
print(result)
#Q4c:
import string

def remove_special_symbols(str1):
    translator = str.maketrans("", "", string.punctuation)
    result = str1.translate(translator)
    return result
str1 = "/*Jon is @developer & musician"
result = remove_special_symbols(input_string)
print(result)
#Q4d:
def split_on_hyphens(str1):
    result = str1.split("-")
    return result
str1 = "Emma-is-a-data-scientist"
result = split_on_hyphens(str1)
print(result)

