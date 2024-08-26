# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def concatenate(string, liste):
    output_list=[]
    for elt in liste:
        output_list.append(string + str(elt))
    return output_list

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    output_list=[]
    temp_list=[]
    if len(sequence)==2:
        output_list.append(sequence)
        output_list.append(sequence[::-1])
    else:
        list_sequence=list(sequence)
        for elt in list_sequence:
            list_copy=list_sequence[::]
            list_copy.remove(elt)
            temp_list=(concatenate(elt, get_permutations(''.join(list_copy))))
            for elt in temp_list:
                output_list.append(elt)
    return output_list


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    sequence1 = "aeiou"
    sequence2 = "AEIOU"
    sequence3 = "hdut"
    get_permutations(sequence1)
    get_permutations(sequence2)
    get_permutations(sequence3)


