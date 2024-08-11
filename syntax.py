def my_range(stop: float, start = 0.0, step = 1.0)
    result =[]
    while start <= stop:
        result.append(start)
        start += step
    return result   
