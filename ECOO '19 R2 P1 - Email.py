for _ in range(10):
    q = int(input())
    emails = set()
    for _ in range(q):
        email = input().lower()
        local, domain = email.split('@')
        local = local.replace('.', '')
        if '+' in local:
            local = local[:local.index('+')]
        email = f"{local}@{domain}"
        emails.add(email)
    print(len(emails))

# regex solution for fun
# import re
#
# for _ in range(10):
#     q = int(input())
#     emails = set()
#     for _ in range(q):
#         email = input().lower()
#         local, domain = email.split('@')
#         local = re.sub(r'\.', '', local)
#         local = re.sub(r'\+.*', '', local)
#         email = f"{local}@{domain}"
#         emails.add(email)
#     print(len(emails))
