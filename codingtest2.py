def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    max_m, max_s = video_len.split(":")
    cur_m, cur_s = pos.split(":")
    op_start_m, op_start_s = op_start.split(":")
    op_end_m, op_end_s = op_end.split(":")

    if op_start_m <= cur_m and cur_m <= op_end_m:
        if cur_m == op_end_m and cur_s == op_end_s:
            pass

        elif cur_m == op_end_m and cur_m == op_start_m:
            if int(cur_s) > int(op_end_s):
                pass
            elif int(cur_s) < int(op_start_s):
                pass
            else:
                cur_m = op_end_m
                cur_s = op_end_s

        elif cur_m == op_start_m:
            if int(cur_s) < int(op_start_s):
                pass
            else:
                cur_m = op_end_m
                cur_s = op_end_s
        else:
            cur_m = op_end_m
            cur_s = op_end_s

    for i in commands:

        if op_start_m <= cur_m and cur_m <= op_end_m:
            if cur_m == op_end_m and cur_s == op_end_s:
                pass
            elif cur_m == op_end_m and cur_m == op_start_m:
                if int(cur_s) > int(op_end_s):
                    pass
                elif int(cur_s) < int(op_start_s):
                    pass
                else:
                    cur_m = op_end_m
                    cur_s = op_end_s
            elif cur_m == op_start_m:
                if int(cur_s) < int(op_start_s):
                    pass
                else:
                    cur_m = op_end_m
                    cur_s = op_end_s
            else:
                cur_m = op_end_m
                cur_s = op_end_s

        if i == 'prev':
            if int(cur_m) == 0 and int(cur_s) == 0:
                cur_m = cur_m
                cur_s = cur_s
            if int(cur_m) == 0 and int(cur_s) <= 10:
                cur_m = '00'
                cur_s = '00'
            else:
                if int(cur_s) < 10:
                    if int(cur_m) <= 10:
                        cur_m = "0"+str(int(cur_m)-1)
                        cur_s = str(int(cur_s)+60-10)
                    else:
                        cur_m = str(int(cur_m)-1)
                        cur_s = str(int(cur_s) + 60 - 10)
                else:
                    cur_m = cur_m
                    if int(cur_s) - 10 == 0:
                        cur_s = "00"
                    elif int(cur_s) - 10 < 10:
                        cur_s = "0" + str(int(cur_s) - 10)
                    else:
                        cur_s = str(int(cur_s) - 10)



        elif i == 'next':
            if int(cur_m) == int(max_m) and abs(int(cur_s) - int(max_s)) <10:
                cur_m = max_m
                cur_s = max_s

            else:
                if int(cur_s) > 50:
                    if int(cur_m) < 10:
                        cur_m = "0"+str(int(cur_m)+1)
                        cur_s = "0"+str(int(cur_s)+10-60)
                    else:
                        cur_m = str(int(cur_m)+1)
                        cur_s = "0" + str(int(cur_s) + 10 - 60)
                else:
                    cur_m = cur_m
                    cur_s = str(int(cur_s)+10)

    if int(cur_m) == int(max_m):
        if int(cur_s) + 10 > int(max_s):
            cur_m = max_m
            cur_s = max_s

    if op_start_m <= cur_m and cur_m <= op_end_m:
        if cur_m == op_end_m:
            if int(cur_s) > int(op_end_s):
                pass
            elif cur_m == op_end_m and cur_m == op_start_m:
                if int(cur_s) > int(op_end_s):
                    pass
                elif int(cur_s) < int(op_start_s):
                    pass
                else:
                    cur_m = op_end_m
                    cur_s = op_end_s
        elif cur_m == op_start_m:
            if int(cur_s) < int(op_start_s):
                pass
            else:
                cur_m = op_end_m
                cur_s = op_end_s
        else:
            cur_m = op_end_m
            cur_s = op_end_s

    answer = cur_m + ":" + cur_s
    return answer



if __name__=='__main__':
    x = solution("30:00", "15:00", "15:10", "15:30", ["next", "next"])
    print(x)
