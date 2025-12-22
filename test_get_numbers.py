#!/usr/bin/env python3

import get_numbers

def test_works():
    assert get_numbers.TestWorks() == True

def test_train_8013():
    image_path = "trains/8013.png"
    numbers = get_numbers.ProcessTrain(image_path)
    assert numbers == [8013]

def test_train_3263():
    image_path = "trains/3263.png"
    numbers = get_numbers.ProcessTrain(image_path)
    assert numbers == [3263]

def test_train_7941():
    image_path = "trains/7941.png"
    numbers = get_numbers.ProcessTrain(image_path)
    assert numbers == [7941]

def test_train_2875():
    image_path = "trains/2875.png"
    numbers = get_numbers.ProcessTrain(image_path)
    assert numbers == [2875]
