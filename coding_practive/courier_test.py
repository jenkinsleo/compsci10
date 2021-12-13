NEWLINE = '\r\n'
PROMPT = '?:'

################################################################################
##2021-12-13
TARGET_FILE = 'courier.py'

def run_tests():

    ##test for formatted answer
    run_console_test('50\ns\nd', '$0.50')

    ##test for weight
    run_console_test('100\ns\nd', '$0.50')
    run_console_test('101\ns\nd', '$0.75')
    run_console_test('200\ns\nd', '$0.75')
    run_console_test('201\ns\nd', '$1.00')

    #test for priority
    run_console_test('50\np\nd', '$0.75')
    run_console_test('50\nP\nd', '$0.75')
    run_console_test('50\nPriority\nd', '$0.75')
    run_console_test('50\ne\nd', '$1.25')
    run_console_test('50\nE\nd', '$1.25')
    run_console_test('50\nExpress\nd', '$1.25')

    #test for destination
    run_console_test('50\ns\nd', '$0.50')
    run_console_test('50\nS\nD', '$0.50')
    run_console_test('50\ns\nDomestic', '$0.50')
    run_console_test('50\nS\nI', '$2.50')
    run_console_test('50\nStandard\nInternational', '$2.50')

    #test for combinations
    run_console_test('50\nPriority\nInternational', '$2.75')
    run_console_test('125\nPriority\nDomestic', '$1.12')
    run_console_test('125\nExpress\nDomestic', '$1.88')
    run_console_test('225\nExpress\nInternational', '$4.50')

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
    elif (type(actual_output) != type(expected_output)):
        color_print("FAIL (TYPE MISMATCH: expected "+ str(type(expected_output)) + ")","COMMENT")
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
    
    if (is_windows == False):
        input_string = '"' + input_string.replace('\n', '"\n"')[:-1]

    #add newline to end of expected output only if not already there
    if (expected_output[-len(NEWLINE):] != NEWLINE):
        expected_output = expected_output + NEWLINE

    #add newline to end of input only if not already there
    if (input_string[-len(NEWLINE):] != NEWLINE):
        input_string = input_string + NEWLINE

    display_test_header(input_string, expected_output, match_expected)

    try:
        if (is_windows):
            test_output = check_output(TARGET_FILE, input=input_string.encode('utf-8'), stderr=PIPE,  shell=True).decode("utf-8")
        else:
            test_output = subprocess.run(['pythonw' , TARGET_FILE], input=input_string.encode('utf-8'), stdout=subprocess.PIPE).stdout.decode("utf-8")
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
import os
import shutil
from datetime import datetime
LOG_DIRECTORY = "C:/.cs10log/courier"

score = 0
tests = 0

try:
    color = sys.stdout.shell
    color_enabled = True
except AttributeError:
    color_enabled = False

is_windows = (platform.system() == 'Windows')

if (is_windows == False):
    containing_folder_path = os.path.dirname(os.path.realpath(__file__))
    TARGET_FILE = containing_folder_path + '/' + TARGET_FILE
    NEWLINE = '\n'

if not os.path.exists(LOG_DIRECTORY):
    os.makedirs(LOG_DIRECTORY)
os.system("attrib +h " + LOG_DIRECTORY)    

timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

shutil.copy2(TARGET_FILE, LOG_DIRECTORY +  "/" + timestamp + " " + TARGET_FILE)
os.system("attrib +h " + LOG_DIRECTORY +  "/" + timestamp + " " + TARGET_FILE)    




run_tests()
display_score()
