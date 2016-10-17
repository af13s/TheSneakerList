//
//  StartPage.swift
//  TheSneakerList
//
//  Created by Andrew Florial on 7/8/16.
//  Copyright © 2016 Florial. All rights reserved.
//

import Foundation
import UIKit

class StartPage: UIViewController, UITableViewDelegate, UITableViewDataSource, UITextFieldDelegate {
    
    
    
    @IBOutlet var textField: UITextField!
    @IBOutlet weak var autocompleteTableView: UITableView!
    
    var autocompleteShoeNames = [String]()
    
    
    ////// * DataBase List Import Function in the future
    
    var shoeList = [" yeezy boost 350 *pirate black (2016 release)* | $1,250 | http://www.flightclub.com/adidas-yeezy-boost-350-pirate-black-2016-release-pirblk-blugra-cblack-201189 | ['4', '4.5', '5', '6', '6.5', '7', '7.5', '8', '8.5', '9', '9', '9.5', '10', '10.5', '11', '11.5', '12.5', '13', '13.5', '14', '14.5', '15', '16', '17', '18'] | http://media.flightclub.com/media/catalog/product/cache/1/small_image/234x167/9df78eab33525d08d6e5fb8d27136e95/a/d/adidas-yeezy-boost-350-pirate-black-2016-release-pirblk-blugra-cblack-201189_1.jpg ",
                    " yeezy boost 750 | $1,750 | http://www.flightclub.com/adidas-yeezy-boost-750-lgtgre-lgtgrt-gum3-201296 | ['6', '6.5', '7', '7.5', '8', '8.5', '9', '9', '9.5', '10', '10.5', '11', '11.5', '12.5', '13', '13.5', '14'] | http://media.flightclub.com/media/catalog/product/cache/1/small_image/234x167/9df78eab33525d08d6e5fb8d27136e95/6/3/63600839266-adidas-yeezy-boost-750-lgtgre-lgtgrt-gum3-201296_1.jpg ",
                    " yeezy boost 350 *oxford tan* | $1,250 | http://www.flightclub.com/adidas-yeezy-boost-350-oxford-tan-lgtsto-oxftan-lgtsto-201172 | ['4.5', '5', '5.5', '6', '6.5', '7', '7.5', '8', '8.5', '9', '9', '9.5', '10', '10.5', '11', '11.5', '12.5', '13.5', '14', '14.5'] | http://media.flightclub.com/media/catalog/product/cache/1/small_image/234x167/9df78eab33525d08d6e5fb8d27136e95/a/d/adidas-yeezy-boost-350-oxford-tan-lgtsto-oxftan-lgtsto-201172_1.jpg ",
                    " yeezy boost 350 *turtle dove* | $2,000 | http://www.flightclub.com/adidas-yeezy-boost-350-turtle-dove-turtle-blugra-cwhite-201114 | ['5', '6', '7', '8', '10', '11', '12', '12', '13'] | http://media.flightclub.com/media/catalog/product/cache/1/small_image/234x167/9df78eab33525d08d6e5fb8d27136e95/a/d/adidas-yeezy-boost-350-turtle-blugra-cwhite-201114_1.jpg ",
                    " yeezy boost 350 *pirate black* | $1,250 | http://www.flightclub.com/adidas-yeezy-boost-350-pirate-black-pirblk-pirblk-pirblk-201122 | ['4', '4.5', '5', '5.5', '6', '6.5', '7', '7.5', '8', '8.5', '9', '9', '9.5', '10', '10.5', '11', '11.5', '12.5', '13', '13.5', '14', '14.5', '15', '16', '17'] | http://media.flightclub.com/media/catalog/product/cache/1/small_image/234x167/9df78eab33525d08d6e5fb8d27136e95/a/d/adidas-yeezy-boost-350-pirblk-pirblk-pirblk-201122_1.jpg ",
                    " yeezy boost 350 *moonrock* | $1,250 | http://www.flightclub.com/adidas-yeezy-boost-350-moonrock-agagra-moonro-agagra-201153 | ['4', '4.5', '5', '6', '6.5', '7', '7.5', '8', '8.5', '9.5', '10', '10.5', '11', '11.5', '12', '12.5', '13.5', '14', '18'] | http://media.flightclub.com/media/catalog/product/cache/1/small_image/234x167/9df78eab33525d08d6e5fb8d27136e95/a/d/adidas-yeezy-boost-350-moonrock-agagra-moonro-agagra-201153_1.jpg ",
                    " yeezy boost 750 | $2,000 | http://www.flightclub.com/adidas-yeezy-boost-750-cblack-cblack-cblack-201169 | ['6', '7', '8', '9', '9', '10', '11', '12', '13', '14', '15'] | http://media.flightclub.com/media/catalog/product/cache/1/small_image/234x167/9df78eab33525d08d6e5fb8d27136e95/a/d/adidas-yeezy-750-boost-cblack-cblack-cblack-201169_1.jpg ",
                    " yeezy 750 boost | $2,500 | http://www.flightclub.com/adidas-yeezy-750-boost-lbrown-cwhite-lbrown-201060 | ['6', '7', '8', '9', '10', '11', '12', '12', '13'] | http://media.flightclub.com/media/catalog/product/cache/1/small_image/234x167/9df78eab33525d08d6e5fb8d27136e95/a/d/adidas-yeezy-750-boost-lbrown-cwhite-lbrown-201060_1.png ",
                    " yeezy 950 m | $950 | http://www.flightclub.com/adidas-yeezy-950-m-pirblk-pirblk-pirblk-201146 | ['6.5', '7'] | http://media.flightclub.com/media/catalog/product/cache/1/small_image/234x167/9df78eab33525d08d6e5fb8d27136e95/a/d/adidas-yeezy-950-m-pirblk-pirblk-pirblk-201146_1.jpg "]
    var nameList = ["yeezy boost 350 pirate black (2016 release)",
                    "yeezy boost 750",
                    "yeezy boost 350 oxford tan",
                    "yeezy boost 350 turtle dove",
                    "yeezy boost 350 pirate black",
                    "yeezy boost 350 moonrock",
                    "yeezy boost 750",
                    "yeezy 750 boost",
                    "yeezy 950 m"]
    
    
    
    
    //// Database contained data
    
    
    //let autocompleteTableView = UITableView(frame: CGRectMake(0,80,320,120), style: UITableViewStyle.Plain)
    
    //////////
    override func viewDidLoad()
    {
        super.viewDidLoad()
        
        textField.delegate = self
        autocompleteTableView!.delegate = self
        autocompleteTableView!.dataSource = self
        autocompleteTableView!.isScrollEnabled = true
        autocompleteTableView!.isHidden = true
    }
    
    
    
    ///////////
    func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool
    {
        
        autocompleteTableView.isHidden = false
        
        let substring = (textField.text! as NSString).replacingCharacters(in: range, with: string)
        
        searchAutocompleteEntriesWithSubstring(substring)
        return true     // not sure about this - could be false
    }
    
    
    
    //////////
    func searchAutocompleteEntriesWithSubstring(_ substring: String)
    {
        autocompleteShoeNames.removeAll(keepingCapacity: false)
        
        for curString in nameList
        {
            let myString:NSString! = curString as NSString
            
            let substringRange :NSRange! = myString.range(of: substring, options: .caseInsensitive)
            
            if (substringRange.location  == 0 || curString.contains(substring.lowercased()))
                
            {
                autocompleteShoeNames.append(curString)//uppercaseString
            }
            
        }
        
        autocompleteTableView!.reloadData()
    }
    
    
    
    ////////////
    override func didReceiveMemoryWarning()
    {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    
    //////////
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int
    {
        return autocompleteShoeNames.count
    }
    
    
    
    ////////
    func textFieldShouldReturn(_ textField: UITextField) -> Bool
    {
        self.view.endEditing(true)
        return false
    }
    
    
    /////////////
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell
    {
        
        let autoCompleteRowIdentifier = "cell"
        let cell : UITableViewCell = tableView.dequeueReusableCell(withIdentifier: autoCompleteRowIdentifier, for: indexPath) as UITableViewCell
        let index = (indexPath as NSIndexPath).row as Int
        cell.textLabel!.text = autocompleteShoeNames[index]
        return cell
    }
    
    
    ////////////
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath)
    {
        let selectedCell : UITableViewCell = tableView.cellForRow(at: indexPath)!
        textField.text = selectedCell.textLabel!.text
        self.autocompleteTableView!.isHidden = true

    }
    
    
    
    //////////////
    override func prepare(for segue: UIStoryboardSegue, sender: Any?)
    {
            let destviewcon = segue.destination as! View2
            let found = shoeObj(l: shoeList[nameList.index(of: textField.text!.lowercased())!])
            
            destviewcon.displayshoe = found
        
    }
    
    
    
    
    
}

