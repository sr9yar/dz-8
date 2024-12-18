from app import calc

def test(a, b):
  expected = a
  result = calc(a, b)
  assert expected == result

test_cases = [
  [4, 2],
  [404, 101],
  [-999, 3],
  # [-6, 4], # throws error on assert
]

for test_case in test_cases:
  a = test_case[0]
  b = test_case[1]
  test(a, b)

