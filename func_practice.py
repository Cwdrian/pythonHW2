#Write a Python function called max_num()to find the maximum of three numbers.

#this would be better as an iterative 

def max_num(x,y,z):
    high_num = x #lets assume x is the highest for now

    if y > high_num:
        high_num = y #update if its higher
    
    if z > high_num:
        high_num = z #update if its higher

    return high_num
print(max_num(7, 13, -49))


#Write a Python function called mult_list() to multiply all the numbers in a list.

#a recursion could be used BUT it would be less efficient

def mult_list(numbers):
    result = 1
    for every_number in numbers:
        result *= every_number
    return result

numbers = [1, 2, 3, 4, 50]
print(mult_list(numbers)) 


#Write a Python function called rev_string() to reverse a string.

#this would be the absolute best way to do it with a built in function
# BUT i think you want us to write the function
original_string = "Hello, World!"
reversed_string = ''.join(reversed(original_string))

print("Original string:", original_string)
print("Reversed string:", reversed_string)

#an iterative approach would be best in this case also

def rev_string(input_str):
    reversed_str = ""
    for char in input_str:
        reversed_str = char + reversed_str
    return reversed_str

original_string = "This is what i want to reverse"
print("Reversed string:", rev_string(original_string))
#Write a Python function called num_within() to check whether a number falls in a given

def num_within(num, start, end):
    return start <= num <= end

print(num_within(13, 21, 41))   
print(num_within(9, 10, 3))   
print(num_within(10, 2, 55)) 


#Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

def pascal(n):
    for i in range(n):
        #first element of each row as 1
        row = [1]
        # Calculate the elements in the current row based on the previous row
        if i > 0:
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)
        print(' '.join(map(str, row)))
        # Save the current row for the next iteration
        prev_row = row

# Example usage:
pascal(5)
