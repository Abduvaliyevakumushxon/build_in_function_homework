def main(x, y):
    """Integer type variables 'x' and 'y' are given. Return the value of the expression in README.md file.
    https://github.com/codeschool43/Build_in_function_homework#build_func08

    Args:
        x (int): integer
        y (int): integer
        
    Returns:
        int: the value of the expression
    """
    natija=pow(x,2)
    natija1=pow(y,3)
    natija2=((natija*natija1)*5)
    natija3=pow(y,2)
    natija4=natija3*x
    natija5=natija2+natija4
    return natija5
print(main(7,1))