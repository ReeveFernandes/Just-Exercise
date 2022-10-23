import csv
from curls import curls
from lunges import lunges
from squats import squats
from push import push
from operator import itemgetter


def TheCode(name, mode):
    main_score_list_curls = []
    main_score_list_push = []
    main_score_list_squats = []
    main_score_list_lunges = []

    file1 = open("score_table_curls.csv", 'r')
    reader = csv.reader(file1)
    for line in reader:
        if len(line) == 0:
            break
        main_score_list_curls = [[line[0], int(line[1])]]

    file1.close()

    file2 = open("score_table_push.csv", 'r')
    reader = csv.reader(file2)
    for line in reader:
        if len(line) == 0:
            break
        main_score_list_push = [[line[0], int(line[1])]]

    file2.close()

    file3 = open("score_table_squats.csv", 'r')
    reader = csv.reader(file3)
    for line in reader:
        if len(line) == 0:
            break
        main_score_list_squats = [[line[0], int(line[1])]]

    file3.close()

    file4 = open("score_table_lunges.csv", 'r')
    reader = csv.reader(file4)
    for line in reader:
        if len(line) == 0:
            break
        main_score_list_lunges = [[line[0], int(line[1])]]

    file4.close()

    while True:

        if mode == 1:
            score_lst = [name, curls()]
            main_score_list_curls.append(score_lst)

            main_score_list_curls = sorted(main_score_list_curls, key=itemgetter(1), reverse=True)

            file1 = open("score_table_curls.csv", 'a')
            with file1:
                writer = csv.writer(file1)

                for row in main_score_list_curls:
                    writer.writerow(row)

            file1.close()

            Leaders = ""
            rank = 1
            for line in main_score_list_curls:
                s = str(rank) + '. ' + line[0] + " " + str(line[1]) + '\n'
                Leaders += s
                rank += 1
                if rank == 6:
                    break

            return Leaders

        if mode == 2:
            score_lst = [name, push()]
            main_score_list_push.append(score_lst)
            main_score_list_push.sort(key=lambda x: x[1], reverse=True)
            file2 = open("score_table_push.csv", 'a')
            with file2:
                writer = csv.writer(file2)

                for row in main_score_list_push:
                    writer.writerow(row)

            file2.close()

            Leaders = ""
            rank = 1
            for line in main_score_list_push:
                s = str(rank) + '. ' + line[0] + " " + str(line[1]) + '\n'
                Leaders += s
                rank += 1
                if rank == 6:
                    break

            return Leaders

        if mode == 3:
            score_lst = [name, squats()]
            main_score_list_squats.append(score_lst)
            main_score_list_squats.sort(key=lambda x: x[1], reverse=True)
            file3 = open("score_table_squats.csv", 'a')
            with file3:
                writer = csv.writer(file3)

                for row in main_score_list_squats:
                    writer.writerow(row)

            file3.close()

            Leaders = ""
            rank = 1
            for line in main_score_list_squats:
                s = str(rank) + '. ' + line[0] + " " + str(line[1]) + '\n'
                Leaders += s
                rank += 1
                if rank == 6:
                    break

            return Leaders


        if mode == 4:
            score_lst = [name, lunges()]
            main_score_list_lunges.append(score_lst)
            main_score_list_lunges.sort(key=lambda x: x[1], reverse=True)
            file4 = open("score_table_lunges.csv", 'a')
            with file4:
                writer = csv.writer(file4)

                for row in main_score_list_lunges:
                    writer.writerow(row)

            file4.close()

            Leaders = ""
            rank = 1
            for line in main_score_list_curls:
                s = str(rank) + '. ' + line[0] + " " + str(line[1]) + '\n'
                Leaders += s
                rank += 1
                if rank == 6:
                    break

            return Leaders

        break
