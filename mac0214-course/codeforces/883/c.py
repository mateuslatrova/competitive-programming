t = int(input())
for i in range(t):
    n, m, h = map(int, input().split())

    p = []
    for i in range(n):
        minutes = list(map(int, input().split()))
        minutes.sort()
        p.append(minutes)

    classification = []
    for i in range(n):
        pts = 0
        time_already_spent = 0
        penalty = 0
        for curr_time in p[i]:
            time_to_solve_this_problem = curr_time + time_already_spent
            if time_to_solve_this_problem <= h:
                pts += 1
                time_already_spent += curr_time
                penalty += time_to_solve_this_problem
            else:
                break
        classification.append((pts, -penalty, i))

    classification.sort(reverse=True)

    if (
        len(classification) > 1
        and (classification[0][2] == 0 or classification[1][2] == 0)
        and classification[0][0] == classification[1][0]
        and classification[0][1] == classification[1][1]
    ):
        rudolph_position = 1
    else:
        rudolph_position = 0
        for idx, c in enumerate(classification):
            if c[2] == 0:
                rudolph_position = idx + 1
                break

    print(rudolph_position)
