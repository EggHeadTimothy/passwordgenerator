import passwordgeneratorv1
import passwordgeneratorv2
import time


def main():
    reps = 1000
    length = 15
    print('\n')
    print('Testing Password Generator Version 1.0...')
    v1start = time.time()
    for i in range(reps):
        passwordgeneratorv1.generate_password(length)
    v1end = time.time()
    v1time = v1end - v1start
    print('Testing Password Generator Version 2.0...')
    v2start = time.time()
    for i in range(reps):
        passwordgeneratorv2.generate_password(length)
    v2end = time.time()
    v2time = v2end - v2start
    percent_faster = ((v1time - v2time) / v1time) * 100
    percent_faster_round = round(percent_faster, 2)
    print('\n')
    print('Password Generator Version 1.0 took {} seconds to generate'
          ' {} passwords of length {}.'.format(v1time, reps, length))
    print('Password Generator Version 2.0 took {} seconds to generate'
          ' {} passwords of length {}.'.format(v2time, reps, length))
    print('\n2.0 is {}% faster than 1.0'.format(percent_faster_round))
    return 0


if __name__ == '__main__':
    main()
