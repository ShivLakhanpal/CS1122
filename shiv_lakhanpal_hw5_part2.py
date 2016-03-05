#Shiv Lakhanpal
#svl238
#Homework 5 part 2
#Disassembler

INS_REF = {
    1: "ADD",
    2: "SUB",
    3: "STA",
    5: "LDA",
    6: "BRA",
    7: "BRZ",
    8: "BRP",
    901: "INP",
    902: "OUT",
    000: "HLT",
}

def disassemble(int_code_operation):
    if int_code_operation[0]=='1':
        output="ADD "+str(int_code_operation[1:])   #1
        return output
    
    elif int_code_operation[0]=='2':
        output="SUB "+str(int_code_operation[1:])   #2
        return output
    
    elif int_code_operation[0]=='3':
        output="STA "+str(int_code_operation[1:])   #3
        return output
    
    elif int_code_operation[0]=='5':
        output="LDA "+str(int_code_operation[1:])   #4
        return output
    
    elif int_code_operation[0]=='7':
        output="BRZ "+str(int_code_operation[1:])   #5
        return output
    
    elif int_code_operation[0]=='8':
        output="BRP "+str(int_code_operation[1:])   #6
        return output
    
    elif int_code_operation=='901':                 #7
        return "INP "
    
    elif int_code_operation=='902':                 #8
        return "OUT "
    
    elif int_code_operation=='000':                 #9
        return "HLT "
    
    else:
        return "DAT "+str(int_code_operation[1:])   #10



def main():
    command_list = []
    
    halt_noticed = False
    
    while (halt_noticed == False):
        
        item = str(input("Enter an instruction please: "))
        
        if item=="000":
            halt_noticed = True
        command_list.append(item)
        
    for item in command_list:
        output = disassemble(item)
        print(output)
    
main()
