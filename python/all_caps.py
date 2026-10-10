def shout(text) :
    result = ''
    for ch in text :
        if ch == ' ' :
            result += '-'
        else :
            result += ch.upper()
    return result
print(shout("hi there"))       # HI-THERE
print(shout("go team go"))     # GO-TEAM-GO
