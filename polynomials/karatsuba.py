#!/usr/bin/env python
#-*- coding:utf-8 -*-

from math import floor, log10

def m_power(num1,num2):

    digits_of_num1 = number_of_digits(num1)
    digits_of_num2 = number_of_digits(num2)

    return min(digits_of_num1,digits_of_num2) / 2

def split_at(number,m_power):

    left_part = int(floor(number / (10 ** m_power)))
    right_part = int(number % (10 ** m_power))

    return (left_part,right_part)

def number_of_digits(number):
    return int(log10(number) + 1)


def karatsuba(num1, num2):

	if (num1 / 10 == 0) or (num2 / 10 == 0):
		return num1 * num2

	# calculates the size of the numbers
	m2 = m_power(num1,num2)

	# split the digit sequences about the middle
	high1, low1 = split_at(num1, m2)
	high2, low2 = split_at(num2, m2)

	# 3 calls made to numbers approximately half the size
	z0 = karatsuba(low1,low2)
	z1 = karatsuba((low1+high1),(low2+high2))
	z2 = karatsuba(high1,high2)

	return (z2 * 10 ** (2 * m2)) + ((z1-z2-z0) * 10 ** (m2)) + (z0)

print karatsuba(1002,1013)
