def check_permutation?(str1, str2)
  return false if str1.length != str2.length
  str1_array = Array.new(128,0)
  str2_array = Array.new(128,0)
  for i in 0...str1.length do
    str1_array[str1[i].ord] +=1
    str2_array[str2[i].ord] +=1
  end
  for i in 0...128 do
    return false if str1_array[i] != str2_array[i]
  end
  true
end

puts check_permutation?('umuang', 'ngaamu')
