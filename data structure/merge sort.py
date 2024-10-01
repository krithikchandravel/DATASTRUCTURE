# Simple Merge Sort implementation
def merge_sort(papers):
    if len(papers) <= 1:
        return papers
    
    mid = len(papers) // 2
    left_half = merge_sort(papers[:mid])
    right_half = merge_sort(papers[mid:])
    
    return merge(left_half, right_half)

# Function to merge two sorted halves
def merge(left, right):
    sorted_list = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    # Add remaining elements
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list


# Example: List of exam papers with (roll_number, marks)
exam_papers = [(45, 85),(12, 92),(78, 56),(34, 74),(23, 88),(56, 64)]

# Print papers before sorting
print("Before sorting:")
for paper in exam_papers:
    print(f"Roll No: {paper[0]}, Marks: {paper[1]}")

# Sort exam papers by roll number
sorted_papers = merge_sort(exam_papers)

# Print papers after sorting
print("\nAfter sorting by roll number:")
for paper in sorted_papers:
    print(f"Roll No: {paper[0]}, Marks: {paper[1]}")
