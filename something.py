def maximize_equal_numbers(A, K):
    events = []
    for x in A:
        events.append((x - K, +1))  # start of range
        events.append((x + K, -1))  # end of range

    # Sort events by the position; if equal, start events (+1) come before end events (-1)
    events.sort(key=lambda event: (event[0], -event[1]))

    current_overlap = 0
    max_overlap = 0
    for pos, delta in events:
        current_overlap += delta
        max_overlap = max(max_overlap, current_overlap)
    
    return max_overlap

# Example usage:
A = [5, 7, 10, 8, 15]
K = 4
print(maximize_equal_numbers(A, K))  # Should print 5 in the sample explained.
