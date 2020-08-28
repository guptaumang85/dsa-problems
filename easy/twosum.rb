# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
    values = {}
    for i in 0..(nums.length-1)
        unless values[target - nums[i]].nil?
            return [values[target - nums[i]], i]
        else
            values[nums[i]] = i
        end
    end
end