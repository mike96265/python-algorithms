"""
Given an image represented by an NxN matrix, where each pixel in the image is 4 byte, write a method to rotate
the image by 90 degrees,Can you do this in place.
"""


class Solution:

    def RotateMatrix(self, matrix):
        width, brith = len(matrix), len(matrix[0])
