# -*- coding: utf-8 -*-
# @Time    : 2022-09-06 11:34 p.m.
# @Author  : qkzhong
# @FileName: HJ054.py
# @Software: PyCharm

expression = '(' + input() + ')'
expression = expression.replace('(-', '(0-')
num_stack = []
op_stack = ['(']
num = 0
op1 = {'+', '-'}
op2 = {'*', '/'}


def do_operate():
    num2 = num_stack.pop()
    num1 = num_stack.pop()
    op = op_stack.pop()
    result = 0
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 // num2
    num_stack.append(result)


for i in range(1, expression.__len__()):
    if expression[i].isdigit():
        num = num * 10 + int(expression[i])
        if not expression[i + 1].isdigit():
            # 数字入栈
            num_stack.append(num)
            num = 0
    elif expression[i] == '(':
        op_stack.append(expression[i])
    elif expression[i] == ')':  # 操作括号里的所有操作
        while op_stack[- 1] != '(':
            do_operate()
        op_stack.pop()
    else:
        # 判断操作栈是否为空
        while op_stack[- 1] != '(':
            if (expression[i] in op1 and op_stack[- 1] in op1) \
                    or (expression[i] in op1 and op_stack[- 1] in op2) \
                    or (expression[i] in op2 and op_stack[- 1] in op2):  # 操作前两个运算
                do_operate()

            else:
                break
        op_stack.append(expression[i])

print(num_stack[0])

