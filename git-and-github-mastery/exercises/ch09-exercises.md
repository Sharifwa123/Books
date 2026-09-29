# Chapter 9 exercises — The Problem of Changing Files

Attempt each exercise before you open `solutions/ch09-solutions.md`. Work only inside `sharif-git-lab`.

## Level 1 — Guided

**1.1 Reproduce the names.** In `sharif-git-lab`, type the commands of section 9.1 (from `mkdir menu-history` to `ls`). *Expected result:* the same five files as the recording (the order may differ on your system).

**1.2 Read a diff.** Run the two `diff` commands. In your own words, say what each report line means.

## Level 2 — Partially guided

**2.1 Reproduce the collision.** Type the commands of section 9.2.1. *Expected result:* the final `shared/menu.txt` has no `Cake` line. Explain, in two sentences, why no error appeared.

**2.2 Name the difficulty.** For each situation, say which of the six difficulties it shows: (a) "Is this the latest?" (b) "Why did we change the price?" (c) "Who deleted the cake line?" (d) "I saved over the old version by mistake."

## Level 3 — Independent

**3.1** Design a safer working method for Alice and Bob *without* version-control software. Write down the rules you would impose. Then list two ways the rules could still fail. (This is what people did before version control.)

## Level 4 — Professional scenario

**4.1** A five-person volunteer group edits one shared price list every week using a synchronised folder. Twice this month someone's change disappeared. Explain what is probably happening, what a synchronised folder does and does not record, and recommend one change of working method.

## Level 5 — Troubleshooting

**5.1** In section 9.2.1 you have Alice's private copy, Bob's private copy, and the shared file (which contains only Bob's change). Recover a shared menu that holds **both** the cake and the new bread price. What did you have to do by hand, and what would you want a tool to do for you?

**5.2** Someone says: "Our backup runs every night, so we have version control." Give two reasons why that is not correct.
