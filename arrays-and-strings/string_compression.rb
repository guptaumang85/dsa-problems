def string_compression(str)
  new_str = ''
  char = str[0]
  count = 1
  get_new_str = false
  for i in 1...str.length do
    if str[i] == str[i-1]
      count +=1
      get_new_str = true
    else
      new_str = new_str + char + count.to_s
      count = 1
      char = str[i]
    end
  end
  new_str = new_str + char + count.to_s
  get_new_str ? new_str : str
end

puts(string_compression('aabbcddddeef'))
