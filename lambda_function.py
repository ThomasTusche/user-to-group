from ldap3 import Server, Connection, ALL, NTLM, SUBTREE
from ldap3.extend.microsoft.addMembersToGroups import ad_add_members_to_groups as addUsersInGroups
import email
import os
import json

from error_msg import no_user_template, no_group_template, no_permissions_template, success_template

def lambda_handler(event, context):

    # Getting the sender mail and subject from the SES Event

    data = json.loads(event['Records'][0]['Sns']['Message'])
    email = data['mail']['source']
    subjectdata= data['mail']['headers']

    for keypair in subjectdata:
        if keypair['name']=='Subject':
            subject=keypair['value']

    group = subject.split(",")[1]
    user = subject.split(",")[0]


    admin_user = ["ENTER ALL THE EMAIL ADDRESSES WHICH SHOULD BE ABLE TO SEND THIS EMAIL HERE"]
    adgroups = ["ENTER ALL AD GROUPS WHERE PEOPLE CAN BE ASSIGNED TOO HERE"]

    server = Server('IP OF YOU AD SERVER', use_ssl=True, get_info=ALL)

    conn = Connection(server, "CN OF YOUR USER WITH 'Account Operator' PERMISSIONS", "PASSWORD", auto_bind=True, auto_referrals=False)
    

    print("###SENDER###")
    print(email)
    print("###USER###")
    print(user)
    print("###GROUP###")
    print(group)
    print("###SUBJECTDATA###")
    print(subjectdata)

    # If the sender is part of admin_user it looks up the user and group cn
    if email in admin_user:
        user_dn = find_user(user,conn,email)
        group_dn = find_group(group,conn,email)

        print(user_dn)
        print(group_dn)
        addUsersInGroups(conn,user_dn[:-1],group_dn[:-1])

        success_template(email)

    else:
        send_error_mail("no_permission",email)



def find_user(user,conn,email): #Tries to find the user and return the users CN or fires an email with error message back

    user_criteria = "(&(objectClass=user)(sAMAccountName=%s))"%user

    if conn.search("THE BASE OU WHER USERS ARE LOCATED", user_criteria):

        result = str(conn.entries)

        user_dn = result.split("-")[0].replace("[DN: ","")

        return user_dn


    send_error_mail("user",email)
    print("No user found and email was send")
    exit()


def find_group(group,conn,email): #Tries to find the group and return the group CN or fires an email with error message back

    group_criteria = "(&(objectClass=group)(sAMAccountName=%s))"%group

    if conn.search("THE BASE OU WHERE GROUPS ARE LOCATED", group_criteria):

        result_group = str(conn.entries)

        group_dn = result_group.split("-")[0].replace("[DN: ","")

        return group_dn

    send_error_mail("group",email)
    print("No group found and email was send")
    exit()


def send_error_mail(reason,email):
    if reason == "user":
        no_user_template(email)
    elif reason == "group":
        no_group_template(email)
    elif reason == "no_permission":
        no_permissions_template(email)
    return
