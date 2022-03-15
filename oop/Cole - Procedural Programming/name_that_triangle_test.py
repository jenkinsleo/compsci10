NEWLINE = '\r\n'
PROMPT = '?:'

################################################################################
##2019-10-04
TARGET_FILE = 'name_that_triangle.py'
import name_that_triangle

def run_tests():

    ##test is_valid_triangle
    assert_equals("is_valid_triangle(60,60,60)", name_that_triangle.is_valid_triangle(60,60,60), True)
    assert_equals("is_valid_triangle(60,60,90)", name_that_triangle.is_valid_triangle(60,60,90), False)
    assert_equals("name_that_triangle.is_valid_triangle(0,90,90)", name_that_triangle.is_valid_triangle(0,90,90), False);    	
    assert_equals("name_that_triangle.is_valid_triangle(90,0,90)", name_that_triangle.is_valid_triangle(90,0,90), False);    	
    assert_equals("name_that_triangle.is_valid_triangle(0,90,90)", name_that_triangle.is_valid_triangle(0,90,90), False);      
    

    ##test classify_by_angle
    assert_equals("classify_by_angle(60,60,60)", name_that_triangle.classify_by_angle(60,60,60), 'acute')
    assert_equals("name_that_triangle.classify_by_angle(60,60,60)", name_that_triangle.classify_by_angle(60,60,60), "acute");    	
    assert_equals("name_that_triangle.classify_by_angle(90,60,30)", name_that_triangle.classify_by_angle(90,60,30), "right");    	
    assert_equals("name_that_triangle.classify_by_angle(30,90,60)", name_that_triangle.classify_by_angle(30,90,60),"right");    	
    assert_equals("name_that_triangle.classify_by_angle(60,30,90)", name_that_triangle.classify_by_angle(60,30,90),"right");    	
    assert_equals("name_that_triangle.classify_by_angle(100,60,20)", name_that_triangle.classify_by_angle(100,60,20),"obtuse");    	
    assert_equals("name_that_triangle.classify_by_angle(60,20,100)", name_that_triangle.classify_by_angle(60,20,100),"obtuse");    	
    assert_equals("name_that_triangle.classify_by_angle(20,100,60)", name_that_triangle.classify_by_angle(20,100,60),"obtuse");    	

    ##test classify_by_side
    assert_equals("classify_by_side(60,60,60)", name_that_triangle.classify_by_side(60,60,60), 'equilateral')
    assert_equals("name_that_triangle.classify_by_side(60,60,60)", name_that_triangle.classify_by_side(60,60,60), "equilateral");	
    assert_equals("name_that_triangle.classify_by_side(30,30,120)", name_that_triangle.classify_by_side(30,30,120), "isosceles");	
    assert_equals("name_that_triangle.classify_by_side(30,120,30)", name_that_triangle.classify_by_side(30,120,30), "isosceles");	
    assert_equals("name_that_triangle.classify_by_side(120,30,30)", name_that_triangle.classify_by_side(120,30,30), "isosceles");	
    assert_equals("name_that_triangle.classify_by_side(50,60,70)", name_that_triangle.classify_by_side(50,60,70), "scalene");
    assert_equals("name_that_triangle.classify_by_side(60,70,50)", name_that_triangle.classify_by_side(60,70,50), "scalene");
    assert_equals("name_that_triangle.classify_by_side(70,50,60)", name_that_triangle.classify_by_side(70,50,60), "scalene");


    assert_equals("classify_triangle(30,60,90)", name_that_triangle.classify_triangle(30,60,90), 'right scalene')
    assert_equals("classify_triangle(30,90,60)", name_that_triangle.classify_triangle(30,90,60), 'right scalene')
    assert_equals("classify_triangle(90,60,30", name_that_triangle.classify_triangle(90,60,30), 'right scalene')
    assert_equals("classify_triangle(90,30,60)", name_that_triangle.classify_triangle(90,30,60), 'right scalene')
    assert_equals("classify_triangle(60,90,30)", name_that_triangle.classify_triangle(60,90,30), 'right scalene')
    assert_equals("classify_triangle(60,30,90)", name_that_triangle.classify_triangle(60,30,90), 'right scalene')

    assert_equals("classify_triangle(45,90,45)", name_that_triangle.classify_triangle(45,90,45), 'right isosceles')
    assert_equals("classify_triangle(90,45,45)", name_that_triangle.classify_triangle(90,45,45), 'right isosceles')
    assert_equals("classify_triangle(45,45,90)", name_that_triangle.classify_triangle(45,45,90), 'right isosceles')

    assert_equals("classify_triangle(100,40,40)", name_that_triangle.classify_triangle(100,40,40), 'obtuse isosceles')
    assert_equals("classify_triangle(40,100,40)", name_that_triangle.classify_triangle(40,100,40), 'obtuse isosceles')
    assert_equals("classify_triangle(40,40,100)", name_that_triangle.classify_triangle(40,40,100), 'obtuse isosceles')

    assert_equals("classify_triangle(20,60,100)", name_that_triangle.classify_triangle(20,60,100), 'obtuse scalene')
    assert_equals("classify_triangle(20,100,60)", name_that_triangle.classify_triangle(20,100,60), 'obtuse scalene')
    assert_equals("classify_triangle(100,60,20)", name_that_triangle.classify_triangle(100,60,20), 'obtuse scalene')
    assert_equals("classify_triangle(100,20,60)", name_that_triangle.classify_triangle(100,20,60), 'obtuse scalene')
    assert_equals("classify_triangle(60,100,20)", name_that_triangle.classify_triangle(60,100,20), 'obtuse scalene')
    assert_equals("classify_triangle(60,20,100)", name_that_triangle.classify_triangle(60,20,100), 'obtuse scalene')

    assert_equals("classify_triangle(60,60,60)", name_that_triangle.classify_triangle(60,60,60), 'equilateral')

    assert_equals("classify_triangle(80,50,50)", name_that_triangle.classify_triangle(80,50,50), 'acute isosceles')
    assert_equals("classify_triangle(50,80,50)", name_that_triangle.classify_triangle(50,80,50), 'acute isosceles')
    assert_equals("classify_triangle(50,50,80)", name_that_triangle.classify_triangle(50,50,80), 'acute isosceles')

    assert_equals("classify_triangle(50,60,70)", name_that_triangle.classify_triangle(50,60,70), 'acute scalene')
    assert_equals("classify_triangle(50,70,60)", name_that_triangle.classify_triangle(50,70,60), 'acute scalene')
    assert_equals("classify_triangle(60,70,50)", name_that_triangle.classify_triangle(60,70,50), 'acute scalene')
    assert_equals("classify_triangle(60,50,70)", name_that_triangle.classify_triangle(60,50,70), 'acute scalene')
    assert_equals("classify_triangle(70,50,60)", name_that_triangle.classify_triangle(70,50,60), 'acute scalene')
    assert_equals("classify_triangle(70,60,50)", name_that_triangle.classify_triangle(70,60,50), 'acute scalene')

    assert_equals("classify_triangle(30,90,90)", name_that_triangle.classify_triangle(30,90,90), 'INVALID')
    assert_equals("classify_triangle(70,80,90)", name_that_triangle.classify_triangle(70,80,90), 'INVALID')
    assert_equals("classify_triangle(0,120,60)", name_that_triangle.classify_triangle(0,120,60), 'INVALID')
    assert_equals("classify_triangle(90,90,0)", name_that_triangle.classify_triangle(90,90,0), 'INVALID')
    assert_equals("classify_triangle(170,10,0)", name_that_triangle.classify_triangle(170,10,0), 'INVALID')
                
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
