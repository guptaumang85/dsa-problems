def zero_matrix(matrix)
  row = Array.new(matrix.size)
  column = Array.new(matrix[0].size)

  for i in 0...matrix.size do
    for j in matrix[0].size do
      if matrix[i][j] == 0
        row[i] = true
        column[j] = true
    end
  end

  for i in 0...row.size do
    if row[i] == 0
      nullify_row(matrix, i)
    end
  end

  for j in 0...column.size do
    if column[i] == 0
      nullify_column(matrix, j)
    end
  end
end

def nullify_row(matrix, row)
  for i in 0...matrix[0].length do
    matrix[row][i] = 0
  end
end

def nullify_column(matrix, column)
  for i in 0...matrix.length do
    matrix[i][column] = 0
  end
end