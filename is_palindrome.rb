# @param {Integer} x
# @return {Boolean}
require 'pry'
def is_palindrome(x)
  rev_x = ''
  x = x.to_s
    
  for i in (x.length-1).downto(0)
    rev_x += x[i]
  end
  return x == rev_x
    
end

is_palindrome(121)