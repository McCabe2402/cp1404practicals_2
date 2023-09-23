
"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
# Used to be if score < 0
# print("Invalid score")
# This now prevents scores over and below the range to be input.
if score < 0 or score > 100:
    print("Invalid score")
    # Replacing the if with elif checks if previous score is invalid and needs new outcome.
    # Need to find a way to simplify further. (Found it, by replacing last elif with an else I can make it so anything -
    # else that wasn't stated will be another answer).
    # The previous code also did not have any '=' in them, a 50 now is passable and not Excellent.
elif score >= 90:
    print("Excellent")
    # Works.
elif score >= 50:
    print("Passable")
    # Works.
else:
    # Last line is now only print. Else removes the need for an extra range.
    print("Bad")
