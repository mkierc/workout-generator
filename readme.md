# Workout Generator

Generate random sets of physical exercises from [Jordan Yeoh Fitness][1]:

```
λ workout.py

992 requests from random.org are left available today.
How many sets? 3
3-Minute No Gym Fat Burning                 https://www.youtube.com/watch?v=XZQy3kqlbnM        0
3-Minute Fat Burning Progression            https://www.youtube.com/watch?v=lyxCEbNAVpQ        0
9 Minutes Fat Burning: Round 2/3            https://www.youtube.com/watch?v=YUEs8yQ-MBs&t=191  0
```

It was really boring for me to do 3-4 rounds of the exact same workout, so I ended up generating
a set of integers from [random.org][2] and did few different workout routines.

This program basically does the same thing, but automagically.

True randomness is sourced from [random.org][2] service, you need to generate an [API key][3]
and save it as 'api.key' file to be able to use it.

Someday I'd like to generate my own entire workouts based on exercises that Jordan does in
his, and maybe create another project with custom timer and other fun stuff.


## TODO

- [x] Basic functionality of generating sets of workouts
- [x] Pretty printing the workout links with padding
- [ ] Separate the workouts by intensity
- [ ] Order the workouts in generated set by intensity (from most intense to least intense)
- [ ] Don't generate sets of all-intense or all-light workouts
- [ ] Generate a custom workout from single exercises

[1]: https://www.youtube.com/channel/UC4GJndVHEhdmqLFBHOCi97A
[2]: https://www.random.org
[3]: https://api.random.org/json-rpc/1/
