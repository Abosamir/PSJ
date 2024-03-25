def numUniqueEmails(self, emails: list[str]) -> int:
    list_of_different_emails = []
    new_mail = ""
    for email in emails:
        local_name, domain_name = email.split("@")
        true_local_name = local_name.split("+")[0]
        true_local_name = true_local_name.replace(".","")
        new_mail = true_local_name + "@" + domain_name

        if new_mail not in list_of_different_emails:
            list_of_different_emails.append(new_mail)
    
    return len(list_of_different_emails)



print(numUniqueEmails("f",["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))