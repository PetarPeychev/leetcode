package main

func reverseString(s []byte) {
	start := 0
	end := len(s) - 1
	for {
		if start < end {
			a := s[start]
			s[start] = s[end]
			s[end] = a
			start += 1
			end -= 1

		} else {
			return
		}
	}

}
