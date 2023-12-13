def main(x, y):
    """Integer type variables 'x' and 'y' are given. Return the value of the expression in README.md file.
    https://github.com/codeschool43/Build_in_function_homework#build_func09

    Args:
        x (int): integer
        y (int): integer
        
    Returns:
        int: the value of the expression
    """
    natija=pow(y,3)
    natija1=(pow(x,2)*y)
    natija2=natija+natija1
    natija3=natija2*2
    return natija3
print(main(2,4))
