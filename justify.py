def justify(paragraph: str, page_width: int):
    '''
    accepts a paragraph string and page width
    returns an array of left AND right justified strings.
    NOTE: No words should be broken, the beginning and end of the line should be characters).

    Example:
    justify("This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works.", 20)

    Sample input:
        Paragraph = "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works."
        Page Width = 20

    Sample Output:
    [
        "This  is  a   sample"
        "text      but      a"
        "complicated  problem"
        "to be solved, so  we"
        "are adding more text"
        "to   see   that   it"
        "actually      works.”
    ]
    '''

    # split paragraph text into list of words
    paragraph_array = paragraph.split(" ")
    # init array to return at the end
    return_array = []
    # init working array for this line
    working_array = []
    # init pivot
    pivot = 1
    # init spaces
    # while there are still words in the array
    while len(paragraph_array):
        spaces = " "
        # init working_string for this line in the array
        working_string = ""
        # while the string joined together with one space is less than page_width,
        # and
        # while the number of items left in the paragraph array >= 0
        while (len(spaces.join(paragraph_array[0:pivot])) < (page_width)) and (len(paragraph_array) >= 0):
            # pivot to the next word
            pivot += 1
            # if the number of words left in the array is less than the pivot point,
            if len(paragraph_array) < pivot:
                break
        # calculate the working string
        working_string = spaces.join(paragraph_array[0:pivot])
        # if the working string is greater than the page width.
        if len(working_string) > page_width:
            # deincrement the pivot point
            pivot -= 1
            # set the working array
            working_array = paragraph_array[0:pivot]
            # set the working string
            working_string = "".join(working_array)
        while len(working_string) <= page_width and len(paragraph_array) >= pivot:
            if len(working_string) == page_width:
                break
            # loop through all the words in the list, starting with -2 (the second to last word)
            for i in range(2, len(working_array) + 1):
                # add a space to the end of the word
                working_array[-i] += ' '
                # join all the words in the working array together in one string
                working_string = "".join(working_array)
                # once the working string is at the page width,
                if len(working_string) == page_width:
                    # break the while loop
                    break
        # add the working string on to the end of the return array
        return_array.append(working_string)
        # for the number of items between 0 and pivot,
        for i in range(0, pivot):
            # if there are still words in the paragraph_array,
            if len(paragraph_array) > 0:
                # remove the first item in the list
                paragraph_array.pop(0)
            # if there are no more words in the paragraph_array,
            else:
                # remove the last item added to the return array
                working_array = return_array.pop().split(' ')
                # recalculate the working string
                working_string = "".join(working_array)
                # while the working_string is less than or equal to the page width
                while len(working_string) <= page_width:
                    # add a space to the end of the first word
                    for i in range(2, len(working_array) + 1):
                        # add a space to the end of the word
                        working_array[-i] += ' '
                    # recalculate the working string
                    working_string = "".join(working_array)
                # add the working string on to the end of the return array
                return_array.append(working_string)
    # finally, return the return array
    return return_array


# TESTS


array = justify(
    "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works.",
    20)
array[0] == 'This  is  a   sample'
array[1] == 'text      but      a'
array[2] == 'complicated  problem'
array[3] == 'to be solved, so  we'
array[4] == 'are adding more text'
array[5] == 'to   see   that   it'
array[6] == 'actually      works.'
for i in range(0, 6):
    assert len(array[i]) == 20
print(array)
