#Program to muliply two matrices
def multiply(one, two):
    return [[sum(x*y for x,y in zip(rows,cols)) for cols in zip(*two)]for rows in one]
