from Function import *

if __name__ =='__main__':

    #All file go back to null
    f = open('Work_files/Standardized.txt', "w")
    f1 = open('Work_files/Complete.txt', "w")
    f2 = open('Work_files/deterministic.txt', "w")
    f3 = open('Work_files/Minimized.txt', "w")
    f4 = open('Work_files/Completementaire.txt', "w")
    f.close()
    f1.close()
    f2.close()
    f3.close()
    f4.close()


    print('\n\nHello welcome to this programme !')
    print('We will check together some automata, let\' start !')

    M_loop = 1


    #Main loop
    while M_loop:
        n_s = []
        column = []
        # Choose automata
        print('Stage 1 - Choose an automata \n')
        user = '00'
        automata = []
        for i in range (44):
            if i+1 < 10:
                automata.append('0'+str(i+1))
            else :
                automata.append(str(i+1))

        while (user not in automata):

            user = input("Please choose an automata, 44 automatas are available (enter '01' for automata 1):\n")

        print( 'you choose automata',user,':\n')

        filename = 'automata_files/int2-U-'+user+'.txt'
        
        A, nb_state, nb_i, initial, nb_t, terminal, transition = read_automata(filename)

        #display automata
        display(filename)

        print('\n\n')

        #display information on the automata
        print('Stage 2 - Automata informations\n')

        print('The automata is :\n')

        if standardize(filename):
            print("- Standard")

            #append content of automata in standard file
            with open(filename,'r') as f, open('Work_files/Standardized.txt','w') as f1 :
                for line in f :
                    f1.write(line)
            f.close(),f1.close()

        else:
            print("- Not Standard")
        if deterministic(filename):
            if complete_deterministic(filename):
                print("- Deterministic and Complete")
                # append content of automata in deterministic & complete file
                with open(filename, 'r') as f, open('Work_files/Complete.txt','w') as f1, open('Work_files/deterministic.txt','w') as f2:
                    for line in f:
                        f1.write(line)
                        f2.write(line)
                f.close(), f1.close(),f2.close()
            else:
                print("- Deterministic")
                # append content of automata in deterministic file
                with open(filename, 'r') as f, open('Work_files/deterministic.txt','w') as f1:
                    for line in f:
                        f1.write(line)
                f.close(), f1.close()

            for i in range (nb_state):
                n_s.append(str(i))


            for j in range(len(n_s)):
                row = []
                for i in range(int(A)):
                    row.append('')
                for i in range (transition[j][0]):
                    x = transition[j][i+1].split(',')
                    row[ord(x[1])-97] =row[ord(x[1])-97] + str(x[2])
                column.append(row)

        else:
            print("- Not Deterministic")

        i = 3

        #Standardize it on demande

        if standardize(filename) == 0:
            print('\n\n')
            print('Stage ', i, ' - Standardization')
            i = i + 1
            while (user != 'y' and user != 'n'):
                user = input("Do you want to standardize the automata ? (y/n)\n")
            if user == 'y':
                standardization(filename)
                display('Work_files/Standardized.txt')

            user = ''
            while (user != 'c'):
                user = input("enter 'c' to continue\n")

        user = ''

        #Make it deterministic and complete

        print('\n\n')
        print('Stage ', i, ' - Determinization & Complete')
        i = i + 1
        if deterministic(filename) == 0:
            user = ''
            while (user != 'c'):
                user = input("enter 'c' to continue\n")

            print("Once determinized you obtain :")
            n_s, column = determiniation(filename)
            display_2(n_s, column, 'Work_files/deterministic.txt')

            if complete_deterministic('Work_files/deterministic.txt'):
                print("And it's even complete !")
                n_s, column = complete('Work_files/deterministic.txt', n_s, column)

        if complete_deterministic('Work_files/deterministic.txt')!= 1 :
            user = ''
            while (user != 'c'):
                user = input("enter 'c' to continue\n")

            print("Once Complete you obtain :")
            n_s, column = complete('Work_files/deterministic.txt',n_s, column)
            display_2(n_s, column, 'Work_files/Complete.txt')
        if complete_deterministic(filename):
            print("check !\n")
         #Minimization
        print('Stage ', i, ' - Minimization')
        i = i + 1
        user = ''
        while (user != 'c'):
            user = input("enter 'c' to continue\n")

        n_s, column = minimizing("Work_files/Complete.txt", n_s, column)

        #Complementary
        print('Stage ', i, ' - Complementary')
        i = i + 1
        user = ''
        while (user != 'c'):
            user = input("enter 'c' to continue\n")

        complementaire('Work_files/Minimized.txt')
        display_2(n_s, column, 'Work_files/Completementaire.txt')

        print('Stage ', i, ' - Word Recognition')
        i = i + 1
        user = ''
        while (user != 'y' and user != 'n'):
            print('\n\n')
            user = input("Do you want to test word recognition of the automata ?(y/n)\n")
        if user == 'y':

            loop = 1
            while loop:
                user = ''

                while (user != '1' and user != '2'):
                    user = input(" Casual automata(1) or Complementaire automata(2) ?\n")

                if user == '1':
                    word_recognition('Work_files/Minimized.txt')
                if user == '2':
                    word_recognition('Work_files/Completementaire.txt')
                user = ''

                while (user != 'y' and user != 'n'):
                    print('\n')
                    user = input(" Try another word ?(y/n) \n")
                if user == 'n':
                    loop = 0
        user = ''
        while (user != 'y' and user != 'n'):
            print('\n\n')
            user = input(" Want to check another automata ?(y/n) \n")
        if user == 'n':
            M_loop = 0

        print("\n\nNext automata !")

    print('Thank You to have Participated !')
    print('Good Bye !')