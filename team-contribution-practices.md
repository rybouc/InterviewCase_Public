# Team contribution practices
---

**Purpose**: Define when pull requests (PRs) can be self-approved, when reviews are required (and by whom), and when the team must be notified.

**Intent**: Having a repository like this where the growth pod collaboratively invests will allow us to leverage data science best practices, tools to make us more efficient, and domain knowledge. So changing a shared-tools script that others have started to rely on impacts others. Additionally, this repository is used by people using agents in their workflow. The agents can pick up anything in this code base - so introducing an incorrect skill could influence the outcomes of others. 

**General Guidance**: Don't change the contributions from others without approval. Inform people of proposed changes and additions so they can opt-in to review the changes. 

---

## Rules by area
| Repo area	| Type of change	| Can self-approve?	| Required approvals / reviewers	| Team notification required? |
|---|---|---|---|---|
| .github/copilot-instructions.md	| Any change	| No	| Approval required from **everyone** on the team	| Yes via adding mandatory reviewers to PR | 
| projects/	| Any contribution to your own project	| Yes	| None	| No | 
| skills/	| New skill	| No	| 1 reviewer	| Yes — inform team via Teams once the PR is created |
| skills/	| Modify existing skill	| No	| Approval required from the original skill author, or 1 additional team member if you are the original author	| Yes — inform team via Teams once the PR is created | 
| shared-tools/	| Add new tool	| Yes	| None	| Yes — inform team once it is on the main branch | 
| shared-tools/	| Modify existing tool	| No	| Approval required from the original tool author, or 1 additional team member if you are the original author	| Yes — inform team via Teams once the PR is created |
| templates/	| Add new template	| Yes	| None	| Yes — inform team once it is on the main branch |
| templates/	| Modify existing template	| No	| Approval required from the original template creator, or 1 additional team member if you are the original author	| Yes — inform team via Teams once the PR is created | 
| team-contribution-practices.md	| Any change	| No	| Approval required from **everyone** on the team	| Yes via adding mandatory reviewers to PR | 

---
## What to ask for in a review
Please be specific in what you are asking for from reviewers of your PR, and why you are asking for them specifically for the review. Such as: 
- Please test out this shared-tools function on something yourself to make sure it works.
- Please confirm if this domain knowledge is correct.
- Please help me evaluate if this skill contradicts any other skills.
