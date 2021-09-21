import re
import this

print(2 + 3)
print(8 - 3)
print(4 * 6)
print(8 / 4)
print(5 / 2)
print(5 // 2)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(8 + 9 * 2)
print((8 + 9) * 2)
print(2 * 2 * 2)
print(2 ** 3)
print('hi')
print('hi ' * 10)
print(r'c:\noob')
x = 2
y = 3
print(x + 3)
print(y - 1)
print(x + y)
x = 9
print(x + y)
name = 'youtube'
print(name[0])
print(name[-1])
print(name[0:])
print(name + ' rocks')
print(len(name))
print(name[-1:])

"ex---List"
nums = [25, 151, 19, 20, 8, 2]
print(nums[0])
name = ['kiran', 'tells', 'reddy']
mil = [nums, name]
print(nums)
print(name)
print(mil)
print('insert')
nums.insert(0, 20)
print(nums)
print('remove')
nums.remove(20)
print(nums)
print('pop without index')
nums.pop()
print(nums)
print('pop with index')
nums.pop(2)
print(nums)
nums.sort()
print(nums)
nums.extend([1, 5, 6])
print(nums)
print(min(nums))
print(max(nums))

num = "0798959"
pattern = r"9"
num = re.sub(pattern, "X", num)
print(num)

a, b, c, d, *e, f, g = range(20)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

if __name__ == '__main__':
    print("hello")
else:
    print("hi")


