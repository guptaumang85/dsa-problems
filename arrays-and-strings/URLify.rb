def replace_spaces(str, true_length)
  space_count = 0
  for i in 0...true_length do
    if str[i] == ' '
      space_count += 1
    end
  end
  
  total_count = true_length + space_count*2

  (0..(true_length-1)).reverse_each do |i|
    if str[i] == ' '
      str[total_count-1] = '0'
      str[total_count-2] = '2'
      str[total_count-3] = '%'
      total_count = total_count - 3
    else
      str[total_count-1] = str[i]
      total_count = total_count -1
    end
  end
  str
end

puts replace_spaces("Mr John Smith     ", 13)
