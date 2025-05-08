# Microservice A - Tag & Link Reader

This microservice will search through a list of journal pages, both grouped and ungrouped and returns the tags and links present in them.

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

The tags will be formatted as //tag and will only be present in the first line of the page. The links will be formatted as \[\[link\]\] and can be anywhere in the page.

## OUTPUT

After calling the microservice, a file called 'output.txt' will be created in the microservice directory. The file will contain atmost two JSONs in the format. An example out file is in this file [output.txt](output.txt)

    {
        "journal_name": {
            "page_1_name": {
                "tags": [
                    "tag_text",
                    "tag_text"
                ]
                "links": [
                    "link_text",
                    "link_text"
                ]
            },
            "page_2_name": {
                "tags": [
                    "tag_text",
                    "tag_text"
                ]
                "links": [
                    "link_text",
                    "link_text"
                ]
            }
        }
    }

## INPUT

The microservice can be called through the command line. As it's a python file, you can call it through the command 'python \[path/to/main.py\] < args >. 

Args will be one of three words, those being: 

    - journals (only searches pages form journals)
    - ungrouped (only searches ungrouped pages) 
    - full (searches everything)

Adding extra arguments, not providing enough, or using invalid arguments will cause the program to exit without output.

An example call would be 'python main.py full' or 'python main.py journal'