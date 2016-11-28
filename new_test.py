from more_itertools import unique_everseen
import itertools


def checker(liter):
    check_list = list()
    for im in range(len(liter)):
        af = str(liter[im])
        mid_list = af
        for xx in range(len(mid_list)):
            for ro in range(len(mid_list)):
                if mid_list[ro] == mid_list[xx]:
                    continue
                else:
                    alp = str(xx) + str(ro)
                    check_list.append(alp)
    check_list1 = list(unique_everseen(check_list))
    check_list1.sort()
    return check_list1


def invert(item):
    d = list()
    for k in range(len(item)):
        copy = list(item[k])
        for l in range(len(copy)):
            if copy[l] == str(1):
                copy[l] = str(0)
                continue
            if copy[l] == str(0):
                copy[l] = str(1)
        copy = ''.join(copy)
        d.append(copy)
    for k in range(len(d)):
        if d[k] in item:
            item.remove(d[k])
    return item


def compliment_stuck(item):
    d = list()
    for k in range(len(item)):

        copy = list(item[k])
        for l in range(len(copy)):
            if copy[l] == str(1):
                copy[l] = str(0)
                continue
            if copy[l] == str(0):
                copy[l] = str(1)
        copy = ''.join(copy)
        d.append(copy)
    d = ''.join(d)
    return d


def main_fun(aalist):
    mid_list1 = list()
    for ins in range(len(aalist)):
        op_list = str(aalist[ins])
        var1 = op_list + '0'
        var2 = op_list + '1'
        mid_list1.append(var1)
        mid_list1.append(var2)
    return list(unique_everseen(mid_list1))


mid_list = list()
op_list = list()
test = []
check_list1 = list()
aloo = list()
alist = ['01']

inu = int(input('ENTER NUMBER OF MORE LINES YOU WANT TO MANIPULATE'))

if inu == 1:
    print 'Invalid Input'
if inu == 2:
    print 'Test Pattern for Bridging fault', alist
    test=alist

if inu > 2:
    for amy in range(3, inu + 1):
        alist = main_fun(alist)

    for ipo in range(0, inu):
        aloo.append(ipo)
    aloo = list(itertools.permutations(aloo, 2))
    aloo.sort()

    for iii in range(len(aloo)):
        var1 = str(aloo[iii][0])
        for jjj in range(1, len(aloo[iii])):
            var1 += str(aloo[iii][jjj])
        aloo[iii] = var1
    check_list1.sort()
    aloo.sort()
    alist = invert(alist)
    combs = []
    for qw in xrange(1, len(alist) + 1):
        els = [list(x) for x in itertools.combinations(alist, qw)]
        combs.extend(els)
    for qwe in range(len(combs)):
        amp = checker(combs[qwe])
        if str(amp) == str(aloo):
            print 'Test Pattern for Bridging fault', combs[qwe]
            test = combs[qwe]
            break
if inu>1:
    news = compliment_stuck(test[0])
    test.append(news)
    print 'Test Pattern for Stuck-at-Fault', test
