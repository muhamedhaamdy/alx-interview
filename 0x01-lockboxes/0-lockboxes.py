#!/usr/bin/python3

def canUnlockAll(boxes):
    unlocked = [0] * len(boxes)
    stack = []
    unlocked[0] = 1
    stack.append(boxes[0])
    while len(stack):
        box = stack.pop()
        for key in box:
            if not unlocked[key]:
                stack.append(boxes[key])
                unlocked[key] = 1
    return True if sum(unlocked) == len(boxes) else False
