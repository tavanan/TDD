import re
class Calculator:


    def empty_string(self,user_name):
        if user_name=="":
            return 0

    def single_number(self,num):
        return int(num)

    def two_number_comma(self,numbers):
        nums=numbers.split(',')
        num1=int(nums[0])
        num2=int(nums[1])
        return num1+num2

    def two_number_newline(self,numbers):
        nums=numbers.splitlines()
        num1=int(nums[0])
        num2=int(nums[1])
        return num1+num2

    def three_number_delimited(self,numbers):
        if ',' in numbers or '\n' in numbers:

            num1 = int(numbers[0])
            num2 = int(numbers[2])
            return num1+num2

    # def negative_number(self,number):
    #     num=int(number)
    #     if num < 0:

    #         raise Exception("sorry broken")


    
    def number_greater_1000(self,numbers):
         nums=numbers.split(',')
         sum=0
         for i in nums:
             if int(i)>1000:
                 i=0
             sum=sum+int(i)
         return sum

    def num_delimiters(self,numbers):
        if numbers.startswith('//'):
            temp = re.findall(r'\d+', numbers)
            res = list(map(int, temp))
            return sum(res)


#
# #kata methodology?
# def calculator(input_number):
#
#     if input_number == "" :
#         return 0
#     else:
#         return int(input_number)