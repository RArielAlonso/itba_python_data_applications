"""Function that divides a in b."""

from typing import Union,Optional

def divide(a:Union[float,int],b:Union[float,int],c:Optional[str]=None) -> float :
    """
    Use this function to divide a in b.

    Args:
        a (int): value of numerator
        b (int): value of denominator

    Raises:
        ZeroDivisionError: if b is a 0 value

    Returns:
        float: returned by the function
    """
    if b==0:
        raise ZeroDivisionError("b cannot b equal to 0")
    
    return a / b 