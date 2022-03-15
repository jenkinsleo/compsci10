NEWLINE = '\r\n'
PROMPT = '?:'

################################################################################
##2021-04-21

def run_tests():

    #Q1
    run_console_test('iterative_structures_q1.py', '1\n', 'Ni! ')
    run_console_test('iterative_structures_q1.py', '3\n', 'Ni! Ni! Ni! ')
    run_console_test('iterative_structures_q1.py', '6\n', 'Ni! Ni! Ni! Ni! Ni! Ni! ')
    run_console_test('iterative_structures_q1.py', '0\n', '')

    #Q2
    run_console_test('iterative_structures_q2.py', '1\n4\n', '24')
    run_console_test('iterative_structures_q2.py', '3\n5\n', '60')
    run_console_test('iterative_structures_q2.py', '6\n10\n', '30240')
    run_console_test('iterative_structures_q2.py', '7\n8\n', '56')

    #Q3
    run_console_test('iterative_structures_q3.py', '100\n2\n', '7')
    run_console_test('iterative_structures_q3.py', '81\n3\n', '4')
    run_console_test('iterative_structures_q3.py', '5\n5\n', '1')

    #Q4
    run_console_test('iterative_structures_q4.py', '42\n', "You may pass"
)
    run_console_test('iterative_structures_q4.py', '41\n42\n', "You may pass"
)
    run_console_test('iterative_structures_q4.py', '40\n41\n42\n', "You may pass"
)
    run_console_test('iterative_structures_q4.py', '40\n41\n42\n', "You may pass"
)
    run_console_test('iterative_structures_q4.py', '40\n41\n43\n', "Entry denied"
)

################################################################################
    
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

def display_test_header(file, input_string, expected_output, match_expected = True):
    color_print('-' * 80)
    color_print('Test # ' + str(tests))
    color_print('Target:' + str(file))
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

    display_test_header(input_string, input_string, expected_output, match_expected)
    display_test_output(actual_output)

    if (actual_output == expected_output):
        color_print("PASS", "STRING")
        score = score + 1
    elif (type(actual_output) != type(expected_output)):
        color_print("FAIL (TYPE MISMATCH: expected "+ str(type(expected_output)) + ")","COMMENT")
    else:
        color_print("FAIL (NO MATCH)","COMMENT")

def strings_match(expected_output, test_output):
    return(expected_output == test_output[-len(expected_output):])

def run_console_test(file, input_string, expected_output, match_expected = True):
    global tests
    global score
    tests = tests + 1
    test_output = ""
    test_executed = False
    exception_string = ""
    traceback = ""

    if (is_windows == False):
        input_string = '"' + input_string.replace('\n', '"\n"')[:-1]

    #add newline to end of expected output only if not already there
    if (expected_output[-len(NEWLINE):] != NEWLINE):
        expected_output = expected_output + NEWLINE

    #add newline to end of input only if not already there
    if (input_string[-len(NEWLINE):] != NEWLINE):
        input_string = input_string + NEWLINE

    display_test_header(file, input_string, expected_output, match_expected)

    try:
        if (is_windows):
            test_output = check_output(file, input=input_string.encode('utf-8'), stderr=PIPE,  shell=True).decode("utf-8")
        else:
            if (is_windows == False):
                containing_folder_path = os.path.dirname(os.path.realpath(__file__))
                file = containing_folder_path + '/' + file            
            test_output = subprocess.run(['pythonw' , file], input=input_string.encode('utf-8'), stdout=subprocess.PIPE).stdout.decode("utf-8")
        test_executed = True
    except CalledProcessError as e:
        traceback = str(e.stderr)[2:-5]
        traceback = codecs.decode(traceback, 'unicode_escape')
        exception_string = str(type(e))
    except Exception as e:
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

is_windows = (platform.system() == 'Windows')

if (is_windows == False):
    NEWLINE = '\n'

run_tests()
display_score()
