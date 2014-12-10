from account.models import Account

# The context processor function
def users(request):
    all_users = Account.objects.all()

    return {
        'users': all_users,
    }