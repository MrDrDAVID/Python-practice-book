from collections import OrderedDict

new_glossary = OrderedDict()

new_glossary['variable'] = 'a data item that may take on more than one value during the runtime of a program'
new_glossary['code'] = 'program instructions'
new_glossary['list'] = 'a formal structure analogous to a list, by which items of data can be stored or processed in a definite order'
new_glossary['algorithm'] = 'a process or set of rules to be followed in calculations or other problem-solving operations, especially by a computer'

for words in new_glossary:
    print(words + ':' +
        '\n -' + new_glossary[words] +
        '\n')