#!/usr/bin/python3
"""
Module to determine if all boxes can be unlocked.
"""

def canUnlockAll(boxes):
    """
    Function to determine if all boxes can be unlocked.

    Args:
        boxes (list of lists): A list where each list contains keys for other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    unlocked = {0}
    keys_to_check = [0]
    
    while keys_to_check:
        current_box = keys_to_check.pop()
        for key in boxes[current_box]:
            if key < len(boxes) and key not in unlocked:
                unlocked.add(key)
                keys_to_check.append(key)
                
    return len(unlocked) == len(boxes)

