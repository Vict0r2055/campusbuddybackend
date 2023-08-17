import os
import pyautogui
import time
import moduleupdater
import json
import re

pyautogui.FAILSAFE = True


def open_file(file_path):
    # Open the file with the default program
    os.startfile(file_path)
    time.sleep(5)
    # Simulate Ctrl+A (select all)
    pyautogui.hotkey('ctrl', 'a')

    # Simulate Ctrl+C (copy)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(5)
    directory = os.path.dirname(file_path)

    # Create the text file name
    text_file_name = 'output.txt'

    # Construct the text file path
    text_file_path = os.path.join(directory, text_file_name)
    # Create the empty text file
    with open(text_file_path, 'w'):
        pass

    os.startfile(text_file_path)
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('ctrl', 's')
    pyautogui.hotkey('alt', 'F4')
    pyautogui.hotkey('alt', 'F4')
    return text_file_path


def process_output(file_loc):
    with open(file_loc, 'r') as file:
        # Read all lines from the file
        lines = file.readlines()

    # Remove the first three lines
    lines = lines[3:]

    # Remove lines starting with "FINAL"
    lines = [line for line in lines if not line.startswith('FINAL')]
    directory = os.path.dirname(file_loc)
    output_filename = 'exam_timetable_processed.txt'
    output_loc = os.path.join(directory, output_filename)
    # Open the file for writing
    with open(output_loc, 'w') as file:
        # Write the modified lines to the file
        file.writelines(lines)
    with open(output_loc, 'r') as file:
        # Read the lines of the file
        lines = file.readlines()
    examination_timetable = {}
    # Process the lines
    for line in lines:
        module_code = line[:7]
        liner = line.replace(' ', '')
        rline = line[::-1]
        # print(rline)
        counter = 0
        roo_index = 0
        for i in rline:
            roo_index += 1
            if i == "_":
                counter += 1
                if counter == 2:
                    room = rline[:roo_index + 4]
                    room_unq = room[::-1]
        if line.replace(' ', '').__contains__('CAMPUS'):
            dat_index = line.replace(' ', '').index('CAMPUS') + 6
            date = liner[dat_index:dat_index + 10]
            tim_index = dat_index + 10
            times = liner[tim_index:tim_index + 5]
            dur_index = tim_index + 5
            duration = liner[dur_index:dur_index + 3]

        if line.replace(' ', '').__contains__('BAY'):
            dat_index = line.replace(' ', '').index('BAY') + 3
            date = liner[dat_index:dat_index + 10]
            tim_index = dat_index + 10
            times = liner[tim_index:tim_index + 5]
            dur_index = tim_index + 5
            duration = liner[dur_index:dur_index + 3]
        examination_timetable[module_code] = {'date': date, 'duration': duration, 'time': times, 'room': room_unq}
        # Write data to JSON file
        base_directory = os.path.expanduser('~/Documents')
        save_directory2 = os.path.join(base_directory, 'Campus')
        json_data = json.dumps(examination_timetable)
        json_path = os.path.join(save_directory2, 'examinations.json')

        with open(json_path, 'w') as json_file:
            json_file.write(json_data)


process_output('C:\\Users\\luyas\\OneDrive\\Desktop\\exam_timetable_processed.txt')
