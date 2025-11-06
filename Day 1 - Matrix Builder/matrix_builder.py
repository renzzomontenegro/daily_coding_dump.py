
def build_matrix(rows, cols):
    rows = [[0 for _ in range(cols)] for _ in range(rows)]
    return rows

matrix = build_matrix(4,3)

print(f"[")
for i, row in enumerate(matrix):
    if i < len(matrix) - 1:
        print(f" {row},")
    else:
        print(f" {row}")
print(f"]")
