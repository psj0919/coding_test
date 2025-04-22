def solution(wallet, bill):
    answer = 0
    w_w = wallet[0]
    w_h = wallet[1]

    b_w = bill[0]
    b_h = bill[1]

    if (w_w >= b_w and w_h >= b_h) or (w_w >= b_h and w_h >= b_w):
        answer = 0
    else:
        answer += 1
        while True:
            if b_w > b_h:
                b_w = int(b_w / 2)
                if (w_w >=b_w and w_h >= b_h) or (w_w>=b_h and w_h >= b_w):
                    break
                else:
                    answer += 1
            else:
                b_h = int(b_h / 2)
                if (w_w >=b_w and w_h >= b_h) or (w_w>=b_h and w_h >= b_w):
                    break
                else:
                    answer += 1


    return answer






if __name__=='__main__':
    print(int(100/2))