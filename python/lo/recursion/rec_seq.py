def rec_seq(n):
    print(f"rec_sqc({n}) called")
    if n == 1:
        return 1
    return 3 * rec_seq(n-1)

rec_seq_return = rec_seq(3)
print(rec_seq_return)
