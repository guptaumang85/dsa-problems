def is_unique?(str)
  for i in 0...str.length do
    for j in (i+1)...str.length
      return false if str[i] == str[j]
    end
  end
  true
end

puts is_unique?('umanug')