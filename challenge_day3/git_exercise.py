import crisvsfile
import lucas
import namestring
import oliver
import sb



def our_team():
    print("This is Team Cris. We are:")
    for member in (crisvsfile, lucas, namestring, oliver, sb):
        if hasattr(member, "get_name"):
            result = member.get_name()
        elif hasattr(member, "name"):
            result = member.name()
        else:
            result = "Unknown member"

        if callable(result):
            result = result()

        if result is None:
            result = "Unknown member"

        print(result)
