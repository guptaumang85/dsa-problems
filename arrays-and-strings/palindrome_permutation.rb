def check_palindrome_permutation(str)
  char_count = Array.new(128, 0)
  center_char_count = 0
  str.split('').each do |char|
    next if char == ' '
    char_count[char.downcase.ord] += 1
  end

  char_count.each do |count|
    if count == 1
      center_char_count += 1
      next
    end  
    return false if count%2 != 0
  end
  center_char_count <= 1
end

puts check_palindrome_permutation('atc  ctA')