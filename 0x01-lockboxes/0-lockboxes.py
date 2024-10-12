#!/usr/bin/python3
def canUnlockAll(boxes):
    unlocked = {0}
    keys_to_check = [0]

    while keys_to_check:
        current_box = keys_to_check.pop()
        for key in boxes[current_box]:
            if key < len(boxes) and key not in unlocked:
                unlocked.add(key)
                keys_to_check.append(key)

    return len(unlocked) == len(boxes)
