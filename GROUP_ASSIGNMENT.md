# Group assignment: foundation plus three later-topic extensions

**Deadline for all groups: end of Wednesday, 21 October 2026, Uganda time.** This means midnight as Wednesday changes to Thursday, 22 October (00:00 EAT / UTC+3).

This is the current assignment for existing and catch-up groups. The earlier 15 October date has been replaced for this combined submission. Existing groups keep their completed foundation code and PRs; they add three later-topic choices. New groups complete their assigned foundation work and the same three-choice later-topic stage.

A fork is your group's copy of the repository. A branch is one person's working version. A pull request, or PR, asks teammates to review a branch before its changes join `main`. The final group `main` must contain every member's work and merged PRs.

## 1. Choose the work and share it fairly

**Existing groups:** keep your current story. Its `EXTENSIONS.md` has six foundation tasks. A five-member group completes any five different tasks; a six-member group completes all six. Each member owns one task. Keep your completed work and its original contribution records.

**Catch-up groups:** use the story assigned in [CATCH_UP_GROUPS.md](CATCH_UP_GROUPS.md). Each new story has eight foundation choices. Groups of eight complete all eight; the group of seven chooses any seven. Each member owns one task.

**All groups:** open your story's `ADVANCED_EXTENSIONS.md` and choose any **three different options** from A1–A5. Innovation is one of the choices; it is not a compulsory fourth feature. Agree on the three IDs before work begins. Keep the existing foundation contributions and add genuinely new later-topic work.

Every member contributes code or meaningful automated tests to at least one chosen later-topic option and authors a later-topic PR. Split larger features among members; do not leave someone with only their name in a report. Everyone reviews all teammates' PRs with a useful comment.

Read [LATER_TOPICS_GUIDE.md](LATER_TOPICS_GUIDE.md) before starting an unfamiliar topic. You may learn from documentation and discuss ideas, but each member must understand and explain their own work.

## 2. Make one fork for the group

Choose one member to own the group's fork. That member signs in to GitHub, opens [the class repository](https://github.com/slubambo/ucu-oop-class-examples), and clicks **Fork**. Create the fork under that member's account.

All members use **this same group fork**. You do not need a separate fork for each member. Keep the default branch name `main`.

If your group already made a fork before this assignment was added, use **Sync fork** on its GitHub page to bring in the latest instructions before starting. If GitHub reports a conflict, ask for help rather than discarding the group's work.

## 3. Give every member access

The fork owner opens the **group fork**, then **Settings → Collaborators → Add people**. Invite all the other members by their GitHub usernames. Each person must accept the invitation. The owner already has access and does not need to invite themselves.

Each member needs their own GitHub account. Do not all commit or review using the owner's account: the contribution and review must show who did the work. GitHub's [collaborator guide](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/inviting-collaborators-to-a-personal-repository) explains these steps.

## 4. Download the group fork and create your own branch

Clone the **group fork**, not the lecturer's repository. On its GitHub page, open **Code**, copy its HTTPS URL, and use that URL with `git clone`.

For example, replace `GROUP-OWNER` and `GROUP-REPO` with the account and repository name shown on your group's GitHub page:

```sh
git clone https://github.com/GROUP-OWNER/GROUP-REPO.git
cd GROUP-REPO
git switch main
git pull origin main
git switch -c amina-26b12345
```

Use a short branch name containing **your first name and university access number**. `amina-26b12345` is a made-up example. Replace it with your own details, use lower-case letters, and replace spaces or slashes with hyphens.

Each member creates a different branch. Code on your personal branch; changes reach `main` through a reviewed PR.

If you use GitHub Desktop, clone the group fork, fetch the latest `main`, and choose **New branch** with your personal branch name. The same assignment rules apply.

## 5. Write your contribution and show that it works

For foundation work, follow your story's `EXTENSIONS.md`: add the feature and a personal demo. For later-topic work, follow `ADVANCED_EXTENSIONS.md`: you may add modules, demos and test files. Keep the original `story.py` entry point and its public methods available so the original story and earlier demos still work.

Use your own branch and Git identity. Each member needs their own foundation PR and at least one later-topic PR containing code or meaningful automated tests. If your foundation PR is already merged, keep it as evidence; you do not need to repeat it. Do not make an empty PR just to record your name.

Record the three chosen advanced option IDs and split the work among all members before coding. A larger option may have several authors, each with a clear subtask and their own PR. Describe which part you wrote and which checks you ran. Documentation and review alone do not replace your coding/testing contribution.

Run the original story, the relevant demos and the checks for your contribution. On the final combined branch, all demos and tests must work together. Keep the original `main()` and `expected_output.txt` as the starting story. Add stricter behaviour through new methods or wrappers rather than making the original demonstration crash.

Make sure Git uses your name and an email linked to your GitHub account, or your GitHub-provided private email. For example, replace the paths and branch name below with yours:

```sh
git add stories/01_rolex_rescue/story.py stories/01_rolex_rescue/demo_amina_26b12345.py
git commit -m "Add lunch wallet top-up and demo"
git push -u origin amina-26b12345
```

In GitHub Desktop, review your changed files, enter a clear commit message, commit to your personal branch, then publish or push that branch. For a later-topic PR, start a new personal branch from the latest group `main`; you can add a short suffix such as `amina-26b12345-json`.

## 6. Open a PR into your group's main branch

On the **group fork**, open **Pull requests → New pull request**. Check the destination before creating it:

| Field | Choose |
|---|---|
| Base repository | Your group's fork |
| Base branch | `main` |
| Head/compare repository | Your group's fork |
| Compare branch | Your personal branch |

A fork can suggest the lecturer's repository as the destination. For this assignment, change the base repository to **your group's fork**. All members' work must come together in the group's `main` branch. GitHub's [PR guide](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request-from-a-fork) explains the base and compare fields.

Use a clear title, such as `Extension 2: lunch wallet top-up — Amina`.

In the PR description, write:

- Your name, access number, registration number and foundation task or later-topic option ID.
- What you added and where it is in the code.
- How to run your demo.
- The inputs, expected results and actual results for your checks.

Each member must author their own PRs. Ask all the other members to review them.

## 7. Everyone reviews and comments before merge

For **each PR**, every other group member must:

1. Open **Files changed** and read the code.
2. Run the proposed change, or go through its demo with the author and check the results.
3. Leave at least one useful comment on that PR. Name a method, a rule or a case you checked. Explain what works or what should change.
4. If you started a pending review, **submit it** so the author can see the comment.

Examples of useful comments:

> I tried a top-up of zero. The method returned False and the balance stayed the same. This matches the rule.

> This method should refuse a negative amount before changing the balance. Please add that check and show the result in the demo.

“Good”, “done” or an emoji alone is not enough. The author responds to questions and fixes problems on the **same branch**. Pushing more commits updates the same PR; there is no need to open a replacement PR for each fix.

Each PR needs useful comments from **all the author’s teammates** before merge: four reviewers in a group of five, five in a group of six, six in a group of seven, or seven in a group of eight. The author checks their own work and responds, but does not count as a teammate reviewer on their own PR. GitHub also does not allow authors to approve their own PRs. See [GitHub's review guide](https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/reviewing-proposed-changes-in-a-pull-request).

Everyone therefore reviews all the other members' PRs. If a new commit changes a part you reviewed, check that change again before the PR is merged.

## 8. Bring in the latest group work and merge

Merge PRs **one at a time**, after all teammate comments are present and requested fixes are complete. A member with access can perform the merge; the PR must still be authored by the person who did that extension.

Before merging your PR, bring the group's latest `main` into your branch and run the original story and **all available member demos** again. On your personal branch:

```sh
git fetch origin
git merge origin/main
```

If Git reports a conflict, the group has changed the same lines in different branches. Work with the other author, keep both intended features, remove the conflict markers and run the code again. Stage the resolved files and complete the merge commit as Git instructs, then push your branch. Do not replace the file with only your own version and lose another person's extension.

Once the code works and the review is complete, use **Merge pull request → Create a merge commit → Confirm merge**. Use the merge-commit option for this assignment so the group history clearly keeps each member's work and its PR.

After a PR is merged, each member updates their own local `main`:

```sh
git switch main
git pull origin main
```

If you still have uncommitted work on your personal branch, commit it there before switching. To continue your extension, switch back to your personal branch and bring in the latest `origin/main` before making more edits.

## 9. Record the group's work

Copy [GROUP_TEMPLATE.md](GROUP_TEMPLATE.md) to `GROUP.md` in the root of the group fork. Existing groups should extend their existing file rather than erase the earlier contribution record.

Your `GROUP.md` must include:

- Your story title and group number or catch-up label.
- A complete member list: **full name, university access number, registration number and GitHub username for every person**. Access and registration numbers are separate fields; include both.
- Each member's foundation task, later-topic responsibility, branch names, commit links and merged PR links.
- Links to useful review comments each member left on teammates' PRs.
- The three chosen later-topic IDs, and exact commands for the original story, demos and automated checks.
- **One short group evaluation of no more than 250 words.** Explain what you built, which OOP ideas you used, what worked, the main difficulty and how you handled it, and any remaining limitation. This is one evaluation for the whole group, not 250 words per person.

Use your own GitHub account for commits, PRs and reviews. Keep these records in GitHub rather than replacing them with screenshots. Other members may help, but the author and reviewer of each contribution must be clear.

Keep the actual number of member rows: five or six for the original groups, seven or eight for the catch-up groups. Do not publish the lecturer's attendance PDF or a copy of the full class roster; your own group record is enough.

## 10. Submit your group work

Submit the **GitHub repository link for your group fork**, with the completed work on `main`, through the normal class submission channel by the end of **Wednesday, 21 October 2026, Uganda time**. The cut-off is midnight as Wednesday changes to Thursday, 22 October.

Before submitting:

- [ ] The required one-foundation-task-per-member work is complete.
- [ ] Exactly three later-topic choices are clearly recorded.
- [ ] Every member has their own foundation contribution and a merged later-topic PR with code or meaningful automated tests.
- [ ] Every PR has useful comments from all its author's teammates, made before merge.
- [ ] The original story still runs and matches its original expected output.
- [ ] Foundation demos, later-topic demos and automated checks run together on final `main`.
- [ ] No merge conflict markers remain.
- [ ] `GROUP.md` lists every member's full name, access number, registration number and GitHub username.
- [ ] The story title, responsibilities, branch/commit/PR links, review links and run/check commands are recorded.
- [ ] The group evaluation is complete and does not exceed 250 words.

An open PR, an unmerged branch or work copied to `main` without its author's PR does not meet the contribution requirement.
