"""This part I solved it with the part 1 code by running the program repeatedly for different A values.

But the range is huge. So I tried to narrow it down. First I found out from printing the output of multiple A values that some pattern is going on.

Output pattern,
* first it went with 1 char, then 2 char and so on. They all increased with respect to 8. So using that I narrowed down my search to include only 16 chars start and end.

To further narrow down, I've used partial match to match first few chars of the iteration with the target. That narrowed the range further. So using that I found the answer by stepping
through range and try to match.

There are better solutions that uses some kind of reverse engineering to find out the answer. I'll try to do that in future whenever I can.
"""  # noqa: D404
print("Solved mostly by staring at the screen lol!")
