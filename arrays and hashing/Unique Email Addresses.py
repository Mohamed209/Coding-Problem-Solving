# https://leetcode.com/problems/unique-email-addresses/description/
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # forward pass O(n) to modify mails using pre defined rules
        for i in range(len(emails)):
            local, domain = emails[i].split("@")
            local = local.replace(".", "")
            plusidx = local.find("+")
            if plusidx == -1:
                plusidx = len(local)
            local = local[:plusidx]
            emails[i] = local + "@" + domain
        return len(set(emails))


s = Solution()
print(
    s.numUniqueEmails(["test.email+alex@leetcode.com", "test.email.leet+alex@code.com"])
)
