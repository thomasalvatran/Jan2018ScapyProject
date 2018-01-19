with open("test.csv", "r") as f:
    num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  #2010-2020 is num[0]
    for line in f:
        if "2020" in line:
            num[10] += 1
        if "2019" in line:
            num[9] += 1
        if "2018" in line:
            num[8] += 1
        elif "2017" in line:
            num[7] += 1
        elif "2016" in line:
            num[6] += 1
        elif "2015" in line:
            num[5] += 1
        elif "2014" in line:
            num[4] += 1
        elif "2013" in line:
            num[3] += 1
        elif "2012" in line:
            num[2] += 1
        elif "2011" in line:
            num[1] += 1
        elif "2010" in line:
            num[0] += 1

    # print "line " + str(num)
    sum = 0
    index = 0
    for i in num:
        if index == 0:
            print "In 2010 has post " + str(i)
        if index == 1:
            print "In 2011 has post " + str(i)
        if index == 2:
            print "In 2012 has post " + str(i)
        if index == 3:
            print "In 2013 has post " + str(i)
        if index == 4:
            print "In 2014 has post " + str(i)
        if index == 5:
            print "In 2015 has post " + str(i)
        if index == 6:
            print "In 2016 has post " + str(i)
        if index == 7:
            print "In 2017 has post " + str(i)
        if index == 8:
            print "In 2018 has post " + str(i)
        if index == 9:
            print "In 2019 has post " + str(i)
        if index == 10:
            print "In 2020 has post " + str(i)
        index += 1
        sum += i

    print "Total post :     " + str(sum)
