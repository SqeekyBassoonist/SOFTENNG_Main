"""
This module was created by Carter Luka for Mick's microservice for the Software Engineering 1 Project.
It searches through a list of journal pages, both grouped and ungrouped and returns the tags present
in them.

The pages are found in two different file structures.

    Journals
    |
    --- Journal 1
        |
        --- Jou1Pg1.txt
        --- Jou1Pg2.txt
    --- Journal 2
        |
        --- Jou2Pg1.txt

    Or

    Unsorted Pages
    |
    --- Page1.txt
    --- Page2.txt
    --- Page3.txt
"""

from typing import Callable
import os
import json
import sys

def parse_line_for_tags(line: str) -> list[str]:
    """
    Parses a line to find all the different tags in it. Tags are formatted as //tag1 //tag2
    :param line: The line containing tags
    :return: A list of all the found tags in the line. If no tags are found the list is empty
    """
    tag_list = []
    line = line.replace(" ", "")

    while '//' in line: # While there's still tags

        # Find the place of the first tag (pretty much always at index 0)
        first_tag_index = line.find('//')
        tag = line[first_tag_index + 2:]

        # Isolate the tag from the rest in the line, resulting in only the one tag being saved
        sec_tag_index = tag.find('//')
        if sec_tag_index != -1:
            tag = tag[:sec_tag_index]

        # Add the found tag to tag_list and remove it from line
        tag = tag.replace(' ', '')
        tag = tag.replace('\n', '')
        tag = tag.replace('\t', '')
        tag_list.append(tag)
        line = line[sec_tag_index + 2:]

    return tag_list

def parse_file_for_links(text: str) -> list[str]:
    """
    Looks through the contents of a page a looks for links in the format [[pagename]]
    :param text: The content of the page read from the page.txt file
    :return: A list of the links found in the file
    """
    link_list = []
    while '[[' in text:
        start_ind = text.find('[[')
        end_ind = text.find(']]')
        link = text[start_ind + 2 :end_ind]
        link_list.append(link)
        text = text[end_ind + 2:]

    return link_list

def parse_file_tree(dir_name: str) -> json:
    """
    Goes through the file tree starting at dir_name, looking for journals and pages.
    It then calls func on each one. For the purposes of this microservice, this looks through
    a given folder for journals and pages, then passes the first line of each page into
    'parse_line_for_tags'.
    :param dir_name: The name of the root directory to look through
    :return: A JSON in the format
                {
                "test_journal_one": {
                    "journal_1_page_1": {
                        "tags": [
                            "Journal1",
                            "Page1"
                        ]
                    }
                }
    """
    tag_json = {}
    for (root, dirs, files) in os.walk(dir_name):
        if not dirs: # Get a list of directories with pages in them

            journal_list = {}
            for file in files: # For every page in the journal
                with open(root + '\\' + file) as f:

                    line = f.readline() # Get a list of the tags for the page
                    tag_list = {'tags': parse_line_for_tags(line)}

                    text = f.read() # Get a list of links in the page
                    link_list = {'links': parse_file_for_links(text)}

                    journal_list.update({file: tag_list | link_list})

            tag_json.update({os.path.basename(root): journal_list})

    return json.dumps(tag_json, indent=4)

if __name__ == '__main__':
    work_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(work_dir)

    args = sys.argv
    if len(args) < 2:
        print('Invalid input provided: No arguments given')
        exit(-1)

    if args[1] == 'journal':
        with open('output.txt', 'w+') as f:
            f.write(parse_file_tree('.\\journals'))
        print(parse_file_tree('.\\journals'))
        exit(1)
    if args[1] == 'ungrouped':
        with open('output.txt', 'w+') as f:
            f.write(parse_file_tree('.\\ungrouped'))
        print(parse_file_tree('.\\ungrouped'))

        exit(1)
    if args[1] == 'full':
        with open('output.txt', 'w+') as f:
            f.write(parse_file_tree('.\\journals'))
            f.write(parse_file_tree('.\\ungrouped'))
        print(parse_file_tree('.\\journals'))
        print(parse_file_tree('.\\ungrouped'))
        exit(1)

    if len(args) > 2:
        print('Invalid input provided: To many arguments provided')
        exit(-1)

    print('Invalid input provided: input is not \'journal\' or \'ungrouped\'')
    exit(-1)

