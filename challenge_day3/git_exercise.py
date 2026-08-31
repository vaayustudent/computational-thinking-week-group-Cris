import crisvsfile
import lucas
import namestring
import oliver
import sb

def TeamName():
    print ("This is Team Cris. We are:")
    print (crisvsfile.get_name())
    print (lucas.name())
    print (namestring.get_name())
    print (oliver.get_name())
    print (sb.get_name())

if __name__ == "__main__":
    TeamName()
