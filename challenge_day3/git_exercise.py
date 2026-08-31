import crisvsfile
import lucas
import vaayu
import oliver
import sb

def TeamName():
    print ("This is Team Cris. We are:")
    print (crisvsfile.get_name())
    print (lucas.get_name())
    print (vaayu.get_name())
    print (oliver.get_name())
    print (sb.get_name())

if __name__ == "__main__":
    TeamName()

def shortstory():
    print(lucas.act_one_lucas())
    print(oliver.act_one_oliver())
    print(vaayu.vaayu_act_one())
    print(crisvsfile.cris_act_one())
    print(sb.Jingqi_act_one())
    print(lucas.act_two_lucas())
    print(oliver.act_two_oliver())
    print(vaayu.vaayu_act_two())
    print(crisvsfile.cris_act_two())
    print(sb.Jingqi_act_two())
    print(lucas.act_three_lucas())
    print(oliver.act_three_oliver())
    print(vaayu.vaayu_act_three())
    print(crisvsfile.cris_act_three())
    print(sb.Jingqi_act_three())
if __name__ == "__main__":
    shortstory()
