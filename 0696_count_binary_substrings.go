package main

func countBinarySubstrings(s string) int {
	zeros := 0
	ones := 0
	substrings := 0
	var currentDigit rune

	for _, c := range s {
		if c == currentDigit {
			if c == '0' {
				zeros += 1
			} else if c == '1' {
				ones += 1
			}
		} else {
			currentDigit = c
			if c == '0' {
				zeros = 1
			} else {
				ones = 1
			}
		}

		if (c == '0' && ones >= zeros) || (c == '1' && zeros >= ones) {
			substrings += 1
		}
	}

	return substrings
}
