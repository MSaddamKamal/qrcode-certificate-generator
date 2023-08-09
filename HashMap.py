# HashMap data sturcture class

class Hashmap:
    def __init__(self):
        # defining the size of Memory that the hashmap should use
        self.SIZE_OF_HASHMAP_ARRAY = 10
        self.dummyArray = [[] for i in range(self.SIZE_OF_HASHMAP_ARRAY)]
        
    def createHash(self,key):
        convertedKey = 0
        for eachCharacter in key:
            # converting key provided by user in equivalent hash key 
            convertedKey += ord(eachCharacter)
            # determining the index postion to save the record later in the array using
            # below formula.
        return convertedKey % self.SIZE_OF_HASHMAP_ARRAY

    def addRecord(self,key,value):
        # adding record in hashmap
        # creaing hash of the provided key to determin index of array to save record
        hashedKey = self.createHash(key)
        found = False
        
        # if the record already exist then update it
        for index,element in enumerate(self.dummyArray[hashedKey]):
            if element[0] == key and len(element) == 2:
                self.dummyArray[hashedKey][index] = (key,value)
                found = True
                break
        # other wise append new record in the array
        if not found:
            self.dummyArray[hashedKey].append((key,value))
         
                
    def searchRecordByKey(self,key):
        hashedKey = self.createHash(key)
        # searching for record
        for item in self.dummyArray[hashedKey]:
            # if key matches
            if item[0] == key:
                print('\n\t\t\t**********Search Result********** ','\n')
                # formating results in table form to look good
                format = "{:<20}{:<20}{:<20}{:<20}"    
                # print the result
                print('\t',format.format("ID","NAME","COURSE","MARKS"))
                # accessing index 1 as it contains the value against key
                print('\t',format.format(item[1]['id'],item[1]['name'],item[1]['course'],item[1]['marks']))
            
    
    def deleteRecordByKey(self,key):
        # deleting record
        hash_key = self.createHash(key)
        for index,item in enumerate(self.dummyArray[hash_key]):
            # if key matches
            if item[0] == key:
                # delete item
                del self.dummyArray[hash_key][index]
    

    def listAllRecords(self):
        # listing all records
        print('\n\t\t\t**********All Record List********** ','\n')
        # formating results in table form to look good
        format = "{:<20}{:<20}{:<20}{:<20}"    
        print('\t',format.format("ID","NAME","COURSE","MARKS"))
        for item in self.dummyArray:
            # ignoring all the empty spaces in hashmap
            if(item != []):
                for subItem in item:
                    # accessing index 1 as it contains the value against key
                    print('\t',format.format(subItem[1]['id'],subItem[1]['name'],subItem[1]['course'],subItem[1]['marks']))
                

   

        


 
 