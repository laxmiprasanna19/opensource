input_string = input()


output = ""
count = 1


for i in range(1, len(input_string)):
    
    if input_string[i] == input_string[i - 1]:
        count += 1   
    else:
       
        output += input_string[i - 1] + str(count)
        count = 1  

output += input_string[-1] + str(count)

print(output)
