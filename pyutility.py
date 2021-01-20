# import sys
# import argparse
#
# def cal(args):
#     if args.o == 'add':
#         return args.x + args.y
#     elif args.o == 'mul':
#         return args.x * args.y
#     elif args.o == 'div':
#         return args.x/args.y
#     elif args.o == 'min':
#         return args.x - args.y
#     else :
#         print("error")
# if __name__ == '__main__':
#     parser=argparse.ArgumentParser()
#     parser.add_argument('--x',type='float',default='1.0',
#                         help="Enter first number")
#     parser.add_argument('--y', type='float', default='3.0',
#                           help="Enter first number")
#     parser.add_argument('--o',type='str', default="add",
#                         help="Hello")
#
#     args= parser.parse_args()
#     sys.stdout.write(str(cal(args)))

import argparse
import sys

def calc(args):
    if args.o == 'add':
        return args.x + args.y

    elif args.o == 'mul':
        return args.x * args.y

    elif args.o == 'sub':
        return args.x - args.y

    elif args.o == 'div':
        return args.x / args.y

    else:
        return "Something went wrong"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,
                        help="Enter first number. This is a utility for calculation. Please contact harry bhai")

    parser.add_argument('--y', type=float, default=3.0,
                        help="Enter second number. This is a utility for calculation. Please contact harry bhai")

    parser.add_argument('--o', type=str, default="add",
                        help="This is a utility for calculation. Please contact harry bhai for more")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))