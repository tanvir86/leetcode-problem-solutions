class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        pathArray = []
            
        # traverse the path
        
        # check for /, .., ., other ch
        # start with /
        # trim end /
        # for every / check previous
        # for every . check next ch
            
        
        length = len(path)
        pathArray.append("/")
        i = 1 if path[0] == '/' else 0
        
        while i < length:
            if path[i] == "/":
                if pathArray[-1] != "/":
                    pathArray.append("/")
            elif path[i] == ".":
                count = 1
                while i+count < length and path[i+count] == ".":
                    count += 1
                if count == 1 and (i + count >= length or path[i+count] == "/") and pathArray[-1] == "/": #skip .
                    i += 1
                    continue
                elif count == 2 and (i + count >= length or path[i+count] == "/") and pathArray[-1] == "/":
                    if len(pathArray) > 1:
                        if pathArray[-1] == "/":
                            pathArray.pop(-1)
                        pathArray.pop(-1)           
                else :
                    if pathArray[-1] == "/":
                        pathArray.append(path[i:i+count])
                    else:
                        pathArray[-1] = pathArray[-1] + path[i:i+count]
                i = i + count -1
            else:
                count = 1
                while i+count < length and path[i+count] != "." and path[i+count] != "/":
                    count += 1
                if pathArray[-1] == "/":
                    pathArray.append(path[i:i+count])
                else:
                    pathArray[-1] = pathArray[-1] + path[i:i+count]
                i = i + count -1
            i += 1
        
        if len(pathArray) > 1 and pathArray[-1] == "/":
            pathArray.pop(-1)
        
        return  "".join(pathArray)
