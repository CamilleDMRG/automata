# Function to read all the automata file
import copy
def read_automata(filename):
    with open(filename, "r") as f:
        A = f.readline() #A is the alphabet
        nb_state = int(f.readline()) #the number of states
        nb_i = int(f.readline()) #number inital states
        initial =f.readline().split() #initial states
        nb_t = int(f.readline()) #number of terminal states
        if (nb_t != 0):
            terminal =f.readline().split()#terminal states
        else:
            terminal = []
        transition = [] #transition table first entry each row = nb transition of the state
        for i in range (nb_state):
            row = []
            row.append(int(f.readline()))
            for j in range (row[0]):
                line = f.readline().split('\n')
                row.append(line[0])
            transition.append(row)
    f.close()
    return A, nb_state, nb_i, initial, nb_t, terminal, transition

#display
def display(filename):
    A, nb_state, nb_i, initial, nb_t, terminal, transition = read_automata(filename)
    nb = 19
    #line 1 upper edge
    print('     ',end='')
    print('┏', end='')
    for i in range(int((nb_state/10)+5)):
        print('━', end='')
    print('┳', end='')
    for i in range (int(A)-1):
        for i in range(nb):
            print('━', end='')
        print('┳', end='')
    for i in range(nb):
        print('━', end='')
    print('┓')

    #line 2 alphabet
    print('     ', end='')
    print('┃',end='')
    for i in range(int((nb_state / 10) + 5)):
        print(' ', end='')
    print('┃', end='')
    for i in range (int(A)-1):
        for j in range((nb-1) //2 ):
            print(' ', end='')
        print(chr(i+97), end='')
        for j in range((nb-1) //2 ):
            print(' ', end='')
        print('┃', end='')
    for i in range((nb-1) //2 ):
        print(' ', end='')
    print(chr(int(A) + 96), end='')
    for i in range((nb-1) //2 ):
        print(' ', end='')
    print('┃')



    # loop state and transition
    for i in range (nb_state):
        print('     ', end='')
        print('┣', end='')
        for b in range(int((nb_state / 10) + 5)):
            print('━', end='')
        print('╋', end='')
        for b in range(int(A) - 1):
            for l in range(nb):
                print('━', end='')
            print('╋', end='')
        for b in range(nb):
            print('━', end='')
        print('┫')

        if str(i) in list(initial) :
            if str(i) in list(terminal) :
                print(' <-> ',end='')
            else :
                print('  -> ', end='')
        elif str(i) in list(terminal) :
            print('  <- ', end='')
        else :
            print('     ', end='')

        print('┃', end='')
        for j in range(2):
            print(' ', end='')
        if(nb_state>=10):
            if(i<10):
                print(i,'',end='')
            else:
                print(i,end='')
        else:
            print(i, end='')
        for j in range(2):
            print(' ', end='')
        if(nb_state>=20):
            print(' ', end='')
        print('┃', end='')

        for k in range (int(A)):
            count = 0
            for j in range (transition[i][0]):
                x = transition[i][j+1].split(',')
                if x[1] == chr(k+97):
                    if(int(x[2])>=10):
                        count = count + 2
                    else:
                        count = count + 1
            if count == 0 :
                for j in range ((nb-1)// 2):
                    print(' ', end='')
                print('X', end='')
                for j in range ((nb-1)// 2):
                    print(' ', end='')
                print('┃', end='')
            else :
                count = count + (count-1)
                c = (nb - count )//2
                p = 0
                if ((c * 2) + count!= nb):
                    p = nb - ((c * 2) + count)
                for j in range(c+p):
                    print(' ', end='')
                q=0
                qd = 0
                for j in range (transition[i][0]):
                    x = transition[i][j + 1].split(',')
                    if x[1] == chr(k + 97):
                        if q == 0:
                            print('' + x[2], end='')
                            q=1
                        else:
                            print('' + ',' + x[2] , end='')
                        if(int(x[2])>=10):
                            qd=+1


                for j in range(c+qd):
                    print(' ', end='')
                print('┃', end='')
        print('')
    # last line
    print('     ', end='')
    print('┗', end='')
    for i in range(int((nb_state / 10) + 5)):
        print('━', end='')
    print('┻', end='')
    for i in range(int(A) - 1):
        for i in range(nb):
            print('━', end='')
        print('┻', end='')
    for i in range(nb):
        print('━', end='')
    print('┛')

    return

#aestatic display
def display_2(n_s, column, file):
    A, nb_state, nb_i, initial, nb_t, terminal, transition = read_automata(file)

    max = 0
    for i in range (len(n_s)):
        if len(n_s[i]) > max :
            max = len(n_s[i])
    nb = 19

    # line 1 upper edge
    print('     ', end='')
    print('┏', end='')
    for i in range(int(max + 4)):
        print('━', end='')
    print('┳', end='')
    for i in range(int(A) - 1):
        for i in range(nb):
            print('━', end='')
        print('┳', end='')
    for i in range(nb):
        print('━', end='')
    print('┓')

    # line 2 alphabet
    print('     ', end='')
    print('┃', end='')
    for i in range(int(max + 4)):
        print(' ', end='')
    print('┃', end='')
    for i in range(int(A) - 1):
        for j in range((nb - 1) // 2):
            print(' ', end='')
        print(chr(i + 97), end='')
        for j in range((nb - 1) // 2):
            print(' ', end='')
        print('┃', end='')
    for i in range((nb - 1) // 2):
        print(' ', end='')
    print(chr(int(A) + 96), end='')
    for i in range((nb - 1) // 2):
        print(' ', end='')
    print('┃')

    # loop state and transition
    for i in range(len(n_s)):
        print('     ', end='')
        print('┣', end='')
        for b in range(int(max + 4)):
            print('━', end='')
        print('╋', end='')
        for b in range(int(A) - 1):
            for l in range(nb):
                print('━', end='')
            print('╋', end='')
        for b in range(nb):
            print('━', end='')
        print('┫')

        if str(i) in list(initial):
            if str(i) in list(terminal):
                print(' <-> ', end='')
            else:
                print('  -> ', end='')
        elif str(i) in list(terminal):
            print('  <- ', end='')
        else:
            print('     ', end='')

        print('┃', end='')
        h = 0
        if max > len(n_s[i]):
            h = ((max + 4) -( len(n_s[i])) )%2

        for j in range((((max + 4) -( len(n_s[i])))//2) + h):
            print(' ', end='')
        print(n_s[i], end='')
        for j in range((((max + 4) -( len(n_s[i])))//2)):
            print(' ', end='')
        print('┃', end='')

        for k in range(int(A)):

            count = len(column[i][k])

            if count == 0:
                for j in range((nb - 1) // 2):
                    print(' ', end='')
                print('X', end='')
                for j in range((nb - 1) // 2):
                    print(' ', end='')
                print('┃', end='')

            else :
                c = (nb - count) // 2
                p = 0
                if ((c * 2) + count != nb):
                    p = nb - ((c * 2) + count)
                for j in range(c + p):
                    print(' ', end='')
                print('' + column[i][k], end='')
                for j in range(c):
                    print(' ', end='')
                print('┃', end='')
        print('')
    # last line
    print('     ', end='')
    print('┗', end='')
    for i in range(int(max + 4)):
        print('━', end='')
    print('┻', end='')
    for i in range(int(A) - 1):
        for i in range(nb):
            print('━', end='')
        print('┻', end='')
    for i in range(nb):
        print('━', end='')
    print('┛')

    return

# return 0 if automata not standardize otherwise return 1
def standardize(F):
    A, nb_state, nb_i, initial, nb_t, terminal, transition = read_automata(F)
    if nb_i != 1:
        #print("the automata isn't standardize")
        return 0
    else :
        s = 1 # equal 1 if it standardize
        for i in range(nb_state):
            for j in range(int(transition[i][0])):
                w = transition[i][j+1].split(',')
                if w[2] == initial[0]:
                    s = 0
                    break

        if s :
            #print("the automata is standardize")
            return 1
        else :
            #print("the automata isn't standardize")
            return 0

# standardize the automata in file Standardized.txt
def standardization(filename):
    A, nb_state, nb_i, initial, nb_t, terminal, transition = read_automata(filename)
    f = open('Work_files/Standardized.txt', 'w')
    #rewrite everything while changing nb_i =1 and initial as the new initial state
    f.write(A)
    f.write(str(nb_state+1)+"\n")
    f.write("1"+"\n")
    f.write(str(nb_state)+"\n")
    #recognize empty word ?
    e = 0
    for i in range (nb_i):
        if initial[i] in terminal:
            e = 1
    if (e): #if empty word recognize new initial state is terminal
        f.write(str(nb_t+1)+'\n')
        for h in range (nb_t):
            f.write(str(terminal[h]) + ' ')
        f.write(str(nb_state))
        f.write('\n')
    if (e==0):#else
        f.write(str(nb_t) + '\n')
        for h in range(nb_t-1):
            f.write(str(terminal[h]) + ' ')
        f.write(str(terminal[nb_t-1]))
        f.write('\n')

    #we rewrite all the transition
    for i in range (nb_state) :
        f.write(str(transition[i][0]) + '\n')
        for j in range (transition[i][0]) :
            f.write(str(transition[i][j+1]) + '\n')
    #add the transition of the new initial state


    new_initial = []
    for i in range(nb_i):
        for j in range(transition[int(initial[i])][0]):
            x = transition[int(initial[i])][j + 1].split(',')
            p = str(nb_state)+','+x[1]+','+x[2]
            if ( p not in new_initial):
                new_initial.append(p)

    f.write(str(len(new_initial)) + '\n')
    for i in range (len(new_initial)):
        f.write(new_initial[i] + '\n')

    f.close()
    return

# return 0 if automata not deterministic otherwise return 1
def deterministic(filename):
    A, nb_state, nb_i, initial, nb_t, terminal, transition = read_automata(filename)
    if nb_i != 1:
        #print("the automata isn't deterministic")
        return 0
    else :
        d = 1
        for i in range (nb_state):
            a = []
            for j in range (int(A)):
                a.append(0)
            for j in range(transition[i][0]):
                x = transition[i][j + 1].split(',')
                a[ord(x[1])-97] +=1
                if(a[ord(x[1])-97] > 1):
                    d = 0
                    break
        if d :
            #print("the automata is deterministic")
            return 1
        else :
            #print("the automata isn't deterministic")
            return 0

# determinise the automata in file deterministic.txt
def determiniation(filename):
    A, nb_state, nb_i, initial, nb_t, terminal, transition = read_automata(filename)
    column = []
    n_s = []
    x1 =''
    for i in range(nb_i):
        if i == 0 :
            x1 = x1 + initial[i]
        else:
            x1 = x1+',' + initial[i]
    ns = 0
    end = 0
    n_s.append(x1) #initial state become first new state

    while len(n_s) != len(column):

        row1= []
        x = ''

        for j in range(int(A)):
            row1.append('')
        for i in range(len(n_s[ns].split(','))):
            split = n_s[ns].split(',')
            for j in range(transition[int(split[i])][0]):
                x = transition[int(split[i])][j+1].split(',')
                if(x[2] not in row1[ord(x[1])-97].split(',')):
                    if len(row1[ord(x[1])-97]) == 0 :
                        row1[ord(x[1]) - 97] = row1[ord(x[1]) - 97] + x[2]
                    else:
                        row1[ord(x[1]) - 97] = row1[ord(x[1]) - 97]+ ',' + x[2]

        for k in range(int(A)):
            if row1[k]!='':
                present = 0
                for i in range(len(n_s)):
                    nb = 0
                    for m in range (len(row1[k].split(','))):
                        se=row1[k].split(',')
                        if se[m] in n_s[i].split(','):
                            nb = nb +1
                    if ( nb == len(row1[k].split(',')) and len(n_s[i].split(','))== len(row1[k].split(','))):
                        present = 1
                        row1[k]=n_s[i]

                if (present==0):
                    n_s.append(row1[k])
        column.append(row1)
        ns = ns + 1

#we rewrite everything in the file
    t = []
    f = open('Work_files/deterministic.txt', 'w')
    f.write(A)
    f.write(str(len(n_s)) +'\n')
    f.write('1'+'\n')
    f.write('0'+'\n')
    for j in range (len(n_s)):
        tn = 0
        for i in range(nb_t):
            if terminal[i] in n_s[j].split(','):
                tn=1
        if tn :
            t.append(j)

    f.write(str(len(t))+'\n')
    for i in range(len(t)):
        f.write(str(t[i])+' ')

    f.write('\n')

    for i in range (len(n_s)):
        count = 0
        for j in range (len(column[i])):
            if column[i][j] != '' :
                count=count+1
        f.write(str(count)+'\n')
        for j in range (len(column[i])):
            if column[i][j] != '' :
                f.write(str(i)+','+str(chr(j+97))+','+str(n_s.index(column[i][j]))+'\n')

    f.close()
    return n_s,column

# complet the automata in the file Complete.txt
def complete(filename,n_s , column):
    A, nb_state, nb_i, initial, nb_t, terminal, transition = read_automata(filename)
    check = 0
    for i in range (nb_state):
        if (transition[i][0] != int(A)):
            check =1

    if (check != 0):
        C = 0
        for i in range (len(transition)):
            count = ''
            for j in range (transition[i][0]):
                x = transition[i][j+1].split(',')
                count = count +x[1]
            w = transition[i][0]
            for j in range (int(A)):
                if chr(j+97) not in list(count):
                    C = C + 1
                    w = w + 1
                    transition[i].append(str(i) +','+ str(chr(j + 97)) +','+ str(nb_state))
            transition[i][0] = w
        f = open('Work_files/Complete.txt', 'w')
        # rewrite everything
        f.write(A)
        if C != 0 :
            f.write(str(nb_state + 1) + "\n")
        else :
            f.write(str(nb_state) + "\n")
        f.write(str(nb_i)+'\n')
        for i in range (nb_i) :
            f.write(str(initial[i])+' ')
        f.write('\n')
        f.write(str(nb_t) + '\n')
        for i in range (nb_t) :
            f.write(str(terminal[i])+' ')
        if ( nb_t != 0):
            f.write('\n')
        for i in range (nb_state) :
            f.write(str(transition[i][0]) + '\n')
            for j in range (transition[i][0]) :
                f.write(str(transition[i][j+1]) + '\n')

        if C != 0 :
            f.write(A)
            for i in range (int(A)):
                f.write(str(nb_state)+','+str(chr(i+97))+','+str(nb_state)+'\n')
        f.close()

        n_s.append('P')
        row = []
        for i in range(int(A)):
            row.append('P')
        column.append(row)

        for i in range(int(A)):
            for j in range(len(column)):
                if column[j][i] == '':
                    column[j][i] = 'P'
    else :
        # append content of automata in deterministic & complete file
        with open('Work_files/deterministic.txt', 'r') as f, open('Work_files/Complete.txt', 'w') as f1:
            for line in f:
                f1.write(line)

    return  n_s, column

# return 0 if automata not deterministic & complete otherwise return 1
def complete_deterministic(filename):
    A, nb_state, nb_i, initial, nb_t, terminal, transition = read_automata(filename)
    C = 1
    for i in range (nb_state):
        if int(A) > transition[i][0] :
            C = 0
            return 0

    if C :
        return 1

#give Complementair of the automata in file Complementaire.txt
def complementaire(filename):
    A, nb_state, nb_i, initial, nb_t, terminal, transition = read_automata(filename)
    f = open('Work_files/Completementaire.txt', 'w')
    f.write(A)
    f.write(str(nb_state)+'\n')
    f.write(str(nb_i)+'\n')
    for i in range(nb_i):
        f.write(str(initial[i]) + ' ')
    f.write('\n')
    f.write(str(nb_state - nb_t)+'\n')
    if nb_state - nb_t != 0 :
        for i in range (nb_state):
            if str(i) not in terminal :
                f.write(str(i)+' ')
        f.write('\n')
    for i in range (nb_state) :
        f.write(str(transition[i][0]) + '\n')
        for j in range (transition[i][0]) :
            f.write(str(transition[i][j+1]) + '\n')
    f.close()
    return

#check if the word belong in the automata
def word_recognition(filename):
    A, nb_state, nb_i, initial, nb_t, terminal, transition = read_automata(filename)
    user = input('Please enter a word to see if the automata recognize it :\n')
    print('you entered : ',list(user))

    x = list(initial)
    c_p = x[0]  # current position of checking, we start at the initial state (so here we only test on deterministic)

    L = ''
    for i in range(int(A)):
        L = L + str(chr(i + 97))
    print('alphabet : ', list(L))

    if (user == '' and c_p in list(terminal) ):
        print('The automate indeed recognize the empty word :3')
        return
    else:

        for i in range (len(user)):
            if user[i] not in L :
                print('The word isn\'t recognize by this automata it\'s own character(s) not belonging to the automata language !')
                return

        # we sure to have in the word character from our language now we check if the word belong to the automata
        for i in range(len(user)):
            a = 0  # a = 1 if the letter take a path
            for j in range(transition[int(c_p)][0]):
                w = transition[int(c_p)][j + 1].split(',')
                if user[i] == w[1]:
                    c_p = w[2]
                    a = 1
                    break

            if a == 0:
                print('the automata dont recognize the word !')
                return

        if (c_p in terminal):
            print('the automata recognize the word :3')
            return
        else:
            print('the automata dont recognize the word :,(')
            return

#minimize the automat
def minimizing(filename, n_s, column):
    A, nb_state, nb_i, initial, nb_t, terminal, transition = read_automata('Work_files/Complete.txt')

    print('nota bene : the automata ')
    display_2(n_s,column,'Work_files/Complete.txt')
    matrix = copy.deepcopy(column)
    #stage 1 NT and T
    print("______________________________________________")
    print('θ0 = { NT , T }, where :')

    nt = []
    for i in range(nb_state):
        if str(i) not in terminal:
            nt.append(i)

    print('NT={', end='')
    for i in range(len(nt)):
        if (i == 0):
            print(n_s[int(nt[i])], end='')
        else:
            print(' ;', n_s[int(nt[i])], end='')
    print('}')


    print('T={',end='')
    for i in range (nb_t) :
        if(i==0):
            print(n_s[int(terminal[i])],end='')
        else:
            print(' ;',n_s[int(terminal[i])],end='')
    print('}')


    for i in range (len(matrix)) :
        for j in range (int(A)) :
            if str(n_s.index(matrix[i][j])) in terminal :
                matrix[i][j] = 'T'
            else :
                matrix[i][j] = 'NT'

    display_2(n_s, matrix, 'Work_files/Complete.txt')



    T = copy.deepcopy(terminal)
    NT = copy.deepcopy(nt)
    nb = 0
    NT1 = copy.deepcopy(NT)
    T1 = copy.deepcopy(T)
    T = []
    NT = []
    row = []

    if nb_t != 0 :
        row.append(terminal[0])
        T.append(row)

        for i in range(1, nb_t):
            find = 0
            row = []
            for j in range(len(T)):
                if matrix[int(T[j][0])] == matrix[int(terminal[i])]:
                    T[j].append(terminal[i])
                    find = 1
                    break

            if (find == 0):
                row.append(terminal[i])
                T.append(row)

    row = []

    if len(nt)!= 0 :
        row.append(str(nt[0]))
        NT.append(row)

        for i in range(1, len(nt)):
            find = 0
            row = []
            for j in range(len(NT)):
                if matrix[int(NT[j][0])] == matrix[int(nt[i])]:
                    NT[j].append(str(nt[i]))
                    find = 1
                    break

            if (find == 0):
                row.append(str(nt[i]))
                NT.append(row)


    while T != T1 or NT != NT1 :
        nb=nb+1
        print("______________________________________________")
        print('θ'+str(nb),'= { ',end='')
        groupe = 0
        for i in range (len(NT)):
            if groupe == 0 :
                print(chr(groupe+65),end='')
                groupe=groupe+1
            else :
                print(',',chr(groupe + 65), end='')
                groupe = groupe + 1

        for i in range (len(T)):
            if groupe == 0 :
                print(chr(groupe+65),end='')
                groupe = groupe+1
            else :
                print(',',chr(groupe+ 65), end='')
                groupe = groupe + 1

        print('}, where :')
        groupe = 0
        for k in range(len(NT)):
            print(chr(groupe+65),'={', end='')
            groupe = groupe+1
            for i in range(len(NT[k])):
                if (i == 0):
                    print(n_s[int(NT[k][i])], end='')
                else:
                    print(' ;', n_s[int(NT[k][i])], end='')
            print('}')

        for k in range(len(T)):
            print(chr(groupe+65),'={', end='')
            groupe = groupe+1
            for i in range(len(T[k])):
                if (i == 0):
                    print(n_s[int(T[k][i])], end='')
                else:
                    print(' ;', n_s[int(T[k][i])], end='')
            print('}')

        for i in range (len(matrix)) :
            for j in range (int(A)) :
                groupe = 0
                for k in range(len(NT)):
                    for m in range(len(NT[k])):
                        if str(n_s.index(column[i][j])) in NT[k] :
                            matrix[i][j] = chr(groupe+65)
                            break
                    groupe=groupe+1
                for k in range(len(T)):
                    for m in range(len(T[k])):
                        if str(n_s.index(column[i][j])) in T[k]:
                            matrix[i][j] = chr(groupe+65)
                            break
                    groupe=groupe+1
        display_2(n_s, matrix, 'Work_files/Complete.txt')

        NT1 = copy.deepcopy(NT)
        T1 = copy.deepcopy(T)
        T = []
        NT = []
        row = []

        if nb_t != 0 :
            row.append(terminal[0])
            T.append(row)

            for i in range(1, nb_t):
                find = 0
                row = []
                for j in range(len(T)):
                    if matrix[int(T[j][0])] == matrix[int(terminal[i])]:
                        T[j].append(terminal[i])
                        find = 1
                        break

                if (find == 0):
                    row.append(terminal[i])
                    T.append(row)

        row = []

        if len(nt)!= 0 :
            row.append(str(nt[0]))
            NT.append(row)

            for i in range(1, len(nt)):
                find = 0
                row = []
                for j in range(len(NT)):
                    if matrix[int(NT[j][0])] == matrix[int(nt[i])]:
                        NT[j].append(str(nt[i]))
                        find = 1
                        break

                if (find == 0):
                    row.append(str(nt[i]))
                    NT.append(row)


    #conclusion

    f = open('Work_files/Minimized.txt', 'w')
    f.write(A)

    ninit = []
    print("______________________________________________")
    print('We can\' t partition it more')
    print('So θfinal = θ'+str(nb))
    print('the states are ',end='')
    groupe = 0
    for i in range(len(NT)):
        if groupe == 0:
            print(chr(groupe + 65), end='')
            groupe = groupe + 1
        else:
            print(',', chr(groupe + 65), end='')
            groupe = groupe + 1

    for i in range(len(T)):
        if groupe == 0:
            print(chr(groupe + 65), end='')
            groupe = groupe + 1
        else:
            print(',', chr(groupe + 65), end='')
            groupe = groupe + 1

    same = 0
    f.write(str(groupe)+'\n')
    if (groupe == nb_state):
        same = 1


    print('\n The initial state(s) are ',end='')

    groupe = 0
    mlp = 0
    for i in range(len(NT)):
        for j in range(nb_i):
            if initial[j] in list(NT[i]):
                ninit.append(groupe)
                if mlp ==0 :
                    print(chr(groupe + 65), end='')

                    mlp = 1
                else:
                    print(',',chr(groupe + 65), end='')
        groupe = groupe + 1

    for i in range(len(T)):
        for j in range(nb_i):
            if initial[j] in list(T[i]):
                ninit.append(groupe)
                if mlp == 0:
                    print(chr(groupe + 65), end='')
                    mlp = 1
                else:
                    print(',', chr(groupe + 65), end='')
        groupe = groupe + 1

    f.write(str(len(ninit))+'\n')
    for i in range (len(ninit)):
        f.write(str(ninit[i])+' ')
    f.write('\n')

    print('\n The terminal state(s) are ', end='')

    groupe = 0
    mlp = 0
    for i in range(len(NT)):
        groupe = groupe + 1

    if nb_t != 0 :
        f.write(str(len(T))+'\n')
        for i in range(len(T)):
            if mlp == 0:
                print(chr(groupe + 65), end='')
                mlp = 1
            else:
                print(',', chr(groupe + 65), end='')
            f.write(str(groupe)+' ')
            groupe = groupe + 1

        f.write('\n')
        print('\n')
    else:
        print("none.")
        f.write(str(0) + '\n')
    groupe = 0

    for i in range(len(NT)):

        f.write(A)
        for j in range (int(A)):
            f.write(str(groupe)+','+str(chr(j+97))+','+str(ord(matrix[int(NT[i][0])][j])-65)+'\n')
        groupe=groupe+1

    for i in range(len(T)):
        f.write(A)
        for j in range (int(A)):
            f.write(str(groupe)+','+str(chr(j+97))+','+str(ord(matrix[int(T[i][0])][j])-65)+'\n')
        groupe=groupe+1
    f.close()
    if ( same ):
        print("We notice that the automata was already minimized !")
        f.close()
        with open(filename, 'r') as f, open('Work_files/Minimized.txt', 'w') as f1:
            for line in f:
                f1.write(line)
        f.close()

    else :
        n_s =[]
        for i in range (groupe):
            n_s.append(chr(i+65))
        row = []
        column=[]
        for i in range(len(NT)):
            row = []
            for j in range (int(A)):
                row.append(str(matrix[int(NT[i][0])][j]))
            column.append(row)

        for i in range(len(T)):
            row = []
            for j in range (int(A)):
                row.append(str(matrix[int(T[i][0])][j]))
            column.append(row)

    display_2(n_s, column, 'Work_files/Minimized.txt')

    return n_s , column
