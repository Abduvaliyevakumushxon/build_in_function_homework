def main(n):
    """A integer type variable 'n' is given. Return the value of the expression in README.md file.
    https://github.com/codeschool43/Build_in_function_homework#build_func03

    Args:
        n (float): float

    Returns:
        float: the value of the expression
    """
    x=(n+1)
    x1=pow(x,2)
    x2=(x1*3)
    return x2
print(main(3.5))