code_dictionary = {
    'variable': 'a data item that may take on more than one value during the runtime of a program',
    'code': 'program instructions',
    'list': 'a formal structure analogous to a list, by which items of data can be stored or processed in a definite order',
    'algorithm': 'a process or set of rules to be followed in calculations or other problem-solving operations, especially by a computer',
    'python': 'a high-level general-purpose programming language',
    'set': 'an unordered collection of items',
    'data': 'facts and statistics collected together for reference or analysis',
}

for words in code_dictionary:
    print(words + ':' +
        '\n\t' + code_dictionary[words] +
        '\n')