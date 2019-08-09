#!/usr/bin/env python
#coding=utf-8

from itertools import *
import random
import sys

def read_file(name):
    with open(name) as f:
        return [word for line in f for word in line.split()]

parts = [
    [
        read_file("1.txt"),
        read_file("2.txt"),
        read_file("3.txt"),
    ],
    [
        read_file("4.txt"),
        read_file("5.txt"),
        read_file("6.txt"),
    ],
    [
        read_file("7.txt"),
        read_file("8.txt"),
        read_file("9.txt"),
    ]
]

def shuffle():
    #random.shuffle(parts)
    for component in parts:
        for l in component:
            random.shuffle(l)

poems = []

indexed_words = []
word_count = 0

part_index = []
line_indexes = {}

line_index = 0

limit = 335
current = 0
while current < limit:
    current += 1
    shuffle()
    words = []
    for part in parts:
        for line in part:
            for word in line:
                words.append(word)
                break

    for i, word in enumerate(words):
        if i % 3 == 0:
            sys.stdout.write("\n")

        sys.stdout.write(word + " ")
    sys.stdin.readline()
