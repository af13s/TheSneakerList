//
//  View2.swift
//  TheSneakerList
//
//  Created by Andrew Florial on 7/9/16.
//  Copyright © 2016 Florial. All rights reserved.
//

import Foundation
import UIKit

class View2: UIViewController, UIPickerViewDelegate, UIPickerViewDataSource {
    
    
    
    @IBOutlet var Name_Label: UILabel!
    @IBOutlet var Size_Picker: UIPickerView!
    @IBOutlet var Price_Label: UILabel!
    @IBOutlet weak var Image_Display: UIImageView!
    @IBOutlet var CodeName_Label: UILabel!
    
    var displayshoe: shoeObj!
    
    override func viewDidLoad()
    {
        super.viewDidLoad()
        
        self.Size_Picker.delegate = self
        self.Size_Picker.dataSource = self
        
        Name_Label.text = displayshoe.fullname.uppercased()
        Price_Label.text = displayshoe.lprice.uppercased()
        CodeName_Label.text = displayshoe.codename?.uppercased()
        
        loadImageFromUrl(displayshoe.imgURL, view: Image_Display)
        
    }
    
    func numberOfComponents(in pickerView: UIPickerView) -> Int
    {
        return 1
    }
    
    func loadImageFromUrl(_ url: String, view: UIImageView){
        
        // Create Url from string
        let url = URL(string: url)!
        
        // Download task:
        // - sharedSession = global NSURLCache, NSHTTPCookieStorage and NSURLCredentialStorage objects.
        let task = URLSession.shared.dataTask(with: url, completionHandler: { (responseData, responseUrl, error) -> Void in
            // if responseData is not null...
            if let data = responseData{
                
                // execute in UI thread
                DispatchQueue.main.async(execute: { () -> Void in
                    view.image = UIImage(data: data)
                })
            }
        }) 
        
        // Run task
        task.resume()
    }
    
    
    
    
    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int
    {
        return displayshoe.sizeArr.count
    }
    
    func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
        return displayshoe.sizeArr[row]
    }
    
    
    func pickerView(_ pickerView: UIPickerView, didSelectRow row: Int, inComponent component: Int) {
        print (displayshoe.sizeArr[row])
    }
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    
}
