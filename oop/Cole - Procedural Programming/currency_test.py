NEWLINE = '\r\n'
PROMPT = '?:'

################################################################################
##2020-01-28
TARGET_FILE = 'target.py'
import currency

def run_tests():

    #test function add_coins
    assert_equals('currency.add_coins(1,1,1,1)',currency.add_coins(1,1,1,1), 0.41, True)
    assert_equals('currency.add_coins(3,2,1,3)',currency.add_coins(5,2,1,3), 1.53, True)
    #test for optional pennies parameter; only three arguments passed in
    assert_equals('currency.add_coins(3,2,1)',currency.add_coins(5,2,1), 1.50, True)
    #test for correct naming of parameters; note the use of keyword parameters
    assert_equals('currency.add_coins(nickels=1,dimes=2,quarters=5)',currency.add_coins(nickels=1,dimes=2,quarters=5), 1.50, True)

    #test function make_change
    assert_equals('currency.make_change(0.41)', currency.make_change(0.41), (1,1,1,1), True)
    assert_equals('currency.make_change(1.87)', currency.make_change(1.87), (7,1,0,2), True)
    assert_equals('currency.make_change(19.15)', currency.make_change(19.15), (76,1,1,0), True)

    #test function to_string
    assert_equals('currency.to_string(1,1,1,1)',currency.to_string(1,1,1,1), 'quarters:1; dimes:1; nickels:1; pennies:1', True)
    assert_equals('currency.to_string(5,2,1,3)',currency.to_string(5,2,1,3), 'quarters:5; dimes:2; nickels:1; pennies:3', True)

    #test function to_string_from_tuple
    assert_equals('currency.to_string_from_tuple((1,1,1,1))',currency.to_string_from_tuple( (1,1,1,1) ), 'quarters:1; dimes:1; nickels:1; pennies:1', True)
    assert_equals('currency.to_string_from_tuple((5,2,1,3))',currency.to_string_from_tuple( (5,2,1,3) ), 'quarters:5; dimes:2; nickels:1; pennies:3', True)

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
    if (input_string != ''):
        color_print('Input: ' + human_readable_input_string(str(input_string)))
    color_print('Output Expected: ' if match_expected else 'Output Expected NOT TO MATCH:')
    color_print(str(expected_output), "stdout")

def display_test_output(test_output):
    if (type(test_output) == str):
        test_output = test_output.rsplit(PROMPT, 1)[-1]
    color_print('Output Returned:')
    color_print(str(test_output), "stdout")

def assert_equals(input_string, actual_output, expected_output, match_expected = True):
    global tests
    global score
    global output
    
    tests = tests + 1

    display_test_header(input_string, expected_output, match_expected)
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
