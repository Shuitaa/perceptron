import numpy, random, os


def main():
    learning_rate = 1
    bias = 1
    weights = [random.random(),random.random(),random.random()]
    
    for i in range(50):
        perceptron_training(1, 1, 1, learning_rate, bias, weights)
        perceptron_training(1, 0, 1, learning_rate, bias, weights)
        perceptron_training(0, 1, 1, learning_rate, bias, weights)
        perceptron_training(0, 0, 0, learning_rate, bias, weights)

    perceptron_prod(bias, weights)


def perceptron_training(in_a, in_b, out, learning_rate, bias, weights):
    out_p = in_a * weights[0] + in_b * weights[1] + bias * weights[2]

    if out_p > 0:
        out_p = 1
    else:
        out_p = 0

    err = out - out_p

    weights[0] += err * in_a * learning_rate
    weights[1] += err * in_b * learning_rate
    weights[2] += err * bias * learning_rate

    return out_p

def perceptron_prod(bias, weights):
    x = int(input())
    y = int(input())

    out_p = x * weights[0] + y * weights[1] + bias * weights[2]

    if out_p > 0:
        out_p = 1
    else:
        out_p = 0

    print(x, "or", y, "is : ", out_p)
    
if __name__ == "__main__":
    main()