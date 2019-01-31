def evenlySpaced(a, b, c):
    def evenlySpacedOrderedArgs(oa, ob, oc):
        return oa + (oc - oa) / 2.0 == ob

    a_before_b = a < b
    b_before_c = b < c
    a_before_c = a < c

    if a_before_b and b_before_c:
        return evenlySpacedOrderedArgs(a, b, c)
    elif a_before_c and c_before_b:
        return evenlySpacedOrderedArgs(a, c, b)
    elif not a_before_b and a_before_c:
        return evenlySpacedOrderedArgs(b, a, c)
    elif b_before_c and not a_before_c:
        return evenlySpacedOrderedArgs(b, c, a)
    elif not a_before_c and a_before_b:
        return evenlySpacedOrderedArgs(c, a, b)
    else:
        return evenlySpacedOrderedArgs(c, b, a)


print evenlySpaced(2, 4, 6), "Should be", True
print evenlySpaced(4, 6, 2), "Should be", True
print evenlySpaced(4, 6, 3), "Should be", False
