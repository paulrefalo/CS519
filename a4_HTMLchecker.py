# CS 519 assignment 4 - a4_HTMLchecker by Paul ReFalo

import re
from pprint import pprint

example_set = ['''<a><b><c></c></b></a>''',
 '''<foo>asd<bar>alksjd</bar><p>asldkj</p></foo>''',
 '''<foo><bar></bop></bar></foo>''',
 '''<foo><bar></bar></foo></foo>''',
 '''<foo><bar></bar></foo></foo><p>''',
 '''<scooby><a><b><c></c></b></a></doo>''',
 '''<scooby><a><b><c></c></b></a></scooby>''']

# Should return a list of tuples of the form ('string', boolean)

def valid_html(test_string):
    result = []

    for s in test_string:
        tags = re.findall('(<\/?\w+>)', s)            # get all HTML tags
        openingTags = re.findall('(<\w+>)', s)        # get only opening HTML tags
        closingTags = re.findall('(<\/\w+>)', s)      # get only closing tags

        # Check that opening and closing tags are of equal number.  If not, append result with False
        if len(openingTags) != len(closingTags):
            result.append((s, False))
            continue

        print(tags)
        restart = True

        while restart:              # use while loop to restart and re-index for loop since we are removing elements conditionally
            if len(tags) == 0:      # if len(tags) == 0 then HTML is valid -> append result True and string
                result.append((s, True))
                break
            for idx, tag in enumerate(tags):            # iterate and enumerate tags
                mo = re.search('(<\/(\w+)>)', tag)      # find first closing tag
                if mo:
                    testTagText = "^<" + mo.group(2) + ">$"           # build equivalent opening tag to the closing one found
                    mo2 = re.search(testTagText, tags[idx - 1])     # check if previous tag matches this
                    if mo2:                                         # if so, remove this closing and opening tag and restart for loop
                        tags.remove(tags[idx])
                        tags.remove(tags[idx - 1])
                        print(tags)
                        break                                       # break needed to restart for loop
                    else:                                           # if not, HTML is not valid, return False and string
                        result.append((s, False))                   # append False to result
                        restart = False                             # get out of while loop
                        break                                       # break for loop

    return result

validHTML = valid_html(example_set)
print("The result of HTML submitted for validity is: ")
pprint(validHTML)
