import numpy, random, os


def main():
    learning_rate = 1
    bias = 1
    weights = [random.random(),random.random(),random.random()]


def perceptron(in_a, in_b, out, learning_rate, bias, weights):
    out_p = in_a * weights[0] + in_b * weights[1] + bias * weights[3]

    if out_p > 0:
        out_p = 1
    else:
        out_p = 0

    err = out - out_p

    weights[0] += err * in_a * learning_rate
    weights[0] += err * in_b * learning_rate
    weights[0] += err * bias * learning_rate

    return out_p
    
if __name__ == "__main__":
    main()