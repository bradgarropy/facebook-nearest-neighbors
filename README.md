# 🏘 Facebook Nearest Neighbors

_During a recent interview with [Facebook][1], I was asked to complete a coding question on the whiteboard. I liked this question because as I wrote the solution, the interviewer pushed me to increase performance for large data sets._

## ❓ Question

Write a program that finds the n closest points to a point p.

## 🤔 Assumptions

This question didn't contain much information at all, so I had to clarify and put some assumptions in place.

There was no indication of how the list of points would be provided, so I assumed there was a file on the system which contained the relevant data. Based on this assumption, my solution accepts a file path as input from which to read the points.

I went a little above and beyond here and created [tools/neighbors.py][2], a script which generates a file with as many points as you specify.

## 💀 Execution

If you want to see my solution, clone the repository and execute it locally!

```
git clone https://github.com/bradgarropy/facebook-nearest-neighbors.git
cd facebook-nearest-neighbors
python fnn.py neighbors.txt -o '(0, 0)' -n 3
```

[1]: https://www.facebook.com/careers
[2]: https://github.com/bradgarropy/facebook-nearest-neighbors/blob/master/tools/neighbors.py
