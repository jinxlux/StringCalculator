import re


def add(numbers: str) -> int:
    """
    Read a string numbers separated by a comma (ex:1,2,3) or other delimiters indicated as
    “//[delimiters separated by comma]\n[delimiter separated numbers]”
    (ex: one delimiter: //;\n1;2;3 two delimiters: //;,@\n1;2@3);
    delimiters can be arbitrary length.
    Numbers in the string must be positive. If a number > 1000, it will not be added to the final result
    :param numbers: a string of numbers
    :return: an int value for the sum of all numbers
    """
    # Remove white spaces in the front and tail of the input string
    numbers = numbers.strip()
    result = 0
    # Calculate only if the string is not empty
    if len(numbers) > 0:
        # Find whether the string needs to customize delimiter;
        # if it needs, find all delimiters;
        # add \\ to each delimiters to avoid recognizing delimiters as special
        # characters of regular expression;
        # create regular expression for splitting the numbers.
        if numbers.find("//", 0, 2) != -1:
            start_position = numbers.find("\n", 2)
            temp_split_string = numbers[2:start_position]
            start_position += 1
            split_string_list = temp_split_string.split(",")
            for i in range(len(split_string_list)):
                split_string_list[i] = "\\" + "\\".join(list(split_string_list[i]))
            split_string = "|".join(split_string_list)
        # If it not needs to customize delimiters, use comma as the delimiters by default.
        else:
            start_position = 0
            split_string = ","
        # Use regular expression to indicate all delimiters to split numbers;
        nums_string_list = re.split(split_string, numbers[start_position:])
        # Check whether negative numbers involved;
        # Throw NegativesNotAllowedError if they are detected.
        nums_negative_list = [i for i in nums_string_list if int(i) < 0]
        if len(nums_negative_list) > 0:
            raise NegativesNotAllowedError("Negatives not allowed: " + str(nums_negative_list))
        # Add all numbers together to calculate final result.
        for i in nums_string_list:
            if int(i) <= 1000:
                result += int(i)

    return result


class NegativesNotAllowedError(Exception):
    """
    A class for the exception of detecting negative numbers
    """

    def __init__(self, message):
        """
        constructor for the exception
        :param message: message for printing out
        """
        super().__init__(message)
        self.message = message

    def __str__(self):
        """
        output the message when printing the exception
        :return: the message
        """
        return self.message


if __name__ == '__main__':

    # test cases for unit test
    test_between = [
        # test cases for 1st question
        {
            'input': "1",
            'output': 1,
            'reason': "1 is the only input"
        }, {
            'input': "",
            'output': 0,
            'reason': "empty string should return 0"
        }, {
            'input': "1,2,3",
            'output': 6,
            'reason': "1+2+3 = 6"
        }, {
            'input': "4,2,1",
            'output': 7,
            'reason': "4+2+1 = 7"
        }, {
            'input': "4,2,100,0",
            'output': 106,
            'reason': "4+2+100+0 = 106"
        },
        # test cases for 2nd question
        {
            'input': "1\n,2,1",
            'output': 4,
            'reason': "1+2+1 = 7"
        }, {
            'input': "3,\n2,1\n",
            'output': 6,
            'reason': "3+2+1 = 6"
        }, {
            'input': "\n",
            'output': 0,
            'reason': "string only contains new line still should return 0"
        },
        # test cases for 3rd question
        {
            'input': "//;\n1;7;20",
            'output': 28,
            'reason': "1+7+20 = 28 with delimiter ;"
        }, {
            'input': "//$\n1$5$200",
            'output': 206,
            'reason': "1+5+200 = 206 with delimiter $"
        }, {
            'input': "///\n200/5/200",
            'output': 405,
            'reason': "200+5+200 = 405 with delimiter /"
        }, {
            'input': "//\\\n100\\5\\200",
            'output': 305,
            'reason': "100+5+200 = 305 with delimiter \\"
        },
        # test cases for 3rd question
        {
            'input': "1,-2, 5",
            'output': None,
            'reason': "Negative numbers exist: -2"
        },  {
            'input': "1,-2, 5, -100",
            'output': None,
            'reason': "Negative numbers exist: -2, -100"
        },
        # test cases for bonus 1 question
        {
            'input': "1,2,1001",
            'output': 3,
            'reason': "1001 should be ignored, so 1+2 = 3"
        }, {
            'input': "1,2,1000",
            'output': 1003,
            'reason': "1000 should not be ignored, so 1+2+1000 = 1003"
        }, {
            'input': "//$\n1$5$1001",
            'output': 6,
            'reason': "1000 should not be ignored, so 1+5 = 6"
        },
        # test cases for bonus 2 question
        {
            'input': "//^^^\n1^^^7^^^0^^^1",
            'output': 9,
            'reason': "1+7+0+1 = 9 with delimiter ^^^"
        }, {
            'input': "//***\n1***2***3",
            'output': 6,
            'reason': "1+2+3 = 6 with delimiter ***"
        },
        # test cases for bonus 3 question
        {
            'input': "//$,@\n1$2@3",
            'output': 6,
            'reason': "1+2+3 = 6 with delimiter $ and @"
        }, {
            'input': "//$,^,%\n1%2^3%4",
            'output': 10,
            'reason': "1+2+3+4 = 10 with delimiter $, ^, and %"
        },
        # test cases for bonus 4 question
        {
            'input': "//$$,@\n1$$2@3",
            'output': 6,
            'reason': "1+2+3 = 6 with delimiter $$ and @"
        }, {
            'input': "//$$,^^,!,****\n10$$20!30^^40****50",
            'output': 150,
            'reason': "10+20+30+40+50 = 150 with delimiter $$, ^^, !, and ****"
        }
    ]

    for case in test_between:
        try:
            if add(case['input']) != case['output']:
                print("Testing fault: ", case['reason'])
        except NegativesNotAllowedError as e:
            print("Throw 'Negatives Not allowed' exception successfully: ", e)

    print("test finished!")
