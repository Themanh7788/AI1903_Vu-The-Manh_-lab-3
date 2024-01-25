#Q1:
str1 = "parliament"
str2 = "partial men"
def is_anagram(str1: str, str2: str) ->bool:
    str1 = ''.join(e for e in str1 if e.isalnum()).lower()
    str2 = ''.join(e for e in str2 if e.isalnum()).lower()
    str1_sorted = sorted(str1)
    str2_sorted = sorted(str2)
    return str1_sorted == str2_sorted
if is_anagram(str1, str2):
    print(f"{str1} are anagrams of {str2}")
else:
    print(f"{str1} are not anagrams of {str2}")
#Q2:
def check_hexa(input_str):
    try:
        int(input_str, 16)
        return True
    except ValueError:
        return False

def main():
    user_input = input("Enter a string: ")

    if check_hexa(user_input):
        decimal_value = int(user_input, 16)
        print(f"The base-10 value is: {decimal_value}")
    else:
        print("Error: Not all characters are hexadecimal digits.")

if __name__ == "__main__":
    main()