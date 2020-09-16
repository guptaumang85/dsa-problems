
def longest_common_prefix(strs)
  prefix = strs[0]
  for i in 1...strs.length
    while strs[i].index(prefix) != 0 do
      prefix.slice!(-1)
    end
  end
  prefix

end

puts longest_common_prefix(strs)