def get_optimal_value(capacity, weights, values):
    value = 0.

    valuePerWeight = valuePerWeight = sorted([[v / w, w] for v,w in zip(values,weights)], reverse=True)
    while capacity > 0 and valuePerWeight:
        maxi = 0
        idx = None
        for i,item in enumerate(valuePerWeight):
            if item [1] > 0 and maxi < item [0]:
                maxi = item [0]
                idx = i

        if idx is None:
            return 0.

        v = valuePerWeight[idx][0]
        w = valuePerWeight[idx][1]

        if w <= capacity:
            value += v*w
            capacity -= w
        else:
            if w > 0:
                value += capacity * v
                return value
        valuePerWeight.pop(idx)

    return value

if __name__ == "__main__":
    n = 3
    capacity = 50
    values = [403, 17, 24, 36, 102]
    weights = [20, 50, 30.87, 40, 30]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value)) # print 180.0000000000