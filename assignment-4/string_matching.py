def naive_string_matching(text, pattern):
    """
    Task 3: Naive string matching algorithm.
    Returns a tuple: (list of starting indices where pattern is found, number of comparisons)
    """
    n = len(text)
    m = len(pattern)
    comparisons = 0
    occurrences = []
    
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            comparisons += 1
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            occurrences.append(i)
            
    return occurrences, comparisons

def compute_lps_array(pattern):
    """Computes the Longest Proper Prefix which is also Suffix array for KMP."""
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_string_matching(text, pattern):
    """
    Task 3: KMP (Knuth-Morris-Pratt) string matching algorithm.
    Returns: (list of starting indices, number of comparisons)
    """
    n = len(text)
    m = len(pattern)
    lps = compute_lps_array(pattern)
    comparisons = 0
    occurrences = []
    
    i = 0
    j = 0
    
    while i < n:
        comparisons += 1
        if pattern[j] == text[i]:
            i += 1
            j += 1
            
        if j == m:
            occurrences.append(i - j)
            j = lps[j - 1]
        elif i < n:
            comparisons += 1 # additional comparison inside elif block logic essentially
            if pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
                    
    return occurrences, comparisons
