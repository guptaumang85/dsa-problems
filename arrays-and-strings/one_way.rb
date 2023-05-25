#check if two stings are one(or zero) edits away
require 'pry'

def one_way(str1, str2)
  return false if (str1.length - str2.length).abs > 1
  str1 = str1.split('')
  str2 = str2.split('')
  first_str, second_str = str1.length > str2.length ? [str1, str2] : [str2, str1]

  first_index, second_index = 0, 0
  found_difference = false

  while first_index < first_str.length && second_index < second_str.length do
    if first_str[first_index] != second_str[second_index]
      if found_difference
        return false
      end
      found_difference = true
      if first_str.length == second_str.length
        second_index += 1
      end
    else
      second_index += 1
    end
    first_index += 1
  end
  true
end

puts one_way('gpd', 'gapd')
