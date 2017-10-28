def parse_as_json(text):
    """Return data structure parsing text as JSON"""
    import json
    return json.loads(text)

def parse_as_preferred(text):
    """Return data structure parsing text assuming it to follow 'pass
    author preferred' schema which is taken to mean one  ":"-deliminated
    "key:value" sequence per line.
    """
    ret = dict()

    # FIXME: allow multi-line values?
    for line in text.split('\n'):
        if not line.strip():    # empty lines
            continue
        if line.strip().startswith("#"): # allow comment
            continue
        k,v = [one.strip() for one in line.split(':',1)]
        ret[k] = v
    return ret

def parse(text):

    """Parse a pass file into a data structure.  The first line is taken
    to be the password and will be placed in the `password` item of
    the returned ditionary.  The schema which the remaining text
    follows will be guessed and parsed based on the guess.

    """
    pw,rest = text.split('\n',1)

    if rest.strip().startswith("{"):
        ret = parse_as_json(rest)

    elif ':' in rest.split('\n',1)[0]:
        ret = parse_as_preferred(rest)

    ret['password'] = pw
    return ret

    
