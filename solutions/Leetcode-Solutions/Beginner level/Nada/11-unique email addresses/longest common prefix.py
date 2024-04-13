class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set=set()
        for email in emails :
            local_name , domain_name = email.split("@")
            local_name = local_name.replace(".", "")
            local_name = local_name.split("+")[0]
            email_set.add(local_name + "@" + domain_name)

        return len(email_set)