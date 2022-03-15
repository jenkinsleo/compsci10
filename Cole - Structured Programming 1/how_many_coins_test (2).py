NEWLINE = '\r\n'
PROMPT = '?:'

################################################################################
##2018-03-10
TARGET_FILE = 'how_many_coins.py'

def run_tests():

    run_console_test('0.10\n','quarters:0; dimes:1; nickels:0; pennies:0')
    run_console_test('0.25\n','quarters:1; dimes:0; nickels:0; pennies:0')
    run_console_test('0.41\n','quarters:1; dimes:1; nickels:1; pennies:1')
    run_console_test('0.94\n','quarters:3; dimes:1; nickels:1; pennies:4')
    run_console_test('1.31\n','quarters:5; dimes:0; nickels:1; pennies:1')
    run_console_test('19.15\n','quarters:76; dimes:1; nickels:1; pennies:0')
    
################################################################################
##2020-03-26
    
import sys
import subprocess
from subprocess import check_output
from subprocess import call
from subprocess import *
import sys, traceback
import re
import codecs
import os
import platform

def human_readable_input_string(input_string):
    human_readable_string = input_string.replace("\n", ', ')
    if (human_readable_string[-2:] == ', '):
        human_readable_string = human_readable_string[:-2]
    return human_readable_string
    
def color_print(text, text_type = 'stdin'):
    if (color_enabled):
        if text[-1:] != '\n':
            text += '\n'
        color.write(text,text_type)
    else:
        print(text)

def display_test_header(input_string, expected_output, match_expected = True):
    color_print('-' * 80)
    color_print('Test # ' + str(tests))
    color_print('Input: ' + human_readable_input_string(str(input_string)))
    color_print('Output Expected: ' if match_expected else 'Output Expected NOT TO MATCH:')
    color_print(str(expected_output), "stdout")

def display_test_output(test_output):
    test_output = test_output.rsplit(PROMPT, 1)[-1]
    color_print('Output Returned:')
    color_print(str(test_output), "stdout")

def assert_equals(input_string, actual_output, expected_output):
    global tests
    global score
    global output
    
    tests = tests + 1

    display_test_header(input_string, expected_output)
    display_test_output(actual_output)

    if (actual_output == expected_output):
        color_print("PASS", "STRING")
        score = score + 1
    else:
        color_print("FAIL (NO MATCH)","COMMENT")

def strings_match(expected_output, test_output):
    return(expected_output == test_output[-len(expected_output):])

def run_console_test(input_string, expected_output, match_expected = True):
    global tests
    global score
    tests = tests + 1
    test_output = ""
    test_executed = False
    exception_string = ""
    traceback = ""

    if (operating_system != 'Windows' and operating_system != 'Linux'):
        input_string = '"' + input_string.replace('\n', '"\n"')[:-1]

    if (expected_output[-len(NEWLINE):] != NEWLINE):
        expected_output = expected_output + NEWLINE

    if (input_string[-len(NEWLINE):] != NEWLINE):
        input_string = input_string + NEWLINE

    display_test_header(input_string, expected_output, match_expected)

    try:
        if (operating_system == 'Windows'):
            test_output = check_output(TARGET_FILE, input=input_string.encode('utf-8'), stderr=PIPE,  shell=True).decode("utf-8")
        elif (operating_system == 'Linux'):
            os.system('rm -f input1')
            os.system('rm -f output1')
            os.system( 'echo "' + input_string + '" >> input1')
            os.system('python3 ' + TARGET_FILE + ' < "input1" >> output1')
            test_output = open('output1').read()
            os.system('rm -f input1')
            os.system('rm -f output1')
        else:
            test_output = subprocess.run(['pythonw' , TARGET_FILE], input=input_string.encode('utf-8'), stdout=subprocess.PIPE).stdout.decode("utf-8")
        test_executed = True
    except CalledProcessError as e:
        print("CalledProcessError")
        traceback = str(e.stderr)[2:-5]
        traceback = codecs.decode(traceback, 'unicode_escape')
        exception_string = str(type(e))
    except Exception as e:
        print("Exception")
        traceback = str(e)
        exception_string = str(type(e))

    if (test_executed):
        display_test_output(test_output)
        test_result_matched = strings_match(expected_output, test_output)
        if test_result_matched == match_expected:
            color_print("PASS", "STRING")
            score = score + 1
        else:
            color_print("FAIL (No Match)","COMMENT")
    else:
        color_print("FAIL (" + exception_string + ")","COMMENT")
        color_print(traceback,"COMMENT")

def display_score():
    color_print('=' * 80)

    color_print("Total score: " + str(score) + " / " + str(tests))
    if (score == tests):
        color_print('Overall: PASS', "STRING")
    else:
        color_print('Overall: FAIL', "COMMENT")


########################################################################

score = 0
tests = 0

try:
    color = sys.stdout.shell
    color_enabled = True
except AttributeError:
    color_enabled = False

operating_system = platform.system()

if (operating_system != 'Windows' and operating_system != 'Linux'):
    containing_folder_path = os.path.dirname(os.path.realpath(__file__))
    TARGET_FILE = containing_folder_path + '/' + TARGET_FILE

if (operating_system != 'Windows'):
    NEWLINE = '\n'

run_tests()
display_score()
