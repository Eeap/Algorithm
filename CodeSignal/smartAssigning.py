def solution(names, statuses, projects, tasks):
    p = 26
    t = 101
    n = ""
    for idx in range(len(names)):
        if not statuses[idx]:
            if tasks[idx]< t or projects[idx]< p:
                if (tasks[idx],projects[idx]) < (t,p):
                    p = projects[idx]
                    t = tasks[idx]
                    n = names[idx]
    return n
