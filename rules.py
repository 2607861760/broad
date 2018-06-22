def rules(*args):
    def data(list):
        maxlist=[]
        allResults = []
        newlist=[]
        for index in range(len(list[0])):
            newlists=[]
            for n in range(len(list)):
                newlists.append(list[n][index])
            newlist.append(newlists)
            maxlist.append(max(newlists))
        for index in range(len(newlist)):
            results=[]
            for listitems in newlist[index]:
                item=maxlist[index]
                if item==0:
                    result==0
                else:
                    result=listitems/item*100
                results.append(result)
            allResults.append(results)
        newResults=[]
        for nowindex in range(len(allResults[0])):
            nowlist=[]
            for nowIndex in range(len(allResults)):
                nowlist.append(allResults[nowIndex][nowindex])
            newResults.append(nowlist)
        return newResults
    return data(args[0]),data(args[1]),data(args[2]),data(args[3])










