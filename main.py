import re
while True:
    print("\n")
    inp = str(input("Please enter a DNA Sequence: "))
    chars = re.findall(r'[GCATgcat]', inp)
    empty_list = []
    for char in chars:
        if char == "G":
            empty_list.append("C")
        if char == "C":
            empty_list.append("G")
        if char == "A":
            empty_list.append("T")
        if char == "T":
            empty_list.append("A")
    print(''.join(empty_list))
