def rec_seq(n):
    print(f"rec_sqc({n}) called")
    if n == 1:
        print(f"return({n}) = 1")
        return 1
    ret = 3 * rec_seq(n-1)
    print(f"return({n}) = {ret}") 
    return ret

rec_seq_return = rec_seq(3)
print("out=", rec_seq_return)
