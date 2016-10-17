//
//  shoeObj.swift
//  TheSneakerList
//
//  Created by Andrew Florial on 7/8/16.
//  Copyright © 2016 Florial. All rights reserved.
//

import Foundation

class shoeObj
{
    
    var line : String!
    var name : String!
    var lprice :String!
    var URL : String!
    var fullname: String!
    var codename: String?
    var sizeArr = [String]()
    var imgURL: String!
    
    init(l: String)
    {
        self.line = l
        
        print ("STRING: "+self.line)
        print()
        
        var propArr = line.components(separatedBy: "|")
        self.name = propArr[0]
        print ("NAME: "+self.name)
        print()
        
        
        var nameArr = self.name.components(separatedBy: "*")
        
        let isIndexValid = nameArr.indices.contains(1)
        
        if (isIndexValid == true)
        {self.codename = nameArr[1]}
        else{codename = ""}
        
        print ("CODENAME: "+self.codename!)
        print ()
        
        
        self.fullname = nameArr[0]
        print ("REGULAR NAME"+self.fullname)
        print()
        
        
        self.lprice = propArr[1]
        print ("PRICE: "+self.lprice)
        print()
        
        
        self.URL = propArr[2]
        print ("URL"+self.URL)
        print()
        
        
        var sizeformat = propArr[3].replacingOccurrences(of: "[", with: "", options: NSString.CompareOptions.literal, range: nil)
        
        sizeformat = sizeformat.replacingOccurrences(of: "]", with: "", options: NSString.CompareOptions.literal, range: nil)
        
        sizeformat = sizeformat.replacingOccurrences(of: "'", with: "", options: NSString.CompareOptions.literal, range: nil)
        
       sizeArr = sizeformat.components(separatedBy: ",")
        print ("SIZEARRAY: ",self.sizeArr)
        
        self.imgURL = propArr[4]
        self.imgURL = self.imgURL.replacingOccurrences(of: " ", with: "", options: NSString.CompareOptions.literal, range: nil)
        print ("IMGURL ",self.imgURL)
        
    }
}
