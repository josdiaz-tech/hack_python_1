"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    
    i=0
    offset = 1
    count = len(result)
    while i < count:
        result.insert(offset,'@')
        offset +=2
        i+=1

    return result  