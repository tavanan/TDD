import unittest
import calculator as CalculatorClass
class Testing(unittest.TestCase):

    calc=CalculatorClass.Calculator()


    def test_1_empty_string(self):
        result = 0
        print('Start empty_string test\n')
        empty=self.calc.empty_string("")
        self.assertEqual(empty,result)

    def test_2_single_number(self):
        result = 5
        print('Start single_number test\n')
        number=self.calc.single_number('5')
        self.assertEqual(result,number)

    def test_3_twonumber_comma(self):
        result=8
        print('Start two_number_comma test\n')
        sum=self.calc.two_number_comma('2,6')
        self.assertEqual(result,sum)

    def test_4_twonumber_newline(self):
        result=8
        print('Start two_number_newline test\n')
        sum=self.calc.two_number_newline('2\n6')
        self.assertEqual(result,sum)

    def test_5_three_numbers(self):
        result=8
        print('start three_numbers test\n')
        sum=self.calc.three_number_delimited('3,5')
        sum2=self.calc.three_number_delimited('3\n5')
        self.assertEqual(result,sum)
        self.assertEqual(result,sum2)

    # def test_6_negative_number(self):
    #     result=self.calc.negative_number('-6')
    #     print('start negative_number test\n ')
    #     with self.assertRaises(Exception) as context:
    #         result()

    #     self.assertTrue('broken' in str(context.exception))

    def test_7_number_greater_1000_ignore(self):
        result=11
        print("start ignore num>1000 test\n")
        sum=self.calc.number_greater_1000('2,3,6,1123')
        self.assertEqual(result,sum)

    def test_8(self):
        result=15
        print("start test 8")
        sum =self.calc.num_delimiters("//#\n12#3")
        self.assertEqual(result,sum)

    def test_9(self):
        result=17
        print("start test 9")
        sum =self.calc.num_delimiters("//###13###4")
        self.assertEqual(result,sum)

    def test_10(self):
            result = 18
            print("start test 10")
            sum = self.calc.num_delimiters("//!!12,3!!2\n1")
            self.assertEqual(result, sum)


if __name__=='__main__':
    unittest.main()





















# import calculator
#
#     def test_empty_string():
#         # given
#         input_number = ""
#         expected_result = 0
#
#         # when
#         result=calculator(input_number)
#
#         #then
#         assert(expected_result, result)
#
#
#     def test_single_number():
#
#         #given
#         input_number="2"
#         expected_value=2
#
#         #when
#         result=calculator(input_number)
#
#         #then
#         assertEquall(result,expected_value)