#!/usr/bin/python3
"""A module to divide all elements of a matrix.

This module is responsible for dividing all the values of a matrix
according to a divisor given by the user. For the program to work
properly, the following aspects must be taken into account:

    * The matrix must be a list of lists of integers or floats.
    * Each row of the matrix must be of the same size.
    * The divisor must be a number (integer or float) other than 0.
    * The division of all elements of the matrix is rounded off
      to 2 decimal places.
    * The result is delivered in a new matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The divisor number.

    Returns:
        list: A new matrix with all elements divided.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    check_for_list(matrix)
    check_for_divisor(div)

    elem_sizes = set()
    new_list = []

    for elem in matrix:
        if check_for_list(elem) is False:
            raises_matrix_type_error()

        elem_sizes = check_row_size_inconsistency(elem_sizes, elem)
        values = []

        for value in elem:
            if check_for_number(value) is False:
                raises_matrix_type_error()

            values.append(round(value / div, 2))

        new_list.append(values)

    return new_list


def check_for_list(value):
    """Check if the value is of type list.

    Args:
        value (any): The value to verify.

    Raises:
        TypeError: If value isn't a list.
    """
    if type(value) is not list or len(value) == 0:
        raises_matrix_type_error()


def check_for_divisor(div):
    """Check if the divisor is a valid number and not zero.

    Args:
        div (any): The divisor to verify.

    Raises:
        TypeError: If div isn't an integer or float.
        ZeroDivisionError: If div is equal to 0.
    """
    if check_for_number(div) is False:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')


def check_for_number(value):
    """Check if the value is an integer or float.

    Args:
        value (any): The value to verify.

    Returns:
        bool: True if valid, False otherwise.
    """
    if type(value) is not int and type(value) is not float:
        return False

    # Check for NaN
    if value != value:
        return False

    return True


def check_row_size_inconsistency(elem_sizes, row):
    """Ensure all rows in the matrix are of equal size.

    Args:
        elem_sizes (set): Set of unique row sizes.
        row (list): A row from the matrix.

    Returns:
        set: Updated set with current row length.

    Raises:
        TypeError: If rows are of inconsistent sizes.
    """
    elem_sizes.add(len(row))

    if len(elem_sizes) > 1:
        raise TypeError('Each row of the matrix must have the same size')

    return elem_sizes


def raises_matrix_type_error():
    """Raise a matrix type error."""
    raise TypeError('matrix must be a matrix '
                    '(list of lists) of integers/floats') 
