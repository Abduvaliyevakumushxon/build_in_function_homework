def main(x, y):
    """Integer type variables 'x' and 'y' are given. Return the value of the expression in README.md file.
    https://github.com/codeschool43/Build_in_function_homework#build_func07

    Args:
        x (int): integer
        y (int): integer
        
    Returns:
        int: the value of the expression
    """
    natija=pow(x,2)
    natija1=(pow(x,3)*6)
    natija2=(x*3*y)
    natija3=natija+natija1+natija2
    return natija3
print(main(5,2))