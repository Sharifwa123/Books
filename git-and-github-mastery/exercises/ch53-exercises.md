# Chapter 53 exercises — YAML for Beginners

Attempt each exercise before you open `solutions/ch53-solutions.md`. You need Python 3 with PyYAML (`python3 -c "import yaml"` should not fail) or an online YAML checker that you trust with non-secret text.

## Level 1 — Guided

**1.1 A map.** Write a YAML map with the keys `name`, `open` (true) and `loaf` (2.80). Parse it and read the result.

**1.2 A list.** Write a list of three menu items under the key `items`. Parse it.

## Level 2 — Partially guided

**2.1 Nested.** Write a map `prices` nested inside another map, with two prices. Then write a list inside a map inside a list.

**2.2 The trailing zero.** Parse `version: 3.10`, then `version: "3.10"`. Explain the difference.

## Level 3 — Independent

**3.1 The word no.** Parse `answer: no` and `answer: "no"`. What does your parser do? What would you write to be safe with any parser?

**3.2 Break it.** Make each of these mistakes and read the error class: (a) a tab indent; (b) a sibling one space out of line; (c) a missing space after a colon.

## Level 4 — Professional scenario

**4.1 Debugging a file.** A colleague sends a file that "does nothing". Using the checklist of section 53.4, write the five checks you would make, in order.

## Level 5 — Troubleshooting

**5.1** A version key `python: 3.10` is read as `3.1` and the wrong interpreter is chosen. Explain and fix.

**5.2** A linter says the key `on` is a Boolean. Give two things to check before changing the file.
