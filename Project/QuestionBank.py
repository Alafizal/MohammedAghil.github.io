import pickle
from Mymodules import *
import datetime

tn = ''
def inputtn(tn):
    co = inpany('Created On: ', '')
    print()
    cb = inpany('Created by: ', '')
    print()
    tp = inpany('Topic     : ', '')
    print()
    return [tn, co, cb, tp, 0]

def printtn(rc):
    tn, co, cb, tp, nq = rc               
    print('Paper no.   :', tn)
    print('Created on  :', co)
    print('Created by  :', cb)
    print('Topic       :', tp)
    print('No.Questions:', nq)
    print('\n')

def find_next_tn():
    tn = 0
    with open('topic.dat', 'ab+') as fl:
        fl.seek(0)
        while True:
            try:
                tn, co, cb, tp, nq = pickle.load(fl)
            except EOFError:
                break
    return tn+1

def find_next_qn(no):
    qn = 0
    with open('questions.dat', 'ab+') as fl:
        fl.seek(0)
        while True:
            try:
                tn, qn, qe, o1, o2, o3, o4, aw  = pickle.load(fl)
            except EOFError:
                break
    return qn+1

def searchtn(op = ''):
    global tn
    tn = inpany('Test Paper No.: ', 0)
    print()
    with open('topic.dat', 'rb') as fl:
        while True:
            try:
                tt, co, cb, tp, nq = pickle.load(fl)
                if tn == tt:
                    return 
            except EOFError:
                break
        if op == '':
            print('Invalid Test Paper Number !\n')
    return False

def update_qpaper_nq(no):
    recs = []
    with open('topic.dat', 'rb') as fl:
        while True:
            try:
                tn, co, cb, tp, nq = pickle.load(fl)
                if tn == no:
                    nq += 1
                recs.append([tn, co, cb, tp, nq])
            except EOFError:
                break
    with open('topic.dat', 'wb') as fl:
        for rec in recs:
            pickle.dump(rec, fl)
    
def create_topic():
    tn = find_next_tn()
    rc = searchtn('a')
    if not rc:
        rc = inputtn(tn)
        print()
        if input('Save(y/n): ').lower() == 'y':
            with open('topic.dat', 'ab') as fl:
                pickle.dump(rc, fl)
        
def edit_topic():
    print('EDIT TOPIC\n')
    rc = searchtn()
    print()
    if rc:
        flag = False
        with open('topic.dat', 'rb') as fl:
            rs = []
            while True:
                try:
                    tn, co, cb, tp, nq = pickle.load(fl)
                    if tt == tn:
                        flag = True
                        printtn(rc)
                        print('Edit Info...')
                        cb = inpany('Created by  :', '')
                        tp = inpany('Topic       :', '')
                    rs.append([tn, co, cb, tp, nq])                         
                except EOFError:
                    break
                    
        if flag:
            print()
            if input('Confirm Edit(y/n): ').lower() == 'y':
                fl = open('topic.dat', 'wb')
                for rc in rs:
                    pickle.dump(rc, fl)
                fl.close()
                print('Edited !')
            else:
                print('Editing Cancelled !')            

def delete_topic():
    print('REMOVE TOPIC\n')

    rc = searchtn()
    print()
    if rc:
        flag = False
        with open('topic.dat', 'rb') as fl:
            rs = []
            while True:
                try:
                    rc = pickle.load(fl)
                    if tn == rc[0]:
                        flag = True
                        print('Current Info...')
                        printtn(rc)
                    else:
                        rs.append([tn, co, cb, tp, nq])                    
                except EOFError:
                    break
        if flag:
            print()
            if input('Confirm Remove(y/n): ').lower() == 'y':
                with open('topic.dat', 'wb') as fl:
                    for rc in rs: 
                        pickle.dump(rc, fl)
                    print('Removed!')
            else:
                print('Removing Cancelled !')

def list_topic():
    with open('topic.dat', 'ab+') as fl:
        fl.seek(0)
        c = 0
        while True:
            try:
                tn, co, cb, tp, nq = pickle.load(fl)
                if c == 0:
                    print('%-10s %-15s %-20s %-20s %-10s' %
                          ('Paper no.', 'Created on', 'Created by', 'Topic', 'No.Questions'))
                print('%-10s %-15s %-20s %-20s %-10s' %
                      (tn, co, cb, tp, nq))
                c += 1                
            except EOFError:
                break
            
def create_qbank():
    tn = inpany('Test Paper No.:', 0)
    qn = find_next_qn(tn)
    while True:
        print('Question No: ', qn, '\n')
        qe = inpany('Question : ', '')
        print()
        o1 = inpany('Option a): ', '')
        o2 = inpany('Option b): ', '')
        o3 = inpany('Option c): ', '')
        o4 = inpany('Option d): ', '')
        print()
        aw = inpany('Answer(a/b/c/d): ', '').upper()
        print()
        if input('Save(y/n): ').lower() == 'y':
            update_qpaper_nq(tn)
            with open('questions.dat', 'ab') as fl:
                pickle.dump([tn, qn, qe, o1, o2, o3, o4, aw], fl)
            print('\nSaved !\n')
            qn += 1
            if input('More Questions(y/n): ').upper() != 'Y':
                break
        else:
            print('\nCancelled !')

def Edit_Question():
    print('EDIT QUESTION\n')

    qq = inpany('Question No: ', '')
    print()

    with open('questions.dat', 'rb') as fl:
        flag = False
        rs = []
        while True:
            try:
                tn, qn, qe, o1, o2, o3, o4, aw = pickle.load(fl)               
                if qq == tn:
                    flag = True
                    print('Current Info...')
                    print('Question No:', qn)
                    print('Question   :', qe)
                    print('Option a)  :', o1)
                    print('Option b)  :', o2)
                    print('Option c)  :', o3)
                    print('Option d)  :', o4)
                    print('Answer(a/b/c/d):', aw)
                    print('\n')
                    print('Edit Info...')
                    qe = inpany('Question  :', '')
                    o1 = inpany('Option a): ', '')
                    o2 = inpany('Option b): ', '')
                    o3 = inpany('Option c): ', '')
                    o4 = inpany('Option d): ', '')
                    aw = inpany('Answer(a/b/c/d):', '')
                rs.append([tn, qn, qe, o1, o2, o3, o4, aw])                         
            except EOFError:
                break
                    
    if flag:
        print()
        if input('Confirm Edit(y/n): ').lower() == 'y':
            fl = open('questions.dat', 'wb')
            for rc in rs:
                pickle.dump(rc, fl)
            fl.close()
            print('Edited !')
        else:
            print('Editing Cancelled !')            
    else:
        print('Invalid Question Number !')
    
def delete_question():
    print('REMOVE QUESTION\n')

    qb = inpany('Question No: ', '')
    print()
    
    with open('questions.dat', 'rb') as fl:
        flag = False
        rs = []
        while True:
            try:
                tn, qn, qe, o1, o2, o3, o4, aw = pickle.load(fl)               
                if qb == qn:
                    flag = True
                    print('Current Info...')
                    print('Question No:', qn)
                    print('Question   :', qe)
                    print('Option a)  :', o1)
                    print('Option b)  :', o2)
                    print('Option c)  :', o3)
                    print('Option d)  :', o4)
                    print('Answer(a/b/c/d):', aw)
                else:
                    rs.append([tn, qn, qe, o1, o2, o3, o4, aw])                    
            except EOFError:
                break
    if flag:
        print()
        if input('Confirm Remove(y/n): ').lower() == 'y':
            with open('questions.dat', 'wb') as fl:
                for rc in rs:
                   pickle.dump(rc, fl)
            print('Removed!')
        else:
            print('Removing Cancelled !')
            
    else:
        print('Invalid Question Number !')

def List_question():
    with open('questions.dat', 'ab+') as fl:
        fl.seek(0)
        c = 0
        while True:
            try:
                tn, qn, qe, o1, o2, o3, o4, aw = pickle.load(fl)
                if c == 0:
                    print('Question No.:', qn, '\n')
                    print('Question :', qe, '\n')
                    print('%-15s %-15s %-15s %-15s %-15s' %
                          ('Option a)', 'Option b)', 'Option c)', 'Option d)', 'Answer(a/b/c/d)'))
                print('%-15s %-15s %-15s %-15s %-15s' %
                      (o1, o2, o3, o4, aw))
                c += 1                
            except EOFError:
                break
    
qm = '''QUESTION BANK MENU

1. Create Topic
2. Edit Topic
3. Delete Topic
4. List Topic

5. Create Question
6. Edit Question
7. Delete Question
8. List Question

9. Return to Main Menu

Enter Choice(1-9): '''

def question_menu():
    while True:
        op = inpany(qm, '')
        print()
        if op == '1':
            create_topic()
        elif op == '2':
            edit_topic()
        elif op == '3':
            delete_topic()
        elif op == '4':
            list_topic()
        elif op == '5':
            create_qbank()
        elif op == '6':
            Edit_Question()
        elif op == '7':
            delete_question()
        elif op == '8':
            List_question()
        elif op == '9':
            break
        else:
            print('Invalid Choice')
        print('\n')
            
    
