def ParseDegreeString(ddmmss):
    # Find the positions of degree, minute, and second symbols
    deg_pos = ddmmss.find(chr(176))
    min_pos = ddmmss.find("'")
    sec_pos = ddmmss.find('"')

    # Extract degrees, minutes, and seconds
    degrees = float(ddmmss[:deg_pos])
    minutes = float(ddmmss[deg_pos+1:min_pos])
    seconds = float(ddmmss[min_pos+1:sec_pos])

    return degrees, minutes, seconds

def DDMMSStoDecimal(degrees, minutes, seconds):
    # Convert degrees, minutes, and seconds to decimal degrees
    decimal_degrees = degrees + (minutes / 60) + (seconds / 3600)
    return decimal_degrees