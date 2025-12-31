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

# often can be misread as 2675
def test_train_2875():
    image_path = "trains/2875.png"
    numbers = get_numbers.ProcessTrain(image_path)
    assert numbers == [2875]

# For whatever reason white letter on a black train work best with the raw image
# Probably would be better to adjust our thresholds to get this to work.
def test_train_1027():
    image_path = "trains/1027.png"
    numbers = get_numbers.ProcessTrain(image_path)
    assert numbers == [1027]

def test_train_1009():
    image_path = "trains/1009.png"
    numbers = get_numbers.ProcessTrain(image_path)
    assert numbers == [1009]
